from pydantic import BaseModel, Field
from typing import List, Optional


class TaskforceAssignment(BaseModel):
    """Output for assigning the taskforce."""

    n_doctors: int = Field(..., description="Number of doctors assigned.")
    action_details: str = Field(
        ..., description="Additional details of the assignment action."
    )


class MedicalSupplySelection(BaseModel):
    """Output for compiling medical supplies."""

    medical_supplies: List[str] = Field(
        ..., description="List of compiled medical supplies."
    )
    action_details: str = Field(
        ..., description="Details of the medical supplies compilation process."
    )


class HospitalCapacityCheck(BaseModel):
    """Output for checking hospital capacity."""

    hospital_capacities: List[int] = Field(
        ..., description="List of hospital capacities."
    )
    action_details: str = Field(
        ..., description="Details of the hospital capacity check."
    )


class HospitalVoting(BaseModel):
    """Output for hospital voting."""

    hospital_votes: List[int] = Field(..., description="Votes for each hospital.")
    action_details: str = Field(
        ..., description="Details of the hospital voting process."
    )


class VictimVoting(BaseModel):
    """Output for victim voting."""

    victim_hospital_voting_map: dict = Field(
        ..., description="Mapping of victims to hospital votes."
    )
    action_details: str = Field(
        ..., description="Details of the victim voting process."
    )


class AmbulanceSelection(BaseModel):
    """Output for selecting ambulances."""

    ambulances: List[str] = Field(..., description="List of selected ambulances.")
    action_details: str = Field(
        ..., description="Details of the ambulance selection process."
    )


class RoutePlanning(BaseModel):
    """Output for planning the route."""

    routes: List[tuple[str, List[int]]] = Field(
        ..., description="List of planned OSMnx routes for each ambulance."
    )
    action_details: str = Field(
        ..., description="Details of the route planning process."
    )


class MedicalPlanCompilation(BaseModel):
    """Comprehensive output for compiling the final plan."""

    response_plan: str = Field(
        ..., description="Compiled response plan for the medical operation."
    )
    ethical_issues: Optional[str] = Field(
        None, description="Ethical issues considered in the plan."
    )
    action_details: str = Field(
        ..., description="Additional details of the overall medical plan."
    )
