from typing import Type
from pydantic import BaseModel,Field
from langchain.tools import BaseTool

"""
BaseTool — when you want to build a custom tool
BaseTool is the base class/interface for creating your own LangChain tool.
It is useful when you need things such as:

Custom _run() implementation
Custom async _arun()
Internal state/configuration
More complex tool behavior
Custom error handling
A reusable tool class
"""
class MultiplyInput(BaseModel):
    a:int = Field(description="The first number to add")
    b:int = Field(description="The second number to add")

class MultiplyTool(BaseTool):
    name:str = "multiply"
    description:str = "Multiply two numbers"

    args_schema: Type[BaseModel] = MultiplyInput

    def _run(self,a:int,b:int)->int:
        return a*b

multiple_tool = MultiplyTool()
result = multiple_tool.invoke({'a':2,'b':3})
print(result)

