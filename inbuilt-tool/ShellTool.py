from langchain_community.tools import ShellTool

try:
    tool=ShellTool()
    input=input('Enter the command:')
    result=tool.invoke(input)
    print(result)
except Exception as e:
    print(f"Error due to",str(e))