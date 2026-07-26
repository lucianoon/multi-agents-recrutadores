# 🤖 Multi-Agent System for Writing Job Descriptions

*[Versão em português](README.md)*

[![CI](https://github.com/lucianoon/multi-agents-recrutadores/actions/workflows/ci.yml/badge.svg)](https://github.com/lucianoon/multi-agents-recrutadores/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/Python-3.10%E2%80%933.13-blue.svg)](https://www.python.org/downloads/)
[![CrewAI](https://img.shields.io/badge/CrewAI-0.28.8-orange.svg)](https://github.com/joaomdmoura/crewAI)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A multi-agent system in Python, built on the **CrewAI** framework, that
automates writing job descriptions: it researches the company's culture and the
market, drafts the posting and reviews it, producing a ready-to-use
`job_posting.md`.

> **Note on language:** the agents' roles, goals and prompts are written in
> Portuguese in `src/agents.py` and `src/tasks.py`, and the interactive CLI
> prompts in Portuguese too. The system therefore produces **job descriptions in
> Portuguese**. This README is a translation of the documentation, not of the
> pipeline's output.

## Table of contents

- [Overview](#-overview)
- [Architecture](#-architecture)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project structure](#-project-structure)
- [Tests](#-tests)
- [Documentation](#-documentation)
- [Contributing](#-contributing)
- [License](#-license)

## 🎯 Overview

The system orchestrates three specialized agents running five tasks in sequence:

1. **Analista de Pesquisa** (research analyst) — analyzes the company's website
   and description, gathers the role's requirements and runs an industry analysis
2. **Redator de Descrição de Vaga** (job description writer) — turns the research
   insights into an engaging draft of the posting
3. **Especialista em Revisão e Edição** (review and editing specialist) — reviews
   clarity, grammar and cultural alignment, then saves the final result

Input is interactive (company domain, description, role and benefits) and the
output is the finished job description in Markdown.

## 🏗️ Architecture

Agents are defined in `src/agents.py`, tasks in `src/tasks.py`, and the
orchestration (a Crew with `Process.sequential`) in `src/main.py`. The actual
flow in the code:

```
User input (via terminal):
  company domain · company description · role · benefits
        │
        ▼
┌─────────────────────────────────────────────────────────────┐
│              Crew (CrewAI, sequential process)              │
│                                                             │
│  Agent: Analista de Pesquisa (research analyst)             │
│  Tools: WebsiteSearchTool, SerperDevTool                    │
│  ├─ 1. research_company_culture_task                        │
│  │     (company culture, values and mission)                │
│  ├─ 2. research_role_requirements_task                      │
│  │     (ideal candidate's skills and qualifications)        │
│  └─ 3. industry_analysis_task                               │
│        (sector trends, challenges and opportunities)        │
│        │                                                    │
│        ▼                                                    │
│  Agent: Redator de Descrição de Vaga (writer)               │
│  Tools: WebsiteSearchTool, SerperDevTool,                   │
│         FileReadTool (sample job description)               │
│  └─ 4. draft_job_posting_task                               │
│        (draft of the job posting)                           │
│        │                                                    │
│        ▼                                                    │
│  Agent: Especialista em Revisão e Edição (reviewer)         │
│  Tools: WebsiteSearchTool, SerperDevTool,                   │
│         FileReadTool                                        │
│  └─ 5. review_and_edit_job_posting_task                     │
│        (final version → output_file)                        │
└─────────────────────────────────────────────────────────────┘
        │
        ▼
   job_posting.md
```

Because the process is sequential, each task's output becomes context for the
next one.

### Tools used by the agents

- **WebsiteSearchTool** — semantic search over the company website's content
- **SerperDevTool** — web search through the Serper API
- **FileReadTool** — reads a sample job description
  (`job_description_example.md`) as a formatting reference

## ✅ Prerequisites

- Python 3.10 to 3.13 (CI uses 3.12)
- An OpenAI API key (`OPENAI_API_KEY`)
- A Serper API key (`SERPER_API_KEY`) — https://serper.dev/

The keys are only needed to **run** the system; the tests run without real keys.

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/lucianoon/multi-agents-recrutadores.git
cd multi-agents-recrutadores
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the dependencies:
```bash
pip install -r requirements.txt
```

4. Configure the environment variables:
```bash
# Linux/Mac:
export OPENAI_API_KEY="your-openai-key"
export SERPER_API_KEY="your-serper-key"

# Windows (PowerShell):
$env:OPENAI_API_KEY="your-openai-key"
$env:SERPER_API_KEY="your-serper-key"
```

## 🚀 Usage

```bash
cd src
python main.py
```

The system asks for four inputs and then runs the agents in sequence. The
prompts are in Portuguese, as shown here:

```
Domínio/Site da empresa (ex: www.empresa.com.br): www.exemplo.com.br
   → Company domain/website
Descrição breve da empresa: Empresa de tecnologia focada em soluções de RH
   → Short company description
Vaga a ser criada (ex: Desenvolvedor Python Sênior): Desenvolvedor Python Sênior
   → Role to create
Benefícios específicos oferecidos: Trabalho remoto, plano de saúde, vale refeição
   → Specific benefits offered
```

At the end, the job description is saved to `job_posting.md` (in the working
directory) and also printed to the terminal. A sample output lives in
[`examples/job_description_example.md`](examples/job_description_example.md).

### Programmatic use

```python
from crewai import Crew, Process
from agents import Agents
from tasks import Tasks

agents = Agents()
research_agent = agents.research_agent()
writer_agent = agents.writer_agent()
review_agent = agents.review_agent()

tasks = Tasks()
crew = Crew(
    agents=[research_agent, writer_agent, review_agent],
    tasks=[
        tasks.research_company_culture_task(research_agent, "Empresa de tecnologia", "www.exemplo.com.br"),
        tasks.research_role_requirements_task(research_agent, "Desenvolvedor Python Sênior"),
        tasks.industry_analysis_task(research_agent, "www.exemplo.com.br", "Empresa de tecnologia"),
        tasks.draft_job_posting_task(writer_agent, "Empresa de tecnologia", "Desenvolvedor Python Sênior", "Trabalho remoto"),
        tasks.review_and_edit_job_posting_task(review_agent, "Desenvolvedor Python Sênior"),
    ],
    process=Process.sequential,
)
result = crew.kickoff()
```

## 📁 Project structure

```
multi-agents-recrutadores/
├── .github/
│   └── workflows/
│       └── ci.yml                  # CI pipeline (GitHub Actions)
├── src/
│   ├── agents.py                   # The 3 agents and their tools
│   ├── tasks.py                    # The 5 tasks
│   └── main.py                     # Orchestration (Crew) and interactive run
├── tests/
│   ├── conftest.py                 # Test setup (fake keys, sys.path)
│   ├── test_agents.py              # Structural tests for the agents
│   ├── test_tasks.py               # Tests for the tasks and their chaining
│   └── test_main.py                # Smoke test for the main module
├── docs/
│   ├── documentation.md            # Full technical documentation
│   ├── roteiro_apresentacao.md     # Presentation script
│   └── linkedin_post.md            # LinkedIn post
├── examples/
│   └── job_description_example.md  # Sample generated job description
├── QUICK_START.md                  # Quick start guide
├── requirements.txt                # Project dependencies
├── README.md                       # This file
└── LICENSE                         # MIT license
```

## 🧪 Tests

The tests are **structural**: they validate how the agents are built (roles,
goals, tools), how the tasks are built (descriptions, expected outputs, output
file) and how agents and tasks chain together — **without calling any LLM or
requiring real API keys** (fake keys are set in `tests/conftest.py`). The
practical consequence is that CI is free and deterministic.

```bash
pip install -r requirements.txt pytest
pytest tests/ -v
```

The same test suite runs automatically on GitHub Actions on every push and pull
request to `main` (see [`.github/workflows/ci.yml`](.github/workflows/ci.yml)).

## 📚 Documentation

The documents below are in Portuguese.

- **[Quick start](QUICK_START.md)**: get going in a few minutes
- **[Technical documentation](docs/documentation.md)**: detailed analysis of the
  architecture and components
- **[Presentation script](docs/roteiro_apresentacao.md)**: guide for presenting
  the solution
- **[LinkedIn post](docs/linkedin_post.md)**: outreach content

## 🤝 Contributing

Contributions are welcome. To contribute:

1. Fork the project
2. Create a branch for your feature (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Before opening the PR, make sure `pytest tests/` passes locally.

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE)
file for details.

---

**Built with ❤️ using CrewAI and Python**
