# 🚀 Guia Rápido de Início

Este guia ajudará você a começar a usar o Sistema Multi-Agente para Criação de Descrições de Vagas em poucos minutos.

## ⚡ Instalação Rápida

### 1. Clone o Repositório

```bash
git clone https://github.com/lucianoon/multi-agents-recrutadores.git
cd multi-agents-recrutadores
```

### 2. Configure o Ambiente

```bash
# Crie um ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# No Linux/Mac:
source venv/bin/activate
# No Windows:
venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt
```

### 3. Configure as Chaves de API

Você precisará de duas chaves de API:

**OpenAI API Key** (para os modelos de linguagem):
- Acesse: https://platform.openai.com/api-keys
- Crie uma nova chave de API

**Serper API Key** (para pesquisa web):
- Acesse: https://serper.dev/
- Crie uma conta gratuita e obtenha sua chave

Configure as variáveis de ambiente:

```bash
# No Linux/Mac:
export OPENAI_API_KEY="sua-chave-openai-aqui"
export SERPER_API_KEY="sua-chave-serper-aqui"

# No Windows (PowerShell):
$env:OPENAI_API_KEY="sua-chave-openai-aqui"
$env:SERPER_API_KEY="sua-chave-serper-aqui"
```

## 🎯 Primeiro Uso

### Execute o Sistema

```bash
cd src
python main.py
```

### Forneça as Informações

O sistema solicitará:

1. **Domínio/Site da empresa**: `www.suaempresa.com.br`
2. **Descrição da empresa**: `Empresa de tecnologia focada em IA`
3. **Vaga a ser criada**: `Desenvolvedor Python Sênior`
4. **Benefícios específicos**: `Home office, plano de saúde, vale refeição`

### Resultado

O sistema criará automaticamente um arquivo `job_posting.md` com a descrição completa da vaga!

## 📊 Exemplo de Saída

```markdown
# Desenvolvedor Python Sênior

## Sobre a Empresa
[Descrição personalizada baseada na análise do site]

## A Oportunidade
[Descrição envolvente da vaga]

## Responsabilidades
[Lista detalhada de responsabilidades]

## Requisitos
[Requisitos técnicos e comportamentais]

## Benefícios
[Benefícios específicos da empresa]
```

## 🔧 Personalização

### Modificar os Agentes

Edite `src/agents.py` para ajustar:
- Papéis dos agentes
- Objetivos
- Ferramentas utilizadas

### Modificar as Tarefas

Edite `src/tasks.py` para ajustar:
- Descrições das tarefas
- Outputs esperados
- Fluxo de trabalho

## 📚 Próximos Passos

- Leia a [Documentação Completa](docs/documentation.md)
- Veja o [Roteiro de Apresentação](docs/roteiro_apresentacao.md)
- Confira exemplos em `examples/`

## ❓ Problemas Comuns

### Erro de Chave de API

```
Error: Invalid API key
```

**Solução**: Verifique se as variáveis de ambiente estão configuradas corretamente.

### Erro de Dependências

```
ModuleNotFoundError: No module named 'crewai'
```

**Solução**: Certifique-se de que o ambiente virtual está ativado e execute `pip install -r requirements.txt`.

## 💡 Dicas

- Use descrições detalhadas da empresa para melhores resultados
- Seja específico sobre os requisitos da vaga
- O sistema funciona melhor com sites corporativos bem estruturados

## 🆘 Suporte

Para dúvidas ou problemas:
- Abra uma [Issue no GitHub](https://github.com/lucianoon/multi-agents-recrutadores/issues)
- Entre em contato via LinkedIn

---

**Pronto para revolucionar seu recrutamento? Comece agora!** 🚀
