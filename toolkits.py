from langchain_core.tools import tool

"""
In LangChain, a Toolkit is simply a collection of related tools that are packaged together so an agent can use them.

Toolkit
 ↓
Collection of multiple related tools

                    Toolkit
                       │
          ┌────────────┼────────────┐
          ↓            ↓            ↓
     Search Tool   Calculator   Weather Tool

"""

@tool
def add(a: int, b: int) -> int:
    """Addition of two numbers"""
    return a + b

@tool
def multiply(a: int, b: int) -> int:
    """Multiplication of two numbers"""
    return a * b

class Mathtoolkit():
    def get_tools(self):
        return [add, multiply]

toolkit=Mathtoolkit()
tools=toolkit.get_tools()

for tool in tools:
    print(tool.name,"=>", tool.description)
    print(tool.invoke({'a':3, 'b':4}))