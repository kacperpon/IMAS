from typing import Type
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
import osmnx as ox
import networkx as nx
import json


class EmergencyRouteToolInput(BaseModel):
    """
    Input schema for EmergencyRouteTool.

    This schema captures the key parameters for routing:
    - vehicle_type: type of emergency vehicle
    - origin_lat/origin_lon: coordinates for the vehicle’s current position
    - destination_lat/destination_lon: coordinates for the incident location
    """

    vehicle_type: str = Field(
        ...,
        description="Type of emergency vehicle: 'firefighter_truck', 'ambulance', 'police_car'.",
    )
    origin_lat: float = Field(
        ..., description="Latitude of the vehicle's current position."
    )
    origin_lon: float = Field(
        ..., description="Longitude of the vehicle's current position."
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
        origin_lat: float,
        origin_lon: float,
        destination_lat: float,
        destination_lon: float,
    ) -> str:
        """
        Internal method to run the route calculation. It returns a stringified JSON
        containing details of the route.
        """
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
                "vehicle_type": vehicle_type,
                "origin": [origin_lat, origin_lon],
                "destination": [destination_lat, destination_lon],
                "route_nodes": route,
                "route_coordinates": route_coordinates,
            }

            # Return the result as JSON string.
            return json.dumps(result)

        except Exception as e:
            return f"Error occurred while calculating route: {str(e)}"
