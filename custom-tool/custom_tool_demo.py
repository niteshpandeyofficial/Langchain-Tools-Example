from langchain_core.tools import tool
from langchain_core.tools import StructuredTool
from pydantic import BaseModel,Field

def basic_tool_demo():
    """
    Steps to create the custom tools
    Step1: Create a specific function with docs string
    Step2: Declared the function with Type hinting
    Step3: Add @tool decorator to written function
    """
    @tool
    def multiply(a: int, b: int) -> int:
        """
        Multiply two numbers
        """
        return a * b

    result=multiply.invoke({"a":2,"b":3})
    print(multiply.name)
    print(multiply.args)
    print(multiply.description)
    print('*'*20)
    print(multiply.args_schema.model_json_schema())

class StructuredToolDemo(BaseModel):
    a : int = Field(description="The first number to add")
    b : int = Field(description="The second number to add")

def multiply_funcs(a: int, b: int) -> int:
    return a * b

multiple_tool=StructuredTool.from_function(
    func=multiply_funcs,
    name="Multiply",
    description="Multiple the number",
    args_schema=StructuredToolDemo
)

result=multiple_tool.invoke({"a":8,"b":3})
print(result)
print(multiple_tool.name)
print(multiple_tool.description)


