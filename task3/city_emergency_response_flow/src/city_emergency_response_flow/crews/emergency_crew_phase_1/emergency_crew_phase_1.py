import os
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from .schemas.schemas import *
from typing import Type
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
import osmnx as ox
import unicodedata


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
            point = ox.geocode(cleaned_address)
            return f"Coordinates of '{address}': {point[0]}, {point[1]}"
        except Exception as e:
            return f"Error occurred while retrieving coordinates: {e}"


@CrewBase
class EmergencyCrewPhase1:
    """EmergencyCrewPhase1 crew"""

    llm = LLM(
       model= "gpt-4",
        api_key=os.getenv("OPENAI_API_KEY")  # Get the API key from environment variable
    )
    output_path = os.path.join(
        os.path.dirname(os.path.relpath(__file__)), "crew_outputs"
    )
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def distributor(self) -> Agent:
        return Agent(
            config=self.agents_config["distributor"], llm=self.llm, verbose=True,
            tools=[GetCoordinatesTool()]
        )

    @task
    def emergency_alert_distribution(self) -> Task:
        return Task(
            config=self.tasks_config["emergency_alert_distribution"],
            output_json=EmergencyAlertDistribution,
            output_file=os.path.join(
                self.output_path, "001_emergency_alert_distribution.json"
            ),
        )

    @crew
    def crew(self) -> Crew:
        """Creates the EmergencyCrewPhase1 crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
