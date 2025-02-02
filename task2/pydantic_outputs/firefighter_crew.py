from pydantic import BaseModel, Field
from typing import List, Optional


class TaskforceAssignment(BaseModel):
    """Output for assigning the taskforce."""

    n_firefighters: int = Field(..., description="Number of firefighters assigned.")
    action_details: str = Field(
        ..., description="Additional details of the assignment action."
    )


class ExtinguishingToolSelection(BaseModel):
    """Output for selecting extinguishing tools."""

    extinguishing_tools: List[str] = Field(
        ..., description="List of selected tools for extinguishing."
    )
    action_details: str = Field(
        ..., description="Details of the tool selection process."
    )


class AssessBuildingStructurePlanning(BaseModel):
    """Output for assessing the building structure."""

    rescue_strategy: str = Field(..., description="Strategy for rescuing victims.")
    stop_fire_strategy: str = Field(..., description="Strategy for stopping the fire.")
    action_details: str = Field(
        ..., description="Further action details for building assessment."
    )


class VictimRescuePlanning(BaseModel):
    """Output for planning victim rescue."""

    ordered_victim_rescue: List[str] = Field(
        ..., description="List of victims ordered by rescue priority."
    )
    action_details: str = Field(
        ..., description="Details of the rescue planning process."
    )


class ToolSelection(BaseModel):
    """Output for selecting firefighting tools."""

    firefighting_tools: List[str] = Field(
        ..., description="List of selected firefighting tools."
    )
    action_details: str = Field(
        ..., description="Details about the tool selection process."
    )


class FireTruckSelection(BaseModel):
    """Output for selecting fire trucks."""

    fire_trucks: List[str] = Field(..., description="List of selected fire trucks.")
    action_details: str = Field(
        ..., description="Details of the fire truck selection process."
    )


class RoutePlanning(BaseModel):
    """Output for planning the route."""

    routes: List[tuple[str, List[int]]] = Field(
        ..., description="List of planned OSMnx routes for each fire truck."
    )
    action_details: str = Field(
        ..., description="Additional information on route planning."
    )


class FirePlanCompilation(BaseModel):
    """Comprehensive output for compiling the final plan."""

    response_plan: str = Field(
        ..., description="Compiled response plan for the firefighter operation."
    )
    ethical_issues: Optional[str] = Field(
        None, description="Ethical issues considered in the plan."
    )
    action_details: str = Field(
        ..., description="Additional details of the overall firefighter plan."
    )
