from pydantic import BaseModel, Field
from typing import List, Optional


class EmergencyAlertDistribution(BaseModel):
    """Output for assessing and distributing emergency alerts."""

    distributed_tasks: List[str] = Field(
        ..., description="List of distributed tasks from the emergency alert."
    )
    action_details: str = Field(
        ..., description="Details of the distribution process for emergency alerts."
    )

    @classmethod
    def get_schema(cls) -> str:
        schema = "\n"
        for field_name, field_instance in cls.__fields__.items():
            schema += f"{field_name}, described as: {field_instance.description}\n"
        return schema


class SituationReportCompilation(BaseModel):
    """Output for compiling the situation report."""

    situation_report: str = Field(..., description="Compiled situation report.")
    ethical_issues: Optional[str] = Field(
        None, description="Ethical issues identified in the situation report."
    )

    @classmethod
    def get_schema(cls) -> str:
        schema = "\n"
        for field_name, field_instance in cls.__fields__.items():
            schema += f"{field_name}, described as: {field_instance.description}\n"
        return schema


class FinalCompilation(BaseModel):
    """Output for ethical consultation and final compilation."""

    situation_report: str = Field(
        ..., description="Finalised situation report after ethical consultation."
    )

    @classmethod
    def get_schema(cls) -> str:
        schema = "\n"
        for field_name, field_instance in cls.__fields__.items():
            schema += f"{field_name}, described as: {field_instance.description}\n"
        return schema
