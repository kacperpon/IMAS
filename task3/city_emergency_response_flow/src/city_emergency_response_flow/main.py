#!/usr/bin/env python
from random import randint

from pydantic import BaseModel

from crewai.flow.flow import Flow, listen, start

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
        print(self.state.initial_emergency_report)

    # @listen(read_emergency_characteristics)
    # def start_emergency_pipeline(self):
    #     print("Handling the reported emergency")
    #     result = (
    #         EmergencyCrew()
    #         .crew()
    #         .kickoff(inputs={"sentence_count": self.state.sentence_count})
    #     )

    #     print("Poem generated", result.raw)
    #     self.state.poem = result.raw

    # @listen(start_emergency_pipeline)
    # def save_poem(self):
    #     print("Saving poem")
    #     with open("poem.txt", "w") as f:
    #         f.write(self.state.poem)


def kickoff():
    city_emergency_response_flow = CityEmergencyResponseFlow()
    city_emergency_response_flow.kickoff()


def plot():
    city_emergency_response_flow = CityEmergencyResponseFlow()
    city_emergency_response_flow.plot()


if __name__ == "__main__":
    kickoff()
