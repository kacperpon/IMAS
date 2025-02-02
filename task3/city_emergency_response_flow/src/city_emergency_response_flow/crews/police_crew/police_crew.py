import os
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from .schemas.schemas import *
from crewai_tools import FileReadTool
from ...tools.emergency_route_tool import EmergencyRouteTool
from ...tools.json_append_tool import JSONAppendTool
import configparser as ConfigParser


@CrewBase
class PoliceCrew:
    """PoliceCrew crew"""

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

    vehicle_input_path = os.path.join(
        "tests", "vehicle_positions", "police_vehicles.yaml"
    )
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def receiver_and_personnel_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config["receiver_and_personnel_specialist"],
            llm=self.llm,
            verbose=True,
        )

    @agent
    def traffic_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config["traffic_specialist"],
            llm=self.llm,
            verbose=True,
        )

    @agent
    def dispatch_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config["dispatch_specialist"],
            llm=self.llm,
            verbose=True,
        )

    @task
    def police_taskforce_assignment(self) -> Task:
        return Task(
            config=self.tasks_config["police_taskforce_assignment"],
            output_pydantic=TaskforceAssignment,
            output_file=os.path.join(
                self.output_path, "001_police_taskforce_assignment.json"
            ),
        )

    @task
    def perimeter_control_planning(self) -> Task:
        return Task(
            config=self.tasks_config["perimeter_control_planning"],
            output_pydantic=PerimeterControlPlanning,
            output_file=os.path.join(
                self.output_path, "002_perimeter_control_planning.json"
            ),
        )

    @task
    def patrol_vehicle_assignment(self) -> Task:
        return Task(
            config=self.tasks_config["patrol_vehicle_assignment"],
            tools=[FileReadTool(file_path=self.vehicle_input_path)],
            output_pydantic=PatrolSelection,
            output_file=os.path.join(
                self.output_path, "003_patrol_vehicle_assignment.json"
            ),
        )

    @task
    def patrol_route_planning(self) -> Task:
        return Task(
            config=self.tasks_config["patrol_route_planning"],
            context=[self.patrol_vehicle_assignment()],
            tools=[EmergencyRouteTool(result_as_answer=True)],
            output_pydantic=RoutePlanning,
            output_file=os.path.join(
                self.output_path, "004_patrol_route_planning.json"
            ),
        )

    @task
    def police_final_plan_compilation(self) -> Task:
        return Task(
            config=self.tasks_config["police_final_plan_compilation"],
            tools=[JSONAppendTool(dir_path=self.output_path)],
            output_file=os.path.join(self.output_path, "008_final_plan_compilation.md"),
        )

    @crew
    def crew(self) -> Crew:
        """Creates the PoliceCrew crew"""

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
