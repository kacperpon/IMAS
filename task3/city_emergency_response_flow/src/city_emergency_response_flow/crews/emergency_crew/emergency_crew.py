import os
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from .schemas.schemas import *


@CrewBase
class EmergencyCrew:
    """EmergencyCrew crew"""

    llm = LLM(model="ollama/llama3.1")
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

    @agent
    def philosopher(self) -> Agent:
        return Agent(
            config=self.agents_config["philosopher"], llm=self.llm, verbose=True
        )

    @task
    def emergency_alert_distribution(self) -> Task:
        return Task(
            config=self.tasks_config["emergency_alert_distribution"],
            output_pydantic=EmergencyAlertDistribution,
            output_file=os.path.join(
                self.output_path, "emergency_alert_distribution.json"
            ),
        )

    @task
    def situation_report_compilation(self) -> Task:
        return Task(
            config=self.tasks_config["situation_report_compilation"],
            output_pydantic=SituationReportCompilation,
            output_file=os.path.join(
                self.output_path, "situation_report_compilation.json"
            ),
        )

    @task
    def ethical_consultation(self) -> Task:
        return Task(
            config=self.tasks_config["ethical_consultation"],
            output_pydantic=FinalCompilation,
            output_file=os.path.join(self.output_path, "ethical_consultation.json"),
        )

    @crew
    def crew(self) -> Crew:
        """Creates the EmergencyCrew crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
