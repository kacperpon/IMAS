import os
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import FileReadTool

from .schemas.schemas import *
from ...tools.emergency_route_tool import EmergencyRouteTool
from ...tools.json_append_tool import JSONAppendTool

import configparser as ConfigParser


@CrewBase
class FirefightingCrew:
    """FirefightingCrew crew"""

    config = ConfigParser.RawConfigParser()
    config.read(
        os.path.join(
            os.getcwd(), "src/city_emergency_response_flow/config/config.properties"
        )
    )

    llm = LLM(
        model=config.get("LLM", "model"),
        base_url=config.get("LLM", "base_url"),
        max_tokens=4096,
    )
    output_path = os.path.join(
        os.path.dirname(os.path.relpath(__file__)), "crew_outputs"
    )

    # Create the output directory if it does not exist, clean it if it exists
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    else:
        for file in os.listdir(output_path):
            os.remove(os.path.join(output_path, file))

    vehicle_input_path = os.path.join("tests", "vehicle_positions", "firetrucks.yaml")
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
            output_file=os.path.join(self.output_path, "001_taskforce_assignment.json"),
        )

    @task
    def extinguishing_tools_selection(self) -> Task:
        return Task(
            config=self.tasks_config["extinguishing_tools_selection"],
            output_pydantic=ExtinguishingToolSelection,
            output_file=os.path.join(
                self.output_path, "002_extinguishing_tools_selection.json"
            ),
        )

    @task
    def building_structure_assessment(self) -> Task:
        return Task(
            config=self.tasks_config["building_structure_assessment"],
            output_pydantic=AssessBuildingStructurePlanning,
            output_file=os.path.join(
                self.output_path, "003_building_structure_assessment.json"
            ),
        )

    @task
    def victim_rescue_planning(self) -> Task:
        return Task(
            config=self.tasks_config["victim_rescue_planning"],
            output_pydantic=VictimRescuePlanning,
            output_file=os.path.join(
                self.output_path, "004_victim_rescue_planning.json"
            ),
        )

    @task
    def tool_selection(self) -> Task:
        return Task(
            config=self.tasks_config["tool_selection"],
            context=[self.building_structure_assessment()],
            output_pydantic=ToolSelection,
            output_file=os.path.join(self.output_path, "005_tool_selection.json"),
        )

    @task
    def fire_truck_selection(self) -> Task:
        return Task(
            config=self.tasks_config["fire_truck_selection"],
            context=[self.extinguishing_tools_selection()],
            tools=[FileReadTool(file_path=self.vehicle_input_path)],
            output_pydantic=FireTruckSelection,
            output_file=os.path.join(self.output_path, "006_fire_truck_selection.json"),
        )

    @task
    def route_planning(self) -> Task:
        return Task(
            config=self.tasks_config["route_planning"],
            context=[self.fire_truck_selection()],
            tools=[EmergencyRouteTool(result_as_answer=True)],
            output_pydantic=RoutePlanning,
            output_file=os.path.join(self.output_path, "007_route_planning.json"),
        )

    @task
    def final_plan_compilation(self) -> Task:
        return Task(
            config=self.tasks_config["final_plan_compilation"],
            tools=[JSONAppendTool(dir_path=self.output_path)],
            output_file=os.path.join(self.output_path, "008_final_plan_compilation.md"),
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
