# 🤖 Sistema Multi-Agente para Criação de Descrições de Vagas

*[English version](README.en.md)*

[![CI](https://github.com/lucianoon/multi-agents-recrutadores/actions/workflows/ci.yml/badge.svg)](https://github.com/lucianoon/multi-agents-recrutadores/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/Python-3.10%E2%80%933.13-blue.svg)](https://www.python.org/downloads/)
[![CrewAI](https://img.shields.io/badge/CrewAI-0.28.8-orange.svg)](https://github.com/joaomdmoura/crewAI)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Sistema multi-agente em Python, construído com o framework **CrewAI**, que automatiza a criação de descrições de vagas: pesquisa a cultura da empresa e o mercado, redige a publicação e a revisa, gerando um arquivo `job_posting.md` pronto para uso.

## 📋 Índice

- [Visão Geral](#-visão-geral)
- [Arquitetura](#-arquitetura)
- [Pré-requisitos](#-pré-requisitos)
- [Instalação](#-instalação)
- [Uso](#-uso)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Testes](#-testes)
- [Documentação](#-documentação)
- [Contribuindo](#-contribuindo)
- [Licença](#-licença)

## 🎯 Visão Geral

O sistema orquestra três agentes especializados que executam cinco tarefas em sequência:

1. **Analista de Pesquisa** — analisa o site e a descrição da empresa, levanta requisitos da vaga e faz análise da indústria
2. **Redator de Descrição de Vaga** — transforma os insights da pesquisa em um rascunho envolvente da publicação
3. **Especialista em Revisão e Edição** — revisa clareza, gramática e alinhamento cultural, e salva o resultado final

A entrada é interativa (domínio da empresa, descrição, vaga e benefícios) e a saída é a descrição da vaga finalizada em Markdown.

## 🏗️ Arquitetura

Os agentes são definidos em `src/agents.py`, as tarefas em `src/tasks.py` e a orquestração (Crew com `Process.sequential`) em `src/main.py`. Fluxo real do código:

```
Entradas do usuário (via terminal):
  domínio da empresa · descrição da empresa · vaga · benefícios
        │
        ▼
┌─────────────────────────────────────────────────────────────┐
│              Crew (CrewAI, processo sequencial)             │
│                                                             │
│  Agente: Analista de Pesquisa                               │
│  Ferramentas: WebsiteSearchTool, SerperDevTool              │
│  ├─ 1. research_company_culture_task                        │
│  │     (cultura, valores e missão da empresa)               │
│  ├─ 2. research_role_requirements_task                      │
│  │     (habilidades e qualificações do candidato ideal)     │
│  └─ 3. industry_analysis_task                               │
│        (tendências, desafios e oportunidades do setor)      │
│        │                                                    │
│        ▼                                                    │
│  Agente: Redator de Descrição de Vaga                       │
│  Ferramentas: WebsiteSearchTool, SerperDevTool,             │
│               FileReadTool (exemplo de descrição)           │
│  └─ 4. draft_job_posting_task                               │
│        (rascunho da publicação da vaga)                     │
│        │                                                    │
│        ▼                                                    │
│  Agente: Especialista em Revisão e Edição                   │
│  Ferramentas: WebsiteSearchTool, SerperDevTool,             │
│               FileReadTool                                  │
│  └─ 5. review_and_edit_job_posting_task                     │
│        (versão final → output_file)                         │
└─────────────────────────────────────────────────────────────┘
        │
        ▼
   job_posting.md
```

Como o processo é sequencial, a saída de cada tarefa serve de contexto para a seguinte.

### Ferramentas utilizadas pelos agentes

- **WebsiteSearchTool** — busca semântica no conteúdo do site da empresa
- **SerperDevTool** — pesquisa na web via API do Serper
- **FileReadTool** — lê um exemplo de descrição de vaga (`job_description_example.md`) como referência de formato

## ✅ Pré-requisitos

- Python 3.10 a 3.13 (o CI usa 3.12)
- Chave de API da OpenAI (`OPENAI_API_KEY`)
- Chave de API do Serper (`SERPER_API_KEY`) — https://serper.dev/

As chaves só são necessárias para **executar** o sistema; os testes rodam sem chaves reais.

## 🛠️ Instalação

1. Clone o repositório:
```bash
git clone https://github.com/lucianoon/multi-agents-recrutadores.git
cd multi-agents-recrutadores
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:
```bash
# Linux/Mac:
export OPENAI_API_KEY="sua-chave-openai"
export SERPER_API_KEY="sua-chave-serper"

# Windows (PowerShell):
$env:OPENAI_API_KEY="sua-chave-openai"
$env:SERPER_API_KEY="sua-chave-serper"
```

## 🚀 Uso

```bash
cd src
python main.py
```

O sistema solicitará quatro informações e executará os agentes em sequência:

```
Domínio/Site da empresa (ex: www.empresa.com.br): www.exemplo.com.br
Descrição breve da empresa: Empresa de tecnologia focada em soluções de RH
Vaga a ser criada (ex: Desenvolvedor Python Sênior): Desenvolvedor Python Sênior
Benefícios específicos oferecidos: Trabalho remoto, plano de saúde, vale refeição
```

Ao final, a descrição da vaga é salva em `job_posting.md` (no diretório de execução) e também exibida no terminal. Um exemplo de saída está em [`examples/job_description_example.md`](examples/job_description_example.md).

### Uso programático

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

## 📁 Estrutura do Projeto

```
multi-agents-recrutadores/
├── .github/
│   └── workflows/
│       └── ci.yml                  # Pipeline de CI (GitHub Actions)
├── src/
│   ├── agents.py                   # Definição dos 3 agentes e suas ferramentas
│   ├── tasks.py                    # Definição das 5 tarefas
│   └── main.py                     # Orquestração (Crew) e execução interativa
├── tests/
│   ├── conftest.py                 # Configuração dos testes (chaves falsas, sys.path)
│   ├── test_agents.py              # Testes estruturais dos agentes
│   ├── test_tasks.py               # Testes das tarefas e do encadeamento
│   └── test_main.py                # Teste de fumaça do módulo principal
├── docs/
│   ├── documentation.md            # Documentação técnica completa
│   ├── roteiro_apresentacao.md     # Roteiro para apresentação
│   └── linkedin_post.md            # Post para LinkedIn
├── examples/
│   └── job_description_example.md  # Exemplo de descrição de vaga gerada
├── QUICK_START.md                  # Guia rápido de início
├── requirements.txt                # Dependências do projeto
├── README.md                       # Este arquivo
└── LICENSE                         # Licença MIT
```

## 🧪 Testes

Os testes são **estruturais**: validam a construção dos agentes (papéis, objetivos, ferramentas), das tarefas (descrições, saídas esperadas, arquivo de saída) e o encadeamento entre agentes e tarefas — **sem chamar LLMs nem exigir chaves de API reais** (chaves falsas são definidas em `tests/conftest.py`).

```bash
pip install -r requirements.txt pytest ruff mypy
ruff check .    # lint
mypy            # checagem de tipos
pytest tests/ -v
```

Os mesmos três gates rodam automaticamente no GitHub Actions a cada push e pull request para `main` (ver [`.github/workflows/ci.yml`](.github/workflows/ci.yml)).

## 📚 Documentação

- **[Guia Rápido](QUICK_START.md)**: comece a usar em poucos minutos
- **[Documentação Técnica](docs/documentation.md)**: análise detalhada da arquitetura e componentes
- **[Roteiro de Apresentação](docs/roteiro_apresentacao.md)**: guia para apresentar a solução
- **[Post LinkedIn](docs/linkedin_post.md)**: conteúdo para divulgação

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

Antes de abrir o PR, garanta que `ruff check .`, `mypy` e `pytest tests/` passam localmente.

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

---

**Desenvolvido com ❤️ usando CrewAI e Python**
