from pydantic import BaseModel, Field
from typing import List, Optional, Tuple


class TaskforceAssignment(BaseModel):
    """Output for assigning the taskforce."""

    n_officers: int = Field(
        ..., description="Number of officers assigned to the situation."
    )
    action_details: str = Field(
        ..., description="Details of the situation assessment action."
    )

    @classmethod
    def get_schema(cls) -> str:
        schema = "\n"
        for field_name, field_instance in cls.model_fields.items():
            schema += f"{field_name}, described as: {field_instance.description}\n"
        return schema


class PerimeterControlPlanning(BaseModel):
    """Output for planning perimeter control."""

    perimeter_locations: List[str] = Field(
        ..., description="List of locations defining the perimeter."
    )
    action_details: str = Field(
        ..., description="Details of the perimeter control plan."
    )

    @classmethod
    def get_schema(cls) -> str:
        schema = "\n"
        for field_name, field_instance in cls.model_fields.items():
            schema += f"{field_name}, described as: {field_instance.description}\n"
        return schema
    
# For PatrolSelection
class PatrolInformation(BaseModel):
    patrol_id: int = Field(
        ..., description="patrol_id of the selected patrol. (Eg: 1)"
    )
  
    patrol_location: Tuple[float, float] = Field(
        ..., description="patrol_location (composed of latitude and longitude values) of the selected patrol location."
    )
    patrol_status: str = Field(
        ..., description="patrol_status of the selected patrol (Eg: Available, In Service)"
    )


class PatrolSelection(BaseModel):
    """Output for assigning vehicles."""

    patrol_vehicles: List[PatrolInformation] = Field(
        ..., description="List of assigned patrol vehicles."
    )
    action_details: str = Field(
        ..., description="Details of the vehicle assignment process."
    )

    @classmethod
    def get_schema(cls) -> str:
        schema = "\n"
        for field_name, field_instance in cls.model_fields.items():
            schema += f"{field_name}, described as: {field_instance.description}\n"
        return schema

class RoutePlanning(BaseModel):
    """Output for planning the route."""
    
    route_duration_min: List[float] = Field(
        ..., description="The duration in minutes of the route."
    )
    action_details: str = Field(
        ..., description="Additional information on route planning."
    )

    @classmethod
    def get_schema(cls) -> str:
        schema = "\n"
        for field_name, field_instance in cls.model_fields.items():
            schema += f"{field_name}, described as: {field_instance.description}\n"
        return schema


class PolicePlanCompilation(BaseModel):
    """Comprehensive output for compiling the police plan."""

    response_plan: str = Field(
        ..., description="Compiled response plan for the police operation."
    )
    action_details: str = Field(
        ..., description="Additional details of the overall police plan."
    )

    @classmethod
    def get_schema(cls) -> str:
        schema = "\n"
        for field_name, field_instance in cls.model_fields.items():
            schema += f"{field_name}, described as: {field_instance.description}\n"
        return schema
