import os
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from .schemas.schemas import *


@CrewBase
class FirefightingCrew:
    """FirefightingCrew crew"""

    llm = LLM(model="ollama/llama3.1")
    output_path = os.path.join(
        os.path.dirname(os.path.relpath(__file__)), "crew_outputs"
    )
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def fire_personnel_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config["fire_personnel_specialist"],
            llm=self.llm,
            verbose=True,
        )

    @agent
    def fire_type_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config["fire_type_specialist"],
            llm=self.llm,
            verbose=True,
        )

    @agent
    def building_structure_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config["building_structure_specialist"],
            llm=self.llm,
            verbose=True,
        )

    @agent
    def rescue_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config["rescue_specialist"],
            llm=self.llm,
            verbose=True,
        )

    @agent
    def fire_truck_chief(self) -> Agent:
        return Agent(
            config=self.agents_config["fire_truck_chief"],
            llm=self.llm,
            verbose=True,
        )

    @agent
    def tool_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config["tool_specialist"],
            llm=self.llm,
            verbose=True,
        )

    @task
    def taskforce_assignment(self) -> Task:
        return Task(
            config=self.tasks_config["taskforce_assignment"],
            output_pydantic=TaskforceAssignment,
            output_file=os.path.join(self.output_path, "taskforce_assignment.json"),
        )

    @task
    def extinguishing_tools_selection(self) -> Task:
        return Task(
            config=self.tasks_config["extinguishing_tools_selection"],
            output_pydantic=ExtinguishingToolSelection,
            output_file=os.path.join(
                self.output_path, "extinguishing_tools_selection.json"
            ),
        )

    @task
    def building_structure_assessment(self) -> Task:
        return Task(
            config=self.tasks_config["building_structure_assessment"],
            output_pydantic=AssessBuildingStructurePlanning,
            output_file=os.path.join(
                self.output_path, "building_structure_assessment.json"
            ),
        )

    @task
    def victim_rescue_planning(self) -> Task:
        return Task(
            config=self.tasks_config["victim_rescue_planning"],
            output_pydantic=VictimRescuePlanning,
            output_file=os.path.join(self.output_path, "victim_rescue_planning.json"),
        )

    @task
    def tool_selection(self) -> Task:
        return Task(
            config=self.tasks_config["tool_selection"],
            context=[self.building_structure_assessment()],
            output_pydantic=ToolSelection,
            output_file=os.path.join(self.output_path, "tool_selection.json"),
        )

    @task
    def fire_truck_selection(self) -> Task:
        return Task(
            config=self.tasks_config["fire_truck_selection"],
            context=[self.extinguishing_tools_selection()],
            output_pydantic=FireTruckSelection,
            output_file=os.path.join(self.output_path, "fire_truck_selection.json"),
        )

    @task
    def route_planning(self) -> Task:
        return Task(
            config=self.tasks_config["route_planning"],
            context=[self.fire_truck_selection()],
            output_pydantic=RoutePlanning,
            output_file=os.path.join(self.output_path, "route_planning.json"),
        )

    @task
    def final_plan_compilation(self) -> Task:
        return Task(
            config=self.tasks_config["final_plan_compilation"],
            context=[
                self.taskforce_assignment(),
                self.extinguishing_tools_selection(),
                self.building_structure_assessment(),
                self.victim_rescue_planning(),
                self.tool_selection(),
                self.fire_truck_selection(),
                self.route_planning(),
            ],
            output_pydantic=FirePlanCompilation,
            output_file=os.path.join(self.output_path, "final_plan_compilation.json"),
        )

    @crew
    def crew(self) -> Crew:
        """Creates the EmergencyCrew crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
