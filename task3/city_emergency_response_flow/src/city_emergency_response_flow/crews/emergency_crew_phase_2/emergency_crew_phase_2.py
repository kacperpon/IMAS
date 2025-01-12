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

    llm = LLM(model=config.get("LLM", "model"), base_url=config.get("LLM", "base_url"), max_tokens=4096)
    output_path = os.path.join(
        os.path.dirname(os.path.relpath(__file__)), "crew_outputs"
    )
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def philosopher(self) -> Agent:
        return Agent(
            config=self.agents_config["philosopher"], llm=self.llm, verbose=True
        )

    @task
    def ethical_consultation(self) -> Task:
        return Task(
            config=self.tasks_config["ethical_consultation"],
            # tools=[
            #     # FileReadTool(
            #     #     file_path=os.path.join(os.getcwd(), "final_report.md")
            #     # ),
            #     FileReadTool(
            #         file_path=os.path.join(os.path.relpath(__file__), "ethics.txt")
            #     )
            # ],
            output_file=os.path.join(self.output_path, "001_ethical_report.md"),
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
