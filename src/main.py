"""
Sistema Multi-Agente para Criação de Descrições de Vagas
Arquivo Principal de Execução

Este script orquestra a execução dos agentes e tarefas para gerar
descrições de vagas de alta qualidade de forma automatizada.
"""

from crewai import Crew, Process
from agents import Agents
from tasks import Tasks


def main():
    """
    Função principal que executa o sistema multi-agente.
    
    Coleta informações da empresa e da vaga, inicializa os agentes,
    define as tarefas e executa o processo de criação da descrição.
    """
    
    print("=" * 60)
    print("Sistema Multi-Agente para Criação de Descrições de Vagas")
    print("=" * 60)
    print()
    
    # Coleta de informações
    print("Por favor, forneça as seguintes informações:\n")
    
    company_domain = input("Domínio/Site da empresa (ex: www.empresa.com.br): ")
    company_description = input("Descrição breve da empresa: ")
    hiring_needs = input("Vaga a ser criada (ex: Desenvolvedor Python Sênior): ")
    specific_benefits = input("Benefícios específicos oferecidos: ")
    
    print("\n" + "=" * 60)
    print("Iniciando processamento...")
    print("=" * 60 + "\n")
    
    # Inicialização dos agentes
    agents = Agents()
    research_agent = agents.research_agent()
    writer_agent = agents.writer_agent()
    review_agent = agents.review_agent()
    
    # Inicialização das tarefas
    tasks = Tasks()
    
    # Definição das tarefas
    research_company_culture = tasks.research_company_culture_task(
        research_agent, 
        company_description, 
        company_domain
    )
    
    research_role_requirements = tasks.research_role_requirements_task(
        research_agent, 
        hiring_needs
    )
    
    industry_analysis = tasks.industry_analysis_task(
        research_agent, 
        company_domain, 
        company_description
    )
    
    draft_job_posting = tasks.draft_job_posting_task(
        writer_agent, 
        company_description, 
        hiring_needs, 
        specific_benefits
    )
    
    review_and_edit_job_posting = tasks.review_and_edit_job_posting_task(
        review_agent, 
        hiring_needs
    )
    
    # Criação da equipe (Crew)
    crew = Crew(
        agents=[research_agent, writer_agent, review_agent],
        tasks=[
            research_company_culture,
            research_role_requirements,
            industry_analysis,
            draft_job_posting,
            review_and_edit_job_posting
        ],
        process=Process.sequential,  # Execução sequencial das tarefas
        verbose=True
    )
    
    # Execução do processo
    result = crew.kickoff()
    
    print("\n" + "=" * 60)
    print("Processamento concluído!")
    print("=" * 60)
    print("\nA descrição da vaga foi salva em: job_posting.md")
    print("\nResultado:")
    print(result)


if __name__ == "__main__":
    main()
