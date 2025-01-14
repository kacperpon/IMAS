from pydantic import BaseModel, Field
from typing import List, Optional, Tuple


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
    available_bed_capacity: int = Field(..., description="Number of available beds in that hospital")
    hospital_location: Tuple[float, float] = Field(..., description="Location of the hospital (latitude, longitude)")
    specializations: List[str] = Field(..., description="List of specializations of the hospital")


class HospitalCapacityCheck(BaseModel):
    """Output for checking hospital capacity."""

    hospitals: List[HospitalInformation] = Field(..., description="List of hospitals.")

    @classmethod
    def get_schema(cls) -> str:
        schema = "\n"
        for field_name, field_instance in cls.model_fields.items():
            schema += f"{field_name}, described as: {field_instance.description}\n"
        return schema


class VotesPerHospital(BaseModel):
    hospital_name: str = Field(
        ..., description="Official name of the hospital"
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


class VictimToHospitalVotes(BaseModel):
    victim_id: int = Field(..., description="Unique identifier for the victim")
    hospital_votes: List[VotesPerHospital] = Field(..., description="Votes for each hospital for the victim")


class InjuryVoting(BaseModel):
    """Output for victim-injury voting."""

    victim_hospital_mappings: List[VictimToHospitalVotes] = Field(
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


# For AmbulanceSelection
class AmbulanceInformation(BaseModel):
    ambulance_id: int = Field(
        ..., description="ambulance_id of the selected ambulance. (Eg: 1)"
    )
    installed_supplies: List[str] = Field(
        ..., description="List of medical supplies which will be installed in the selected ambulance."
    )
    ambulance_location: Tuple[float, float] = Field(
        ..., description="ambulance_location (composed of latitude and longitude values) of the selected ambulance location."
    )
    ambulance_status: str = Field(
        ..., description="ambulance_status of the selected truck (Eg: Available, In Service)"
    )


class AmbulanceSelection(BaseModel):
    """Output for selecting ambulances."""

    ambulances: List[AmbulanceInformation] = Field(..., description="List of selected ambulances.")
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
    
    route_duration_min: List[float] = Field(
        ..., description="The duration in minutes of the route."
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

class VictimToHospitalMap(BaseModel):
    """Mapping between the victim and the hospital it must be sent to."""

    victim_id: int = Field(..., description="Unique identifier for the victim")
    hospital_name: str = Field(..., description="Official name of the hospital")
    total_votse: int = Field(..., description="Total votes for the winning hospital")


class VoteCompilation(BaseModel):
    """Voting results, mapping between the victim and the hospital it must be sent to."""

    
    victim_hospital_mappings: List[VictimToHospitalMap] = Field(
        ..., description="List of mappings between victims and hospitals."
    )
    action_details: str = Field(
        ..., description="Details of the vote compilation process."
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
        None, description="Ethical issues (if any) considered in the plan."
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
