from emergency_mas_planner.tools.custom_tool import MyCustomTool
from crewai_tools import ScrapeWebsiteTool
from crewai import Agent, Task, Process


@agent
def agent_name(self) -> Agent:
    """
    Agent responsible for giving a name to the emergency situation.

    It uses its MyCustomTool to generate a name based on the emergency situation.
    """
    return Agent(
        config=self.agents_config["agent_name"],
        tools=[MyCustomTool(), ScrapeWebsiteTool()],
        llm='ollama/llama3.1',
        vervose=True
    )
    
    
@task
def task_name(self) -> Task:
    return Task(
        config=self.tasks_config["task_name"],
    )
    
@crew
def crew(self) -> Crew:
    return Crew(
        agents=self.agents,
        tasks=self.tasks,
        process=Process.sequential,
        verbose=True,
    )