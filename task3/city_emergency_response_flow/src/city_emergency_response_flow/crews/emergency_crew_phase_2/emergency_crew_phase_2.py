import os
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import FileReadTool
from .schemas.schemas import *

import configparser as ConfigParser


@CrewBase
class EmergencyCrewPhase2:
    """EmergencyCrewPhase2 crew"""

    config = ConfigParser.RawConfigParser()
    config.read(
        os.path.join(
            os.getcwd(), "src/city_emergency_response_flow/config/config.properties"
        )
    )

    llm = LLM(model=config.get("LLM", "model"), base_url=config.get("LLM", "base_url"))
    output_path = os.path.join(
        os.path.dirname(os.path.relpath(__file__)), "crew_outputs"
    )
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def distributor(self) -> Agent:
        return Agent(
            config=self.agents_config["plan_compiler"], llm=self.llm, verbose=True
        )

    @agent
    def philosopher(self) -> Agent:
        return Agent(
            config=self.agents_config["philosopher"], llm=self.llm, verbose=True
        )

    @task
    def situation_report_compilation(self) -> Task:
        return Task(
            config=self.tasks_config["situation_report_compilation"],
            output_pydantic=SituationReportCompilation,
            tools=[FileReadTool()],
            output_file=os.path.join(
                self.output_path, "001_situation_report_compilation.json"
            ),
        )

    @task
    def ethical_consultation(self) -> Task:
        return Task(
            config=self.tasks_config["ethical_consultation"],
            context=[
                self.situation_report_compilation(),
            ],
            output_pydantic=FinalCompilation,
            tools=[
                FileReadTool(
                    file_path="src/city_emergency_response_flow/crews/emergency_crew_phase_2/ethics.txt"
                )
            ],
            output_file=os.path.join(self.output_path, "002_ethical_consultation.json"),
        )

    @crew
    def crew(self) -> Crew:
        """Creates the EmergencyCrewPhase2 crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
