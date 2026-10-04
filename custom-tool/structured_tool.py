from langchain_core.tools import StructuredTool
from pydantic import BaseModel,Field

"""
StructuredTool — when you already have a function
StructuredTool is a ready-made tool implementation that lets you turn a normal Python function into a LangChain tool.


"""
class StructuredToolDemo(BaseModel):
    a:int=Field(description="The first number to add")
    b:int=Field(description="The second number to add")

def multiply_funcs(a: int,b:int) -> int:
    return a * b

multiple_tools=StructuredTool.from_function(
    func=multiply_funcs,
    name="multiply",
    description="Multiply two numbers",
    args_schema=StructuredToolDemo
)
result=multiple_tools.invoke({"a":9,"b":3})
print(result)
print(multiple_tools.name)
print(multiple_tools.description)

