from dotenv import load_dotenv
import requests
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage

load_dotenv()

#tool creation

@tool
def multiply(a:int, b:int)->int:
    """Given two numbers a and b this tool return multiplication result."""
    return a*b


#create llm
llm=ChatOpenAI()

# bind the tool to llm
binded_tools=llm.bind_tools([multiply])

# print(binded_tools)
#
# print(multiply.invoke({'a':5, 'b':10}))
# print(multiply.name)
# print(multiply.description)
# print(multiply.args)

#Calling llm model
# print(binded_tools.invoke('Hi'))  #its return tool_calls values as  tool_calls=[]

query=HumanMessage('multiply number 3 with number 4')
messages=[query]
# print(messages)

result=binded_tools.invoke(messages)
messages.append(result)
# print(result)

#executing the Tools
tool_result=multiply.invoke(result.tool_calls[0])
messages.append(tool_result)

final_result=binded_tools.invoke(messages)
print(final_result.content)





