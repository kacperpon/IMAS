#!/usr/bin/env python
from random import randint

from pydantic import BaseModel

from crewai.flow.flow import Flow, listen, start, router, or_

from .crews.emergency_crew.emergency_crew import EmergencyCrew
from .crews.firefighting_crew.firefighting_crew import FirefightingCrew
from .crews.medical_crew.medical_crew import MedicalCrew
from .crews.police_crew.police_crew import PoliceCrew


# # TODO probably not necessary since first emergency crew agent extracts information from the markdown file
# class InitialInformation(BaseModel):
# fire_type: str
# fire_location: tuple[str, str]
# fire_severity: str
# injured_people: int


class InitialInformation(BaseModel):
    initial_emergency_report: str = ""
    final_report: str = ""
    medical_crew_required: bool = True
    firefighting_information: str = ""
    medical_information: str = ""
    police_information: str = ""


# class PoemState(BaseModel):
#     sentence_count: int = 1
#     poem: str = ""


class CityEmergencyResponseFlow(Flow[InitialInformation]):
    # 1. Input initial information to the emergency
    # 2. Kickoff emergency crew; input is initial information
    # 3. Kickoff fire, medical, police crew; input is output of emergency crew
    # 4. Feed outputs of those three crews back to emergency crew
    # 5. Emergency crew outputs the final plan in the end

    @start()
    def read_emergency_characteristics(self):
        print("Reading emergency characteristics")
        self.state.initial_emergency_report = open("initial_report.md").read()

    @listen(read_emergency_characteristics)
    def call_emergency_centre(self):
        print("Handling the reported emergency")

        emergency_crew = EmergencyCrew().crew()


        result = (
            EmergencyCrew()
            .crew()
            .kickoff(
                inputs={"initial_emergency_report": self.state.initial_emergency_report}
            )
        )

        # TODO
        print("Results for now", result.raw)
        self.state.final_report = result.raw

    # @listen(read_emergency_characteristics)
    # def call_emergency_centre(self):
    #     print("Handling the reported emergency")
    #     result = (
    #         EmergencyCrew()
    #         .crew()
    #         .kickoff(
    #             inputs={"initial_emergency_report": self.state.initial_emergency_report}
    #         )
    #     )

    #     # TODO
    #     print("Results for now", result.raw)
    #     self.state.final_report = result.raw

    @router(call_emergency_centre)
    def medical_crew_required(self):
        if self.state.medical_crew_required:
            return "meds_required"
        else:
            return "meds_not_required"

    @listen(or_("meds_required", "meds_not_required"))
    def create_fire_plan(self):
        print("Develop a plan for the firefighting crew")
        result = (
            FirefightingCrew()
            .crew()
            .kickoff(
                inputs={"firefighting_information": self.state.firefighting_information}
            )
        )

    @listen("meds_required")  # only when explicitly required
    def create_medical_plan(self):
        print("Develop a plan for the medical crew")
        result = (
            MedicalCrew()
            .crew()
            .kickoff(inputs={"medical_information": self.state.medical_information})
        )

    @listen(or_("meds_required", "meds_not_required"))
    def create_police_plan(self):
        print("Develop a plan for the police crew")
        result = (
            PoliceCrew()
            .crew()
            .kickoff(inputs={"police_information": self.state.police_information})
        )


def kickoff():
    city_emergency_response_flow = CityEmergencyResponseFlow()
    city_emergency_response_flow.kickoff()


def plot():
    city_emergency_response_flow = CityEmergencyResponseFlow()
    city_emergency_response_flow.plot()


if __name__ == "__main__":
    kickoff()
