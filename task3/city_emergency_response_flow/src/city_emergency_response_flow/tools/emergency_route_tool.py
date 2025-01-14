from typing import List, Type
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
import osmnx as ox
import networkx as nx
import json, os

from city_emergency_response_flow.crews.firefighting_crew.schemas.schemas import (
    RoutePlanning,
)


class EmergencyRouteToolInput(BaseModel):
    """
    EmergencyRouteToolInput is a Pydantic model that defines the input schema for the emergency route tool.
    Attributes:
        vehicle_ids (List[str]): List of the Ids of all the vehicles.
        origin_lats (List[float]): List of the Latitudes of all the vehicle's current positions.
        origin_lons (List[float]): List of the Longitudes of the vehicle's current positions.
        destination_lat (float): Latitude of the emergency/incident location.
        destination_lon (float): Longitude of the emergency/incident location.
    """

    vehicle_type: str = Field(
        ...,
        description="Type of the vehicle. CAN ONLY BE firetruck, ambulance, or patrol.",
    )
    vehicle_ids: str = Field(
        ...,
        description="Stringified list of the Ids of all the vehicles.",
    )
    origin_lats: str = Field(
        ...,
        description="Stringified list of the Latitudes of all the vehicle's current positions.",
    )
    origin_lons: str = Field(
        ...,
        description="Stringified list of the Longitudes of the vehicle's current positions.",
    )
    destination_lat: float = Field(
        ..., description="Latitude of the emergency/incident location."
    )
    destination_lon: float = Field(
        ..., description="Longitude of the emergency/incident location."
    )


class EmergencyRouteTool(BaseTool):
    name: str = "emergency_route_tool"
    description: str = (
        "This tool calculates an optimal route from an origin to a destination "
        "for different emergency vehicles using OSMnx and networkx."
    )
    args_schema: Type[BaseModel] = EmergencyRouteToolInput

    def _run(
        self,
        vehicle_type: str,
        vehicle_ids: str,
        origin_lats: str,
        origin_lons: str,
        destination_lat: float,
        destination_lon: float,
    ) -> str:
        """
        Internal method to run the route calculation. It returns pydantic model RoutePlanning.
        """

        print("Received values:")
        print(vehicle_ids)
        print(origin_lats)
        print(origin_lons)

        try:
            vehicle_ids = json.loads(vehicle_ids)
            vehicle_ids = [str(vehicle_id) for vehicle_id in vehicle_ids]
            origin_lats = json.loads(origin_lats)
            origin_lons = json.loads(origin_lons)

        except Exception as e:
            return f"Error occurred while parsing input: {str(e)}"

        total_times = list()

        for idx, vehicle_id in enumerate(vehicle_ids):
            print("Calculatin route for vehicle: ", vehicle_id)
            origin_lat = origin_lats[idx]
            origin_lon = origin_lons[idx]

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
                dest_node = ox.distance.nearest_nodes(
                    G, destination_lon, destination_lat
                )

                G = ox.routing.add_edge_speeds(G)
                G = ox.routing.add_edge_travel_times(G)

                # 3. Calculate the shortest path (by length) between these two nodes.
                route = nx.shortest_path(G, orig_node, dest_node, weight="length")

                # 4. Convert node-based path into a list of (lat, lon) pairs.
                route_coordinates = [
                    (G.nodes[node]["y"], G.nodes[node]["x"]) for node in route
                ]

                # 5. Create a result dictionary for clarity.
                result = {
                    "vehicle_type": vehicle_id,
                    "origin": [origin_lat, origin_lon],
                    "destination": [destination_lat, destination_lon],
                    "route_nodes": route,
                    "route_coordinates": route_coordinates,
                }

                # 6. Plotting the route
                print("Plotting the route, for vehicle_type: ", vehicle_type)
                try:
                    fig, ax = ox.plot_graph_route(G, route, node_size=0)
                    if vehicle_type == "firetruck":
                        path = os.path.join(
                            "src",
                            "city_emergency_response_flow",
                            "crews",
                            "firefighting_crew",
                            "crew_outputs",
                            f"firetruck_{vehicle_id}_route.png",
                        )

                    elif vehicle_type == "ambulance":
                        path = os.path.join(
                            "src",
                            "city_emergency_response_flow",
                            "crews",
                            "medical_crew",
                            "crew_outputs",
                            f"ambulance_{vehicle_id}_route.png",
                        )
                    elif vehicle_type == "patrol":
                        path = os.path.join(
                            "src",
                            "city_emergency_response_flow",
                            "crews",
                            "police_crew",
                            "crew_outputs",
                            f"patrol_{vehicle_id}_route.png",
                        )
                    else:
                        raise (f"Invalid vehicle type: {vehicle_type}")

                    os.makedirs(os.path.dirname(path), exist_ok=True)
                    fig.savefig(path)

                except Exception as e:
                    print(f"Error occurred while plotting route: {str(e)}")

                total_time = round(
                    sum(ox.routing.route_to_gdf(G, route)["travel_time"])
                )  # In seconds
                total_time = total_time / 60  # In minutes
                total_times.append(total_time)
                print(f"Total time for vehicle {vehicle_id}: {total_time} minutes")

            except Exception as e:
                return f"Error occurred while calculating route: {str(e)}"

        new_route = RoutePlanning(
            route_duration_min=total_times,
            action_details="Route planning successful.",
        )

        # Return the result as JSON string.
        return new_route.model_dump_json()
