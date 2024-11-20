from crewai_tools import BaseTool

class MyCustomTool(BaseTool):
    name: str = "Name of my tool"
    description: str = (
        "Clear description for what this tool is useful for, your agent will need this information to use it."
    )
    
    def _run(self, arguemnt: str) -> str:
        # Implementation goes here
        return "this is an example of a tool output"