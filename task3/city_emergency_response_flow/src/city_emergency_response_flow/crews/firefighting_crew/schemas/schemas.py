from pydantic import BaseModel, Field
from typing import List, Optional, Tuple


class TaskforceAssignment(BaseModel):
    """Output for assigning the taskforce."""

    n_firefighters: int = Field(..., description="Number of firefighters assigned.")
    action_details: str = Field(
        ..., description="Additional details of the assignment action."
    )

    @classmethod
    def get_schema(cls) -> str:
        schema = "\n"
        for field_name, field_instance in cls.model_fields.items():
            schema += f"{field_name}, described as: {field_instance.description}\n"
        return schema


class ExtinguishingToolSelection(BaseModel):
    """Output for selecting extinguishing tools."""

    extinguishing_tools: List[str] = Field(
        ..., description="List of selected tools for extinguishing."
    )
    action_details: str = Field(
        ..., description="Details of the tool selection process."
    )

    @classmethod
    def get_schema(cls) -> str:
        schema = "\n"
        for field_name, field_instance in cls.model_fields.items():
            schema += f"{field_name}, described as: {field_instance.description}\n"
        return schema


class AssessBuildingStructurePlanning(BaseModel):
    """Output for assessing the building structure."""

    rescue_strategy: str = Field(..., description="Strategy for rescuing victims.")
    stop_fire_strategy: str = Field(..., description="Strategy for stopping the fire.")
    action_details: str = Field(
        ..., description="Further action details for building assessment."
    )

    @classmethod
    def get_schema(cls) -> str:
        schema = "\n"
        for field_name, field_instance in cls.model_fields.items():
            schema += f"{field_name}, described as: {field_instance.description}\n"
        return schema


# For VictimRescuePlanning
class VictimInformation(BaseModel):
    victim_id: str = Field(
        ..., description="Identifier for the victim (e.g., Victim 1)"
    )
    condition: str = Field(..., description="Description of the victim's condition")
    priority_level: str = Field(
        ..., description="Rescue priority level (e.g., High, Medium, Low)"
    )


class VictimRescuePlanning(BaseModel):
    """Output for planning victim rescue."""

    ordered_victim_rescue: List[VictimInformation] = Field(
        ...,
        description="List of victims ordered by rescue priority, including their details.",
    )
    action_details: str = Field(
        ..., description="Details of the rescue planning process."
    )

    @classmethod
    def get_schema(cls) -> str:
        schema = "\n"
        for field_name, field_instance in cls.model_fields.items():
            schema += (
                f"{field_name}, described as: {field_instance.field_info.description}\n"
            )
        return schema


class ToolSelection(BaseModel):
    """Output for selecting firefighting tools."""

    firefighting_tools: List[str] = Field(
        ..., description="List of selected firefighting tools."
    )
    action_details: str = Field(
        ..., description="Details about the tool selection process."
    )

    @classmethod
    def get_schema(cls) -> str:
        schema = "\n"
        for field_name, field_instance in cls.model_fields.items():
            schema += f"{field_name}, described as: {field_instance.description}\n"
        return schema


# For FireTruckSelection
class FireTruckInformation(BaseModel):
    truck_id: int = Field(
        ..., description="truck_id of the selected fire truck. (Eg: 1)"
    )
    installed_tools: List[str] = Field(
        ..., description="List of tools which will be installed in the selected truck."
    )
    truck_location: Tuple[float, float] = Field(
        ...,
        description="truck_location (composed of latitude and longitude values) of the selected truck location.",
    )
    truck_status: str = Field(
        ...,
        description="truck_status of the selected truck (Eg: Available, In Service)",
    )


class FireTruckSelection(BaseModel):
    """Output for selecting fire trucks."""

    fire_trucks: List[FireTruckInformation] = Field(
        ..., description="List of selected fire trucks."
    )
    action_details: str = Field(
        ..., description="Details of the fire truck selection process."
    )

    @classmethod
    def get_schema(cls) -> str:
        schema = "\n"
        for field_name, field_instance in cls.model_fields.items():
            schema += f"{field_name}, described as: {field_instance.description}\n"
        return schema


class RoutePlanning(BaseModel):
    """Output for planning the route."""

    routes: List[Tuple[str, List[int]]] = Field(
        ..., description="List of planned OSMnx routes for each vehicle."
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


class FirePlanCompilation(BaseModel):
    """Comprehensive output for compiling the final plan."""

    response_plan: str = Field(
        ...,
        description="Summarized response plan including all outputs from before tasks for the firefighter operation.",
    )
    ethical_issues: Optional[str] = Field(
        None, description="Ethical issues considered in the plan."
    )
    

    @classmethod
    def get_schema(cls) -> str:
        schema = "\n"
        for field_name, field_instance in cls.model_fields.items():
            schema += f"{field_name}, described as: {field_instance.description}\n"
        return schema
