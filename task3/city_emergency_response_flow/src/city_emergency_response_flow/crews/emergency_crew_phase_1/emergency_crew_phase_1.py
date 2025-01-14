import os
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from .schemas.schemas import *

import configparser as ConfigParser


@CrewBase
class EmergencyCrewPhase1:
    """EmergencyCrewPhase1 crew"""

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
            config=self.agents_config["distributor"], llm=self.llm, verbose=True
        )

    @task
    def emergency_alert_distribution(self) -> Task:
        return Task(
            config=self.tasks_config["emergency_alert_distribution"],
            output_pydantic=EmergencyAlertDistribution,
            output_file=os.path.join(
                self.output_path, "001_emergency_alert_distribution.json"
            ),
        )

    @crew
    def crew(self) -> Crew:
        """Creates the EmergencyCrewPhase1 crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
