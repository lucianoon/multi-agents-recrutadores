"""
Sistema Multi-Agente para Criação de Descrições de Vagas
Desenvolvido com CrewAI Framework

Este módulo define os agentes especializados que compõem o sistema:
- Agente Pesquisador: Analisa cultura empresarial e requisitos
- Agente Redator: Cria descrições de vagas envolventes
- Agente Revisor: Garante qualidade e alinhamento
"""

from crewai import Agent
from crewai_tools import SerperDevTool, WebsiteSearchTool, FileReadTool


# Inicialização das ferramentas
web_search_tool = WebsiteSearchTool()
serper_dev_tool = SerperDevTool()
file_read_tool = FileReadTool(
    file_path="job_description_example.md",
    description="Uma ferramenta para ler o arquivo de exemplo de descrição de vaga.",
)


class Agents:
    """Classe que define os agentes especializados do sistema."""
    
    def research_agent(self):
        """
        Agente Pesquisador - Analista de Pesquisa
        
        Responsável por analisar o site da empresa e a descrição fornecida
        para extrair insights sobre cultura, valores e necessidades específicas.
        
        Returns:
            Agent: Instância configurada do agente pesquisador
        """
        return Agent(
            role="Analista de Pesquisa",
            goal="Analisar o site da empresa e a descrição fornecida para extrair insights sobre cultura, valores e necessidades específicas.",
            tools=[web_search_tool, serper_dev_tool],
            backstory="Especialista em analisar culturas de empresas e identificar valores e necessidades chave de várias fontes, incluindo sites e breves descrições.",
            verbose=True,
        )

    def writer_agent(self):
        """
        Agente Redator - Redator de Descrição de Vaga
        
        Utiliza insights do Analista de Pesquisa para criar uma publicação
        de vaga detalhada, envolvente e atraente.
        
        Returns:
            Agent: Instância configurada do agente redator
        """
        return Agent(
            role="Redator de Descrição de Vaga",
            goal="Usar insights do Analista de Pesquisa para criar uma publicação de vaga detalhada, envolvente e atraente.",
            tools=[web_search_tool, serper_dev_tool, file_read_tool],
            backstory="Habilidoso em elaborar descrições de vagas convincentes que ressoam com os valores da empresa e atraem os candidatos certos.",
            verbose=True,
        )

    def review_agent(self):
        """
        Agente Revisor - Especialista em Revisão e Edição
        
        Revisa a publicação da vaga quanto à clareza, engajamento, precisão
        gramatical e alinhamento com os valores da empresa.
        
        Returns:
            Agent: Instância configurada do agente revisor
        """
        return Agent(
            role="Especialista em Revisão e Edição",
            goal="Revisar a publicação da vaga quanto à clareza, engajamento, precisão gramatical e alinhamento com os valores da empresa e refiná-la para garantir a perfeição.",
            tools=[web_search_tool, serper_dev_tool, file_read_tool],
            backstory="Um editor meticuloso com atenção aos detalhes, garantindo que cada conteúdo seja claro, envolvente e gramaticalmente perfeito.",
            verbose=True,
        )
