from pydantic import BaseModel, Field
from typing import List, Optional


class TaskforceAssignment(BaseModel):
    """Output for assigning the taskforce."""

    n_doctors: int = Field(..., description="Number of doctors assigned.")
    action_details: str = Field(
        ..., description="Additional details of the assignment action."
    )

    @classmethod
    def get_schema(cls) -> str:
        schema = "\n"
        for field_name, field_instance in cls.__fields__.items():
            schema += f"{field_name}, described as: {field_instance.description}\n"
        return schema


class MedicalSupplySelection(BaseModel):
    """Output for compiling medical supplies."""

    medical_supplies: List[str] = Field(
        ..., description="List of compiled medical supplies."
    )
    action_details: str = Field(
        ..., description="Details of the medical supplies compilation process."
    )

    @classmethod
    def get_schema(cls) -> str:
        schema = "\n"
        for field_name, field_instance in cls.__fields__.items():
            schema += f"{field_name}, described as: {field_instance.description}\n"
        return schema


class HospitalCapacityCheck(BaseModel):
    """Output for checking hospital capacity."""

    hospital_capacities: List[int] = Field(
        ..., description="List of hospital capacities."
    )
    action_details: str = Field(
        ..., description="Details of the hospital capacity check."
    )

    @classmethod
    def get_schema(cls) -> str:
        schema = "\n"
        for field_name, field_instance in cls.__fields__.items():
            schema += f"{field_name}, described as: {field_instance.description}\n"
        return schema


class HospitalVoting(BaseModel):
    """Output for hospital voting."""

    hospital_votes: List[int] = Field(..., description="Votes for each hospital.")
    action_details: str = Field(
        ..., description="Details of the hospital voting process."
    )

    @classmethod
    def get_schema(cls) -> str:
        schema = "\n"
        for field_name, field_instance in cls.__fields__.items():
            schema += f"{field_name}, described as: {field_instance.description}\n"
        return schema


class VictimVoting(BaseModel):
    """Output for victim voting."""

    victim_hospital_voting_map: dict = Field(
        ..., description="Mapping of victims to hospital votes."
    )
    action_details: str = Field(
        ..., description="Details of the victim voting process."
    )

    @classmethod
    def get_schema(cls) -> str:
        schema = "\n"
        for field_name, field_instance in cls.__fields__.items():
            schema += f"{field_name}, described as: {field_instance.description}\n"
        return schema


class AmbulanceSelection(BaseModel):
    """Output for selecting ambulances."""

    ambulances: List[str] = Field(..., description="List of selected ambulances.")
    action_details: str = Field(
        ..., description="Details of the ambulance selection process."
    )

    @classmethod
    def get_schema(cls) -> str:
        schema = "\n"
        for field_name, field_instance in cls.__fields__.items():
            schema += f"{field_name}, described as: {field_instance.description}\n"
        return schema


class RoutePlanning(BaseModel):
    """Output for planning the route."""

    routes: List[tuple[str, List[int]]] = Field(
        ..., description="List of planned OSMnx routes for each ambulance."
    )
    action_details: str = Field(
        ..., description="Details of the route planning process."
    )

    @classmethod
    def get_schema(cls) -> str:
        schema = "\n"
        for field_name, field_instance in cls.__fields__.items():
            schema += f"{field_name}, described as: {field_instance.description}\n"
        return schema


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

    @classmethod
    def get_schema(cls) -> str:
        schema = "\n"
        for field_name, field_instance in cls.__fields__.items():
            schema += f"{field_name}, described as: {field_instance.description}\n"
        return schema
