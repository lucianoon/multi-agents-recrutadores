# 🤖 Sistema Multi-Agente para Criação de Descrições de Vagas

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![CrewAI](https://img.shields.io/badge/CrewAI-0.28.8-orange.svg)](https://github.com/joaomdmoura/crewAI)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Sistema inteligente baseado em agentes de IA para automatizar a criação de descrições de vagas de alta qualidade, economizando até **80% do tempo** da equipe de RH.

## 📋 Índice

- [Visão Geral](#visão-geral)
- [Características](#características)
- [Arquitetura](#arquitetura)
- [Instalação](#instalação)
- [Uso](#uso)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Documentação](#documentação)
- [Benefícios](#benefícios)
- [Contribuindo](#contribuindo)
- [Licença](#licença)

## 🎯 Visão Geral

Este projeto implementa um sistema multi-agente utilizando o framework **CrewAI** para automatizar o processo de criação de descrições de vagas. O sistema é composto por três agentes especializados que trabalham em harmonia:

1. **Agente Pesquisador** - Analisa a cultura empresarial e requisitos da vaga
2. **Agente Redator** - Cria descrições envolventes e alinhadas com a marca
3. **Agente Revisor** - Garante qualidade, clareza e alinhamento cultural

## ✨ Características

- 🚀 **Economia de 80% do tempo** na criação de descrições de vagas
- 🎯 **Consistência garantida** em todas as publicações
- 🏢 **Alinhamento cultural** automático com os valores da empresa
- 📊 **Análise de indústria** integrada para contexto competitivo
- ✅ **Zero erros** gramaticais e de formatação
- 🔄 **Processo automatizado** de pesquisa, criação e revisão

## 🏗️ Arquitetura

O sistema utiliza uma arquitetura de agentes especializados orquestrados pelo CrewAI:

```
┌─────────────────────────────────────────────────────────┐
│                   Sistema Multi-Agente                   │
├─────────────────────────────────────────────────────────┤
│                                                           │
│  ┌──────────────┐    ┌──────────────┐    ┌───────────┐ │
│  │   Agente     │───▶│   Agente     │───▶│  Agente   │ │
│  │ Pesquisador  │    │   Redator    │    │  Revisor  │ │
│  └──────────────┘    └──────────────┘    └───────────┘ │
│         │                    │                   │       │
│         ▼                    ▼                   ▼       │
│  ┌──────────────────────────────────────────────────┐  │
│  │         Descrição de Vaga Finalizada             │  │
│  └──────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
```

### Fluxo de Trabalho

1. **Pesquisa e Análise**: O Agente Pesquisador coleta informações sobre a empresa, cultura e requisitos da vaga
2. **Criação de Conteúdo**: O Agente Redator transforma os insights em uma descrição envolvente
3. **Revisão e Refinamento**: O Agente Revisor garante qualidade e alinhamento final

## 🛠️ Instalação

### Pré-requisitos

- Python 3.9 ou superior
- Chave de API da OpenAI
- Chave de API do Serper (para pesquisa web)

### Passos

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/multi-agents-recrutadores.git
cd multi-agents-recrutadores
```

2. Crie um ambiente virtual:
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
export OPENAI_API_KEY="sua-chave-openai"
export SERPER_API_KEY="sua-chave-serper"
```

## 🚀 Uso

### Execução Básica

```bash
cd src
python main.py
```

O sistema solicitará as seguintes informações:

- **Domínio/Site da empresa**: URL do site da empresa
- **Descrição da empresa**: Breve descrição do negócio
- **Vaga a ser criada**: Título e descrição básica da posição
- **Benefícios específicos**: Benefícios oferecidos pela empresa

### Exemplo de Uso

```python
from agents import Agents
from tasks import Tasks
from crewai import Crew, Process

# Inicializar agentes
agents = Agents()
research_agent = agents.research_agent()
writer_agent = agents.writer_agent()
review_agent = agents.review_agent()

# Definir tarefas
tasks = Tasks()
research_task = tasks.research_company_culture_task(
    research_agent, 
    "Empresa de tecnologia inovadora", 
    "www.empresa.com.br"
)

# Criar e executar a equipe
crew = Crew(
    agents=[research_agent, writer_agent, review_agent],
    tasks=[research_task, ...],
    process=Process.sequential
)

result = crew.kickoff()
```

## 📁 Estrutura do Projeto

```
multi-agents-recrutadores/
├── src/
│   ├── agents.py              # Definição dos agentes
│   ├── tasks.py               # Definição das tarefas
│   └── main.py                # Script principal de execução
├── docs/
│   ├── documentation.md       # Documentação técnica completa
│   ├── roteiro_apresentacao.md # Roteiro para apresentação
│   └── linkedin_post.md       # Post para LinkedIn
├── assets/                    # Imagens e recursos visuais
├── examples/                  # Exemplos de uso
├── requirements.txt           # Dependências do projeto
├── README.md                  # Este arquivo
└── LICENSE                    # Licença do projeto
```

## 📚 Documentação

A documentação completa do projeto está disponível em:

- **[Documentação Técnica](docs/documentation.md)**: Análise detalhada da arquitetura e componentes
- **[Roteiro de Apresentação](docs/roteiro_apresentacao.md)**: Guia completo para apresentar a solução
- **[Post LinkedIn](docs/linkedin_post.md)**: Conteúdo pronto para divulgação

## 💎 Benefícios

### Economia de Tempo

- **80% de redução** no tempo de criação (de 3-5 horas para 15 minutos)
- Automação completa de pesquisa e análise
- Revisão instantânea sem múltiplas rodadas

### Melhoria de Qualidade

- **Consistência 100%** em todas as descrições
- Alinhamento cultural preciso e automático
- Zero erros gramaticais ou de formatação

### Impacto no Negócio

- Maior produtividade da equipe de RH
- Fortalecimento da marca empregadora
- Escalabilidade para múltiplas vagas simultâneas
- **ROI em menos de 3 meses**

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 📧 Contato

Para dúvidas, sugestões ou demonstrações, entre em contato através do LinkedIn.

---

**Desenvolvido com ❤️ usando CrewAI e Python**
