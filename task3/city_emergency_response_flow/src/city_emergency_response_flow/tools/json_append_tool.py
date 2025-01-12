from typing import Any, Optional, Type

from pydantic import BaseModel, Field

from crewai.tools import BaseTool

import os


class FixedFileReadToolSchema(BaseModel):
    """Input for FileReadTool."""

    pass


class JSONFileReadSchema(FixedFileReadToolSchema):
    """Input for FileReadTool."""

    dir_path: str = Field(
        ..., description="Mandatory directory full path to read the JSON files."
    )


class JSONAppendTool(BaseTool):
    name: str = "Read several JSON files and append them."
    description: str = (
        "A tool that can be used to read several JSON files in a directory and append their contents."
    )
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
            dir_path = self.dir_path
            if os.path.isdir(dir_path):

                json_contents = []
                for filename in os.listdir(dir_path):
                    if filename.endswith(".json"):
                        file_path = os.path.join(dir_path, filename)
                        with open(file_path, "r") as file:
                            json_contents.append(file.read())
                return json_contents

        except Exception as e:
            return f"Fail to read the JSON files in  {dir_path}. Error: {e}"
