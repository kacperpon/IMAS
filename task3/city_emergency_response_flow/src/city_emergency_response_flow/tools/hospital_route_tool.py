from typing import List, Type
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
import osmnx as ox
import networkx as nx
import json, os

from city_emergency_response_flow.crews.firefighting_crew.schemas.schemas import RoutePlanning

class HospitalRouteToolInput(BaseModel):
    """
    EmergencyRouteToolInput is a Pydantic model that defines the input schema for the emergency route tool.
    Attributes:
        hospital_names (List[str]): List of the hospital names.
        origin_lat (float): Latitude of the emregency/incident location.
        origin_lon (float): Longitude of the emergency/incident location.
        destination_lats (List[float]): List of the Latitudes of all hosptial locations.
        destination_lons (List[float]): List of the Longitudes of all hospital locations.
    """
    
    # vehicle_type: str = Field(
    #     ...,
    #     description="Type of the vehicle. CAN ONLY BE firetruck, ambulance, or patrol.",
    # )
    hospital_names: str = Field(
        ...,
        description="Stringified list of the hospital names.",
    )
    origin_lat: float = Field(
        ..., description="Latitude of the emergency/incident location."
    )
    origin_lon: float = Field(
        ..., description="Longitude of the emergency/incident location."
    )
    destination_lats: str = Field(
        ..., description="Stringified list of the Latitudes of all hosptial locations."
    )
    destination_lons: str = Field(
        ..., description="Stringified list of the Longitudes of all hospital locations."
    )


class HospitalRouteTool(BaseTool):
    name: str = "hospital_route_tool"
    description: str = (
        "This tool calculates an optimal route from an origin to a destination "
        "for different emergency vehicles using OSMnx and networkx."
    )
    args_schema: Type[BaseModel] = HospitalRouteToolInput

    def _run(
        self,
        hospital_names: str,
        origin_lat: float,
        origin_lon: float,
        destination_lats: str,
        destination_lons: str,
    ) -> str:
        """
        Internal method to run the route calculation. It returns pydantic model RoutePlanning.
        """
        
        print("Received values:")
        print(hospital_names)
        print(destination_lats)
        print(destination_lons)
        
        # print("Received dtypes:")
        # print(type(vehicle_ids))
        # print(type(origin_lats))
        # print(type(origin_lons))
        
        try:
            hospital_names = json.loads(hospital_names)
            destination_lons = json.loads(destination_lons)
            destination_lats = json.loads(destination_lats)
            
            # print("Parsed values:")
            # print(vehicle_ids)
            # print(origin_lats)
            # print(origin_lons)
            
            # print("Parsed dtypes:")
            # print(type(vehicle_ids))
            # print(type(origin_lats))
            # print(type(origin_lons))
            
            
        except Exception as e:
            return f"Error occurred while parsing input: {str(e)}"
        
        tuples = list()
        
        for idx, hospital_name in enumerate(hospital_names):
            print("Calculatin route for hospital: ", hospital_name)
            destination_lat = destination_lats[idx]
            destination_lon = destination_lons[idx]
            
        
            
            try:
                # 1. Create a drivable street network around the vehicle's origin.
                # Adjust 'dist' to expand or limit the search area.
                G = ox.graph_from_point(
                    center_point=(origin_lat, origin_lon),
                    dist=2000,  # in metres
                    network_type="drive",
                )

                # 2. Identify the nodes in the graph nearest to the origin and destination.
                orig_node = ox.distance.nearest_nodes(G, origin_lon, origin_lat)
                dest_node = ox.distance.nearest_nodes(G, destination_lon, destination_lat)

                # 3. Calculate the shortest path (by length) between these two nodes.
                route = nx.shortest_path(G, orig_node, dest_node, weight="length")

                # 4. Convert node-based path into a list of (lat, lon) pairs.
                route_coordinates = [
                    (G.nodes[node]["y"], G.nodes[node]["x"]) for node in route
                ]

                # 5. Create a result dictionary for clarity.
                result = {
                    "vehicle_type": hospital_name,
                    "origin": [origin_lat, origin_lon],
                    "destination": [destination_lat, destination_lon],
                    "route_nodes": route,
                    "route_coordinates": route_coordinates,
                }
                
                # Only used for ambulances.
                vehicle_type = "ambulance"
                

                
                # 6. Plotting the route
                
                try: 
                    fig, ax = ox.plot_graph_route(G, route, node_size=0)
                    if vehicle_type == "firetruck":
                        path = os.path.join("src", "city_emergency_response_flow", "crews", "firefighting_crew", "crew_outputs", f"firetruck_{hospital_name}_route.png")
                        
                    elif vehicle_type == "ambulance":
                        path = os.path.join("src", "city_emergency_response_flow", "crews", "medical_crew", "crew_outputs", f"ambulance_{hospital_name}_route.png")
                    elif vehicle_type == "patrol":
                        path = os.path.join("src", "city_emergency_response_flow", "crews", "patrol_crew", "crew_outputs", f"patrol_{hospital_name}_route.png")
                    else:
                        raise( f"Invalid vehicle type: {vehicle_type}")
                    
                    os.makedirs(os.path.dirname(path), exist_ok=True)
                    fig.savefig(path)
                
                except Exception as e:
                    print(f"Error occurred while plotting route: {str(e)}")
                
                tuples.append((hospital_name, route))
                
                
                
                
            except Exception as e:
                return f"Error occurred while calculating route: {str(e)}"
                
                

        new_route = RoutePlanning(
            routes=tuples,
            action_details="Route planning successful.",
        )

        # Return the result as JSON string.
        return new_route.model_dump_json()
        
