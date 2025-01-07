from crewai.tools import BaseTool
from pydantic import BaseModel, Field
import osmnx as ox
import unicodedata
from typing import Type


class GetCoordinatesInput(BaseModel):
    """Input schema for GetCoordinatesTool."""
    address: str = Field(..., description="The address to retrieve coordinates for.")

class GetCoordinatesTool(BaseTool):
    name: str = "get_coordinates"
    description: str = "Fetches the latitude and longitude of a given address using OSMnx."
    args_schema: Type[BaseModel] = GetCoordinatesInput

    def _run(self, address: str) -> str:
        """
        Retrieves the coordinates for a given address.

        Parameters:
            address (str): The address to geocode.

        Returns:
            str: The coordinates in the format 'latitude, longitude' or an error message.
        """
        try:
            cleaned_address = unicodedata.normalize('NFKC', address)
            print("cleaned address ", cleaned_address)
            point = ox.geocode(cleaned_address)
            return {point[0]}, {point[1]}
        except Exception as e:
            return f"Error occurred while retrieving coordinates: {e}"