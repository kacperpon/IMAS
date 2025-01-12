from typing import Any, Optional, Type

from pydantic import BaseModel, Field

from crewai.tools import BaseTool

import os, json


class FixedFileReadToolSchema(BaseModel):
    """Input for FileReadTool."""

    pass


class JSONFileReadSchema(FixedFileReadToolSchema):
    """Input for FileReadTool."""

    dir_path: str = Field(..., description="Mandatory directory full path to read the JSON files.")


class PlanCompilation(BaseModel):
    """Comprehensive output for compiling the final plan."""

    response_plan: str = Field(
        ...,
        description="Summarized response plan including all outputs from before tasks for a crews operation.",
    )
    ethical_issues: Optional[str] = Field(
        None, description="Ethical issues considered in the plan."
    )
    

    @classmethod
    def get_schema(cls) -> str:
        schema = "\n"
        for field_name, field_instance in cls.model_fields.items():
            schema += f"{field_name}, described as: {field_instance.description}\n"
        return schema



class JSONAppendTool(BaseTool):
    name: str = "Read several JSON files and append them."
    description: str = "A tool that can be used to read several JSON files in a directory and append their contents."
    args_schema: Type[BaseModel] = JSONFileReadSchema
    dir_path: Optional[str] = None

    def __init__(self, dir_path: Optional[str] = None, **kwargs):
        super().__init__(**kwargs)
        if dir_path is not None:
            self.dir_path = dir_path
            self.description = f"A tool that can be used to read JSON files in {dir_path} and append their content."
            self.args_schema = FixedFileReadToolSchema
            self._generate_description()

    def _run(
        self,
        **kwargs: Any,
    ) -> Any:
        try:
            dir_path = kwargs.get("dir_path", self.dir_path)
            if dir_path is None:
                return "No directory path provided."
            if os.path.isdir(dir_path):
                
                json_contents = ""
                for filename in os.listdir(dir_path):
                    if filename.endswith(".json"):
                        file_path = os.path.join(dir_path, filename)
                        with open(file_path, "r") as file:
                            f = file.read()
                            json_data = json.loads(f)
                            if "action_details" in json_data:
                                json_contents += json_data["action_details"] + "\n"
                
                plan_compilation = PlanCompilation(response_plan=json_contents)
                return plan_compilation.model_dump_json()
            
        except Exception as e:
            return f"Fail to read the JSON files in  {dir_path}. Error: {e}"
