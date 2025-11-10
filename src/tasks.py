"""
Definição de Tarefas do Sistema Multi-Agente
Desenvolvido com CrewAI Framework

Este módulo define as tarefas que os agentes executam:
- Pesquisa de cultura empresarial
- Análise de requisitos da vaga
- Criação do rascunho da descrição
- Revisão e edição final
- Análise da indústria
"""

from textwrap import dedent
from crewai import Task


class Tasks:
    """Classe que define as tarefas executadas pelos agentes."""
    
    def research_company_culture_task(self, agent, company_description, company_domain):
        """
        Tarefa de Pesquisa de Cultura Empresarial
        
        Analisa o site da empresa e o domínio fornecido para entender
        cultura, valores, missão e pontos de venda únicos.
        
        Args:
            agent: Agente responsável pela execução
            company_description: Descrição breve da empresa
            company_domain: Domínio/site da empresa
            
        Returns:
            Task: Tarefa configurada
        """
        return Task(
            description=dedent(
                f"""\
                Analise o site da empresa fornecido e o domínio da empresa do gerente de contratação {company_domain}, descrição: "{company_description}". Concentre-se em entender a cultura, os valores e a missão da empresa. Identifique pontos de venda exclusivos e projetos ou conquistas específicas destacadas no site.
                Compile um relatório resumindo esses insights, especificamente como eles podem ser aproveitados em uma publicação de vaga para atrair os candidatos certos."""
            ),
            expected_output=dedent(
                """\
                Um relatório abrangente detalhando a cultura, os valores e a missão da empresa, juntamente com pontos de venda específicos relevantes para a vaga. Sugestões sobre a incorporação desses insights na publicação da vaga devem ser incluídas."""
            ),
            agent=agent,
        )

    def research_role_requirements_task(self, agent, hiring_needs):
        """
        Tarefa de Análise de Requisitos da Vaga
        
        Identifica habilidades, experiências e qualidades necessárias
        para o candidato ideal.
        
        Args:
            agent: Agente responsável pela execução
            hiring_needs: Necessidades de contratação descritas
            
        Returns:
            Task: Tarefa configurada
        """
        return Task(
            description=dedent(
                f"""\
                Com base nas necessidades do gerente de contratação: "{hiring_needs}", identifique as principais habilidades, experiências e qualidades que o candidato ideal deve possuir para a vaga. Considere os projetos atuais da empresa, seu cenário competitivo e as tendências da indústria. Prepare uma lista de requisitos e qualificações de vaga recomendados que se alinhem com as necessidades e valores da empresa."""
            ),
            expected_output=dedent(
                """\
                Uma lista de habilidades, experiências e qualidades recomendadas para o candidato ideal, alinhadas com a cultura da empresa, projetos em andamento e os requisitos específicos da vaga."""
            ),
            agent=agent,
        )

    def draft_job_posting_task(self, agent, company_description, hiring_needs, specific_benefits):
        """
        Tarefa de Criação do Rascunho da Descrição de Vaga
        
        Elabora uma publicação de vaga detalhada e envolvente.
        
        Args:
            agent: Agente responsável pela execução
            company_description: Descrição da empresa
            hiring_needs: Necessidades de contratação
            specific_benefits: Benefícios específicos oferecidos
            
        Returns:
            Task: Tarefa configurada
        """
        return Task(
            description=dedent(
                f"""\
                Elabore uma publicação de vaga para a função descrita pelo gerente de contratação: "{hiring_needs}". Use os insights sobre "{company_description}" para começar com uma introdução convincente, seguida por uma descrição detalhada da função, responsabilidades e habilidades e qualificações necessárias. Certifique-se de que o tom esteja alinhado com a cultura da empresa e incorpore quaisquer benefícios ou oportunidades exclusivos oferecidos pela empresa.
                Benefícios específicos: "{specific_benefits}"""
            ),
            expected_output=dedent(
                """\
                Uma publicação de vaga detalhada e envolvente que inclui uma introdução, descrição da função, responsabilidades, requisitos e benefícios exclusivos da empresa. O tom deve ressoar com a cultura e os valores da empresa, visando atrair os candidatos certos."""
            ),
            agent=agent,
        )

    def review_and_edit_job_posting_task(self, agent, hiring_needs):
        """
        Tarefa de Revisão e Edição da Descrição de Vaga
        
        Revisa o rascunho para garantir clareza, engajamento e alinhamento
        com a cultura da empresa.
        
        Args:
            agent: Agente responsável pela execução
            hiring_needs: Necessidades de contratação descritas
            
        Returns:
            Task: Tarefa configurada com output_file
        """
        return Task(
            description=dedent(
                f"""\
                Revise o rascunho da publicação da vaga para a função: "{hiring_needs}". Verifique a clareza, o engajamento, a precisão gramatical e o alinhamento com a cultura e os valores da empresa. Edite e refine o conteúdo, garantindo que ele se dirija diretamente aos candidatos desejados e reflita com precisão os benefícios e oportunidades exclusivos da função. Forneça feedback para quaisquer revisões necessárias."""
            ),
            expected_output=dedent(
                """\
                Uma publicação de vaga polida, sem erros, clara, envolvente e perfeitamente alinhada com a cultura e os valores da empresa. Feedback sobre possíveis melhorias e aprovação final para publicação. Formatada em markdown."""
            ),
            agent=agent,
            output_file="job_posting.md",
        )

    def industry_analysis_task(self, agent, company_domain, company_description):
        """
        Tarefa de Análise da Indústria
        
        Conduz análise aprofundada da indústria relacionada ao domínio
        da empresa, identificando tendências e oportunidades.
        
        Args:
            agent: Agente responsável pela execução
            company_domain: Domínio/site da empresa
            company_description: Descrição da empresa
            
        Returns:
            Task: Tarefa configurada
        """
        return Task(
            description=dedent(
                f"""\
                Conduza uma análise aprofundada da indústria relacionada ao domínio da empresa: "{company_domain}". Investigue as tendências atuais, desafios e oportunidades dentro da indústria, utilizando relatórios de mercado, desenvolvimentos recentes e opiniões de especialistas. Avalie como esses fatores podem impactar a vaga que está sendo contratada e a atratividade geral da posição para potenciais candidatos.
                Considere como a posição da empresa dentro desta indústria e sua resposta a essas tendências podem ser alavancadas para atrair os melhores talentos. Inclua em seu relatório como a função contribui para abordar desafios da indústria ou aproveitar oportunidades."""
            ),
            expected_output=dedent(
                """\
                Um relatório de análise detalhado que identifica as principais tendências, desafios e oportunidades da indústria relevantes para o domínio da empresa e a vaga específica. Este relatório deve fornecer insights estratégicos sobre o posicionamento da vaga e da empresa como uma escolha atraente para potenciais candidatos."""
            ),
            agent=agent,
        )
