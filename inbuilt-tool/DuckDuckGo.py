from langchain_community.tools import DuckDuckGoSearchRun
from ddgs import DDGS

"""
ddgs is useful because it can act as a web-search tool 
that your LangChain application can call when it needs current information.

The current ddgs package is called Dux Distributed Global Search and works as a metasearch library
"""

results = DDGS().text(
    "latest LangChain documentation",
    max_results=5
)
for item in results:
    print(item["title"])
    print(item["href"])
    print('*'*18,'\n')

#ddgs is the newer package name; the older duckduckgo_search package was renamed to ddgs.
# search_tool=DuckDuckGoSearchRun()
# result=search_tool.invoke('today latest news in india')
# print(result)
