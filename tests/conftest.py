"""
Configuração compartilhada dos testes.

Os testes são estruturais: nenhuma chamada a LLMs ou APIs externas é feita.
Chaves de API falsas são definidas ANTES de qualquer import de `src/`,
pois a construção dos agentes (ChatOpenAI/ferramentas) exige que as
variáveis de ambiente existam.
"""

import os
import sys
from pathlib import Path

# Chaves falsas: precisam existir antes dos imports de crewai/langchain.
os.environ.setdefault("OPENAI_API_KEY", "test-key-not-real")
os.environ.setdefault("SERPER_API_KEY", "test-key-not-real")

# `src/` não é um pacote; os módulos se importam diretamente
# (ex.: `from agents import Agents`), então adicionamos ao sys.path.
SRC_DIR = Path(__file__).resolve().parent.parent / "src"
sys.path.insert(0, str(SRC_DIR))
