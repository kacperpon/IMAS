import os
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from .schemas.schemas import *


@CrewBase
class EmergencyCrewPhase1:
    """EmergencyCrewPhase1 crew"""

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

    @task
    def emergency_alert_distribution(self) -> Task:
        return Task(
            config=self.tasks_config["emergency_alert_distribution"],
            output_pydantic=EmergencyAlertDistribution,
            output_file=os.path.join(
                self.output_path, "emergency_alert_distribution.json"
            ),
        )

    @crew
    def crew(self) -> Crew:
        """Creates the EmergencyCrewPhase1 crew"""

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
