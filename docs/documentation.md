
# Documentação Técnica: Sistema Multi-Agente para Criação de Descrições de Vagas

## 1. Visão Geral

Este documento fornece uma análise técnica detalhada de um sistema multi-agente projetado para automatizar a criação de descrições de vagas. O sistema utiliza o framework CrewAI para orquestrar uma equipe de agentes de inteligência artificial (IA) especializados, cada um com uma função específica no processo. A solução visa otimizar o recrutamento, gerando publicações de vagas que são não apenas informativas, mas também alinhadas com a cultura da empresa e atraentes para os candidatos ideais.

O código é estruturado em duas classes principais, `Agents` e `Tasks`, que definem os agentes e as tarefas que eles executam, respectivamente. Essa arquitetura modular permite uma clara separação de responsabilidades e facilita a manutenção e expansão do sistema.

## 2. Arquitetura do Sistema

O sistema é composto por três componentes principais: **Agentes**, **Tarefas** e **Ferramentas**.

### 2.1. Agentes

Os agentes são entidades de IA autônomas com papéis, objetivos e históricos definidos. A classe `Agents` é responsável por instanciar os seguintes agentes:

| Agente | Papel | Objetivo | Backstory |
| :--- | :--- | :--- | :--- |
| `research_agent` | Analista de Pesquisa | Analisar o site da empresa e a descrição fornecida para extrair insights sobre cultura, valores e necessidades específicas. | Especialista em analisar culturas de empresas e identificar valores e necessidades chave de várias fontes, incluindo sites e breves descrições. |
| `writer_agent` | Redator de Descrição de Vaga | Usar insights do Analista de Pesquisa para criar uma publicação de vaga detalhada, envolvente e atraente. | Habilidoso em elaborar descrições de vagas convincentes que ressoam com os valores da empresa e atraem os candidatos certos. |
| `review_agent` | Especialista em Revisão e Edição | Revisar a publicação da vaga quanto à clareza, engajamento, precisão gramatical e alinhamento com os valores da empresa e refiná-la para garantir a perfeição. | Um editor meticuloso com atenção aos detalhes, garantindo que cada conteúdo seja claro, envolvente e gramaticalmente perfeito. |

### 2.2. Ferramentas

As ferramentas são utilitários que os agentes podem usar para realizar suas tarefas. As seguintes ferramentas são definidas e utilizadas:

- **WebsiteSearchTool**: Permite que os agentes pesquisem conteúdo em um site específico. É fundamental para o `research_agent` coletar informações sobre a cultura e os projetos da empresa.
- **SerperDevTool**: Fornece acesso a uma API de pesquisa da web para obter informações gerais e realizar análises de mercado e da indústria.
- **FileReadTool**: Permite a leitura de arquivos locais. Neste caso, é configurado para ler um arquivo de exemplo de descrição de vaga (`job_description_example.md`), que pode servir como modelo ou referência.

### 2.3. Tarefas

A classe `Tasks` define as atividades a serem executadas pelos agentes. Cada tarefa é encapsulada com uma descrição, o resultado esperado e o agente responsável. As seguintes tarefas são definidas:

| Tarefa | Descrição | Resultado Esperado | Agente Designado |
| :--- | :--- | :--- | :--- |
| `research_company_culture_task` | Analisa o site e a descrição da empresa para entender a cultura, valores e missão. | Um relatório abrangente detalhando a cultura, valores e missão da empresa, com sugestões para a publicação da vaga. | `research_agent` |
| `research_role_requirements_task` | Identifica as principais habilidades, experiências e qualificações para o candidato ideal com base nas necessidades de contratação. | Uma lista de habilidades, experiências e qualidades recomendadas para o candidato ideal. | `research_agent` |
| `draft_job_posting_task` | Elabora uma publicação de vaga detalhada e envolvente, alinhada com a cultura da empresa. | Uma publicação de vaga detalhada, incluindo introdução, descrição da função, responsabilidades, requisitos e benefícios. | `writer_agent` |
| `review_and_edit_job_posting_task` | Revisa o rascunho da publicação da vaga para garantir clareza, precisão e alinhamento com a cultura da empresa. | Uma publicação de vaga polida, sem erros e pronta para ser publicada, formatada em Markdown. | `review_agent` |
| `industry_analysis_task` | Conduz uma análise da indústria para identificar tendências, desafios e oportunidades. | Um relatório de análise detalhado sobre as tendências da indústria e o posicionamento da empresa. | `research_agent` |

## 3. Fluxo de Trabalho e Orquestração

O sistema opera em um fluxo de trabalho sequencial, onde a saída de uma tarefa serve como entrada para a próxima. A orquestração é gerenciada pelo framework CrewAI, que coordena a execução das tarefas pelos agentes designados.

1.  **Pesquisa e Análise (research_agent)**: O processo começa com o `research_agent` executando as tarefas `research_company_culture_task`, `research_role_requirements_task` e `industry_analysis_task`. Essas tarefas coletam e sintetizam as informações necessárias sobre a empresa, a vaga e o mercado.

2.  **Redação (writer_agent)**: Com base nos relatórios gerados pelo `research_agent`, o `writer_agent` executa a `draft_job_posting_task` para criar o rascunho inicial da descrição da vaga.

3.  **Revisão e Finalização (review_agent)**: Finalmente, o `review_agent` assume a tarefa `review_and_edit_job_posting_task`. Ele revisa o rascunho, faz as edições necessárias e produz a versão final da publicação da vaga em formato Markdown, pronta para ser utilizada.

## 4. Dependências e Configuração

O sistema depende das seguintes bibliotecas e ferramentas Python:

-   **CrewAI**: O framework principal para a criação e gerenciamento de agentes e tarefas.
-   **SerperDevTool**: Uma ferramenta que requer uma chave de API para acesso à pesquisa web.
-   **WebsiteSearchTool**: Ferramenta para busca em sites.
-   **FileReadTool**: Ferramenta para leitura de arquivos.

Para executar o sistema, é necessário instalar as dependências e configurar as chaves de API necessárias para as ferramentas de pesquisa.

## 5. Conclusão

Este sistema multi-agente representa uma abordagem sofisticada e eficiente para a criação de descrições de vagas. Ao dividir o processo em tarefas especializadas e atribuí-las a agentes de IA dedicados, a solução garante a produção de conteúdo de alta qualidade, relevante e alinhado com os objetivos estratégicos de recrutamento. A arquitetura modular e extensível permite futuras melhorias, como a integração com sistemas de rastreamento de candidatos (ATS) ou a adição de novos agentes para tarefas como a promoção da vaga em redes sociais.
