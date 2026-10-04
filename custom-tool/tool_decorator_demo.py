from langchain_core.tools import tool

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
    print(result)
    print(multiply.name)
    print(multiply.args)
    print(multiply.description)
    print('*'*20)
    print(multiply.args_schema.model_json_schema())

basic_tool_demo()


