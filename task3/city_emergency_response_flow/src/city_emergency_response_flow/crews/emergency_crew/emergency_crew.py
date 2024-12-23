from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task


llm = LLM(model="ollama/llama3.1")


@CrewBase
class EmergencyCrew:
    """EmergencyCrew crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    # @agent
    # def writer(self) -> Agent:
    # 	return Agent(
    # 		config=self.agents_config['writer'],
    # 		llm=llm,
    # 		verbose=True
    # 	)

    # @task
    # def edit(self) -> Task:
    # 	return Task(
    # 		config=self.tasks_config['edit'],
    # 		output_pydantic=ArticleSchema,
    # 		output_file='Article.json'
    # 	)

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
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
