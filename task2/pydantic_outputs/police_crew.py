from pydantic import BaseModel, Field
from typing import List, Optional


class TaskforceAssignment(BaseModel):
    """Output for assigning the taskforce."""

    n_officers: int = Field(
        ..., description="Number of officers assigned to the situation."
    )
    action_details: str = Field(
        ..., description="Details of the situation assessment action."
    )


class PerimeterControlPlanning(BaseModel):
    """Output for planning perimeter control."""

    perimeter_locations: List[str] = Field(
        ..., description="List of locations defining the perimeter."
    )
    action_details: str = Field(
        ..., description="Details of the perimeter control plan."
    )


class PatrolSelection(BaseModel):
    """Output for assigning vehicles."""

    patrol_vehicles: List[str] = Field(
        ..., description="List of assigned patrol vehicles."
    )
    action_details: str = Field(
        ..., description="Details of the vehicle assignment process."
    )


class RoutePlanning(BaseModel):
    """Output for planning patrol routes."""

    patrol_routes: List[tuple[str, List[int]]] = Field(
        ..., description="List of planned patrol routes."
    )
    action_details: str = Field(
        ..., description="Details of the route planning process."
    )


class PolicePlanCompilation(BaseModel):
    """Comprehensive output for compiling the police plan."""

    response_plan: str = Field(
        ..., description="Compiled response plan for the police operation."
    )
    ethical_issues: Optional[str] = Field(
        None, description="Ethical issues considered in the plan."
    )
    action_details: str = Field(
        ..., description="Additional details of the overall police plan."
    )
