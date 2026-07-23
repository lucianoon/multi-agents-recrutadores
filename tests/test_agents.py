"""Testes estruturais dos agentes (sem chamadas a LLM)."""

import pytest

from agents import Agents


@pytest.fixture(scope="module")
def agents():
    return Agents()


@pytest.fixture(scope="module")
def research_agent(agents):
    return agents.research_agent()


@pytest.fixture(scope="module")
def writer_agent(agents):
    return agents.writer_agent()


@pytest.fixture(scope="module")
def review_agent(agents):
    return agents.review_agent()


class TestResearchAgent:
    def test_role(self, research_agent):
        assert research_agent.role == "Analista de Pesquisa"

    def test_goal_and_backstory_not_empty(self, research_agent):
        assert research_agent.goal.strip()
        assert research_agent.backstory.strip()

    def test_has_two_tools(self, research_agent):
        assert len(research_agent.tools) == 2


class TestWriterAgent:
    def test_role(self, writer_agent):
        assert writer_agent.role == "Redator de Descrição de Vaga"

    def test_goal_and_backstory_not_empty(self, writer_agent):
        assert writer_agent.goal.strip()
        assert writer_agent.backstory.strip()

    def test_has_three_tools(self, writer_agent):
        assert len(writer_agent.tools) == 3


class TestReviewAgent:
    def test_role(self, review_agent):
        assert review_agent.role == "Especialista em Revisão e Edição"

    def test_goal_and_backstory_not_empty(self, review_agent):
        assert review_agent.goal.strip()
        assert review_agent.backstory.strip()

    def test_has_three_tools(self, review_agent):
        assert len(review_agent.tools) == 3


def test_agents_are_distinct(research_agent, writer_agent, review_agent):
    roles = {research_agent.role, writer_agent.role, review_agent.role}
    assert len(roles) == 3


def test_all_agents_verbose(research_agent, writer_agent, review_agent):
    for agent in (research_agent, writer_agent, review_agent):
        assert agent.verbose is True
