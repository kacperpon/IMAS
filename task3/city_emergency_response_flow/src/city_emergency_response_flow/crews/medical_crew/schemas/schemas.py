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
        for field_name, field_instance in cls.model_fields.items():
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
        for field_name, field_instance in cls.model_fields.items():
            schema += f"{field_name}, described as: {field_instance.description}\n"
        return schema


class HospitalInformation(BaseModel):
    hospital_name: str = Field(..., description="Official name of the hospital")
    hospital_id: int = Field(
        ..., description="Integer index to effectively refer to a nearby hospital"
    )
    capacity: int = Field(..., description="Number of available beds in that hospital")


class HospitalCapacityCheck(BaseModel):
    """Output for checking hospital capacity."""

    hospitals: List[HospitalInformation] = Field(..., description="List of hospitals.")
    action_details: str = Field(
        ...,
        description="Details of the nearby hospitals including each's capacity check.",
    )

    @classmethod
    def get_schema(cls) -> str:
        schema = "\n"
        for field_name, field_instance in cls.model_fields.items():
            schema += f"{field_name}, described as: {field_instance.description}\n"
        return schema


class VotesPerHospital(BaseModel):
    hospital_id: int = Field(
        ..., description="Integer index to effectively refer to a nearby hospital"
    )
    vote_count: int = Field(
        ..., description="Integer number including the votes for that hospital"
    )


class HospitalVoting(BaseModel):
    """Output for hospital voting."""

    hospital_votes: List[VotesPerHospital] = Field(
        ..., description="Votes for each hospital."
    )
    action_details: str = Field(
        ..., description="Details of the hospital voting process."
    )

    @classmethod
    def get_schema(cls) -> str:
        schema = "\n"
        for field_name, field_instance in cls.model_fields.items():
            schema += f"{field_name}, described as: {field_instance.description}\n"
        return schema


class VictimToHospitalMap(BaseModel):
    victim_id: int = Field(..., description="Unique identifier for the victim")
    hospital_id: int = Field(..., description="ID of the hospital mapped to the victim")
    priority_score: float = Field(
        ..., description="Priority score for the victim-hospital mapping"
    )


class InjuryVoting(BaseModel):
    """Output for victim-injury voting."""

    victim_hospital_mappings: List[VictimToHospitalMap] = Field(
        ..., description="List of mappings between victims and hospitals."
    )
    action_details: str = Field(
        ..., description="Details of the victim voting process."
    )

    @classmethod
    def get_schema(cls) -> str:
        schema = "\n"
        for field_name, field_instance in cls.model_fields.items():
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
        for field_name, field_instance in cls.model_fields.items():
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
        for field_name, field_instance in cls.model_fields.items():
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
        for field_name, field_instance in cls.model_fields.items():
            schema += f"{field_name}, described as: {field_instance.description}\n"
        return schema
