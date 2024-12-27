import os
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from .schemas.schemas import *


@CrewBase
class EmergencyCrewPhase2:
    """EmergencyCrewPhase2 crew"""

    llm = LLM(model="ollama/llama3.1")
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
    def situation_report_compilation(self) -> Task:
        return Task(
            config=self.tasks_config["situation_report_compilation"],
            output_pydantic=SituationReportCompilation,
            output_file=os.path.join(
                self.output_path, "001_situation_report_compilation.json"
            ),
        )

    @task
    def ethical_consultation(self) -> Task:
        return Task(
            config=self.tasks_config["ethical_consultation"],
            output_pydantic=FinalCompilation,
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
