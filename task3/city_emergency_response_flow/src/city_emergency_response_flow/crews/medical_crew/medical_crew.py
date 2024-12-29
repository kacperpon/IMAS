import os
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from .schemas.schemas import *
from crewai_tools import FileReadTool



@CrewBase
class MedicalCrew:
    """MedicalCrew crew"""

    llm = LLM(model="ollama/llama3.1")
    output_path = os.path.join(
        os.path.dirname(os.path.relpath(__file__)), "crew_outputs"
    )
    vehicle_input_path = os.path.join(
            "tests", "vehicle_positions", "ambulances.yaml"
    )
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def medical_personnel_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config["medical_personnel_specialist"],
            llm=self.llm,
            verbose=True,
        )

    @agent
    def equipment_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config["equipment_specialist"],
            llm=self.llm,
            verbose=True,
        )

    @agent
    def hospital_coordinator(self) -> Agent:
        return Agent(
            config=self.agents_config["hospital_coordinator"],
            llm=self.llm,
            verbose=True,
        )

    @agent
    def triage_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config["triage_specialist"],
            llm=self.llm,
            verbose=True,
        )

    @agent
    def ambulance_coordinator(self) -> Agent:
        return Agent(
            config=self.agents_config["ambulance_coordinator"],
            llm=self.llm,
            verbose=True,
        )

    @task
    def medical_taskforce_assignment(self) -> Task:
        return Task(
            config=self.tasks_config["medical_taskforce_assignment"],
            output_pydantic=TaskforceAssignment,
            output_file=os.path.join(
                self.output_path, "001_medical_taskforce_assignment.json"
            ),
        )

    @task
    def medical_supplies_preparation(self) -> Task:
        return Task(
            config=self.tasks_config["medical_supplies_preparation"],
            output_pydantic=MedicalSupplySelection,
            output_file=os.path.join(
                self.output_path, "002_medical_supplies_preparation.json"
            ),
        )

    @task
    def hospital_capacity_check(self) -> Task:  # TODO here human input
        return Task(
            config=self.tasks_config["hospital_capacity_check"],
            output_pydantic=HospitalCapacityCheck,
            output_file=os.path.join(
                self.output_path, "003_hospital_capacity_check.json"
            ),
        )

    @task
    def hospital_voting(self) -> Task:
        return Task(
            config=self.tasks_config["hospital_voting"],
            context=[self.hospital_capacity_check()],
            output_pydantic=HospitalVoting,
            output_file=os.path.join(self.output_path, "004_hospital_voting.json"),
        )

    @task
    def injury_voting(self) -> Task:
        return Task(
            config=self.tasks_config["injury_voting"],
            output_pydantic=InjuryVoting,
            output_file=os.path.join(self.output_path, "005_injury_voting.json"),
        )

    @task
    def ambulance_selection(self) -> Task:
        return Task(
            config=self.tasks_config["ambulance_selection"],
            context=[self.medical_supplies_preparation()],
            tools=[FileReadTool(file_path=self.vehicle_input_path)],
            output_pydantic=AmbulanceSelection,
            output_file=os.path.join(self.output_path, "006_ambulance_selection.json"),
        )

    @task
    def ambulance_route_planning(self) -> Task:
        return Task(
            config=self.tasks_config["ambulance_route_planning"],
            context=[self.ambulance_selection()],
            output_pydantic=RoutePlanning,
            output_file=os.path.join(
                self.output_path, "007_ambulance_route_planning.json"
            ),
        )

    @task
    def medical_final_plan_compilation(self) -> Task:
        return Task(
            config=self.tasks_config["medical_final_plan_compilation"],
            context=[
                self.medical_taskforce_assignment(),
                self.medical_supplies_preparation(),
                self.hospital_capacity_check(),
                self.hospital_voting(),
                self.injury_voting(),
                self.ambulance_selection(),
                self.ambulance_route_planning(),
            ],
            output_pydantic=MedicalPlanCompilation,
            output_file=os.path.join(
                self.output_path, "008_medical_final_plan_compilation.json"
            ),
        )

    @crew
    def crew(self) -> Crew:
        """Creates the MedicalCrew crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
