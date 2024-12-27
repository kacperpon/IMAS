from pydantic import BaseModel, Field
from typing import List, Optional


class CrewInformation(BaseModel):
    crew: str = Field(
        ..., description="Name of the crew (e.g., Firefighting, Medical, Police)"
    )
    information: List[str] = Field(
        ..., description="List of information related to this crew"
    )


class EmergencyAlertDistribution(BaseModel):
    """Output for assessing and distributing emergency alerts."""

    information_for_each_crew: List[CrewInformation] = Field(
        ...,
        description="List of information from the emergency alert for each crew.",
    )
    medical_crew_required: bool = Field(
        ...,
        description="Assessment of the initial report stating whether the medical crew is required or not",
    )
    action_details: str = Field(
        ..., description="Details of the distribution process for emergency alerts."
    )

    @classmethod
    def get_schema(cls) -> str:
        schema = "\n"
        for field_name, field_instance in cls.model_fields.items():
            schema += f"{field_name}, described as: {field_instance.description}\n"
        return schema
