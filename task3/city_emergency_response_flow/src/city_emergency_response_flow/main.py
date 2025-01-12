#!/usr/bin/env python
from random import choice, randint
import os

from pydantic import BaseModel

from crewai.flow.flow import Flow, listen, start, router, or_, and_

# from .crews.emergency_crew_phase_1.emergency_crew_phase_1 import EmergencyCrewPhase1
from .crews.emergency_crew_phase_2.emergency_crew_phase_2 import EmergencyCrewPhase2
# from .crews.firefighting_crew.firefighting_crew import FirefightingCrew
# from .crews.medical_crew.medical_crew import MedicalCrew
# from .crews.police_crew.police_crew import PoliceCrew




class InitialInformation(BaseModel):
    initial_emergency_report: str = ""

    firefighting_vehicles: str = ""

    final_report: str = ""
    medical_crew_required: bool = True

    firefighting_information: str = ""
    medical_information: str = ""
    police_information: str = ""

    firefighting_plan: str = ""
    medical_plan: str = ""
    police_plan: str = ""


class CityEmergencyResponseFlow(Flow[InitialInformation]):
    # 1. Input initial information to the emergency
    # 2. Kickoff emergency crew; input is initial information
    # 3. Kickoff fire, medical, police crew; input is output of emergency crew
    # 4. Feed outputs of those three crews back to emergency crew
    # 5. Emergency crew outputs the final plan in the end

    # @start()
    # def read_emergency_characteristics(self):
    #     print("Reading emergency characteristics")

    #     # selected_file = os.path.join(
    #     #     "tests", "initial_reports", choice(os.listdir("tests/initial_reports"))
    #     # )
        
    #     selected_file = os.path.join(
    #         "tests", "initial_reports", "initial_report_03.md"
    #     )

    #     self.state.initial_emergency_report = open(selected_file).read()

    # @listen(read_emergency_characteristics)
    # def call_emergency_centre(self):
    #     print("Handling the reported emergency")
    #     result = (
    #         EmergencyCrewPhase1()
    #         .crew()
    #         .kickoff(
    #             inputs={"initial_emergency_report": self.state.initial_emergency_report}
    #         )
    #     )

    #     # Access and assign information for each crew
    #     for crew_info in result.pydantic.information_for_each_crew:
    #         if crew_info.crew == "Firefighting":
    #             self.state.firefighting_information = "\n".join(crew_info.information)
    #         elif crew_info.crew == "Medical":
    #             self.state.medical_information = "\n".join(crew_info.information)
    #         elif crew_info.crew == "Police":
    #             self.state.police_information = "\n".join(crew_info.information)

    #     # # Print the assigned variables
    #     # print(f"Firefighting Information: {self.state.firefighting_information}")
    #     # print(f"Medical Information: {self.state.medical_information}")
    #     # print(f"Police Information: {self.state.police_information}")

    #     self.state.medical_crew_required = result.pydantic.medical_crew_required

    # @router(call_emergency_centre)
    # def medical_crew_required(self):
    #     if self.state.medical_crew_required:
    #         return "meds_required"
    #     else:
    #         medical_plan_path = os.path.join(os.getcwd(), "src", "city_emergency_response_flow", "crews", "medical_crew", "crew_outputs/")
    #         for filename in os.listdir(medical_plan_path):
    #             file_path = os.path.join(medical_plan_path, filename)
    #             if os.path.isfile(file_path):
    #                 os.remove(file_path)
            
    #         return "meds_not_required"

    # #####################
    # # FIREFIGHTING CREW #
    # #####################

    # @listen(or_("meds_required", "meds_not_required"))
    # def create_fire_plan(self):
    #     print("Develop a plan for the firefighting crew")
    #     result = (
    #         FirefightingCrew()
    #         .crew()
    #         .kickoff(
    #             inputs={"firefighting_information": self.state.firefighting_information}
    #         )
    #     )

    # ################
    # # MEDICAL CREW #
    # ################

    # @listen("meds_required")  # only when explicitly required
    # def create_medical_plan(self):
    #     print("Develop a plan for the medical crew")
    #     result = (
    #         MedicalCrew()
    #         .crew()
    #         .kickoff(
    #             inputs={"medical_information": self.state.medical_information}
    #         )
    #     )

    
    # ###############
    # # POLICE CREW #
    # ###############

    # @listen(or_("meds_required", "meds_not_required"))
    # def create_police_plan(self):
    #     print("Develop a plan for the police crew")
    #     result = (
    #         PoliceCrew()
    #         .crew()
    #         .kickoff(inputs={"police_information": self.state.police_information})
    #     )



    # @listen(
    #     (
    #         and_(
    #             create_fire_plan,   
    #             create_police_plan,
    #         )
    #     )
    # )
    @start()
    def merge_plans(self):
        print("Merge each crew's plans into one final plan")
        
        
        firefighting_plan_path = os.path.join(os.getcwd(), "src", "city_emergency_response_flow", "crews", "firefighting_crew", "crew_outputs", "008_final_plan_compilation.md")
        medical_plan_path = os.path.join(os.getcwd(), "src", "city_emergency_response_flow", "crews", "medical_crew", "crew_outputs", "008_final_plan_compilation.md")
        police_plan_path = os.path.join(os.getcwd(), "src", "city_emergency_response_flow", "crews", "police_crew", "crew_outputs", "008_final_plan_compilation.md")
        
        # Read and concatenate the contents of three markdown files
        files_to_merge = [firefighting_plan_path, medical_plan_path, police_plan_path]
        merged_content = ""

        for file_name in files_to_merge:
            if os.path.exists(file_name):
                with open(file_name, "r") as file:
                    merged_content += file.read() + "\n"

        # Save the concatenated content into final_report.md
        with open("final_report.md", "w") as final_file:
            final_file.write(merged_content)
        
        
        result = (
            EmergencyCrewPhase2()
            .crew()
            .kickoff()
        )

     


def kickoff():
    city_emergency_response_flow = CityEmergencyResponseFlow()
    city_emergency_response_flow.kickoff()


def plot():
    city_emergency_response_flow = CityEmergencyResponseFlow()
    city_emergency_response_flow.plot()


if __name__ == "__main__":
    kickoff()
