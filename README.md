# LangChain Tools – DDGS & Shell Tool

This project demonstrates how to use **DDGS Web Search** and **Shell Tool** with LangChain.

These tools allow a LangChain application to interact with the **web** and the **local shell/terminal**.

---

## 📌 Concepts

### 1. DDGS

**DDGS (Dux Distributed Global Search)** is a Python library that allows applications to perform web searches programmatically.

It can be used to retrieve web search results and provide them to an LLM or AI agent.

```text
User Question
      ↓
     LLM
      ↓
   DDGS Tool
      ↓
  Web Search
      ↓
 Search Results
      ↓
     LLM
      ↓
    Answer
```

### 2. Shell Tool

The **Shell Tool** allows LangChain applications to execute shell/terminal commands.

```text
User Request
      ↓
     LLM
      ↓
 Shell Tool
      ↓
Terminal Command
      ↓
Command Output
      ↓
     LLM
```

> ⚠️ Shell tools can execute commands on the machine. Use them carefully and avoid allowing untrusted input to execute arbitrary commands.

---

# 🛠️ Installation

## Using pip

Install DDGS:

```bash
pip install -U ddgs
```

Install LangChain Community:

```bash
pip install -U langchain-community
```

Or install both:

```bash
pip install -U ddgs langchain-community
```

## Using uv

If you are using `uv`:

```bash
uv add ddgs langchain-community
```

---

# 🔎 DDGS Example

## Basic Web Search

```python
from ddgs import DDGS

results = DDGS().text(
    "What is LangChain?",
    max_results=5
)

for result in results:
    print("Title:", result["title"])
    print("URL:", result["href"])
    print("Description:", result["body"])
```

### Output

```text
Title: LangChain Documentation
URL: https://...
Description: ...
```

### Common Use Cases

DDGS can be used for:

* Web search
* Retrieving current information
* Searching documentation
* Building AI search applications
* Providing search results to LLMs
* Building web-search agents

---

# 💻 Shell Tool Example

LangChain provides a `ShellTool` for executing shell commands.

```python
from langchain_community.tools import ShellTool

shell_tool = ShellTool()

result = shell_tool.invoke({
    "commands": ["echo Hello World"]
})

print(result)
```

### Example Command

```python
shell_tool.invoke({
    "commands": ["python --version"]
})
```

The tool executes the command and returns the output.

### Common Use Cases

Shell Tool can be used for:

* Running terminal commands
* Executing Python scripts
* Working with files
* Checking installed packages
* Running development commands
* Automating system tasks

---

# 🔗 Using Tools with an LLM

LangChain tools can be provided to an LLM so that the model can decide when to use them.

```text
                 LLM
                  |
          ┌───────┴────────┐
          ↓                ↓
        DDGS          Shell Tool
          ↓                ↓
      Web Search        Terminal
          ↓                ↓
       Results          Output
          └───────┬────────┘
                  ↓
                 LLM
                  ↓
             Final Answer
```

This pattern is commonly used when building **AI agents**.

---

# 📁 Project Structure

```text
langchain-tools/
│
├── ddgs
├── shell_tool
├── requirements.txt
└── README.md
```
---
# 📦 Dependencies

Main packages used in this project:

```text
ddgs
langchain
langchain-community
```

---

# ⚖️ DDGS vs Shell Tool

| Tool           | Purpose                                    |
| -------------- | ------------------------------------------ |
| **DDGS**       | Search the web                             |
| **Shell Tool** | Execute terminal commands                  |
| **LLM**        | Understand requests and generate responses |
| **LangChain**  | Connect LLMs with tools and workflows      |

---

# 🎯 Summary

### DDGS

> **DDGS → Web Search**

Used when an application needs information from the web.

### Shell Tool

> **Shell Tool → Terminal Commands**

Used when an application needs to execute commands on the system.

Together with an LLM, these tools can be used to build more capable **LangChain agents**.

```text
LLM
 │
 ├── DDGS → Search the Web
 │
 └── Shell Tool → Execute Commands
```

---

## 🚀 Learning Goal

The main goal of this project is to understand how **LangChain Tools** work and how external capabilities such as **web search** and **shell execution** can be connected to an LLM.
