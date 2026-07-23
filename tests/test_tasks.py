"""Testes estruturais das tarefas e do encadeamento agente-tarefa (sem chamadas a LLM)."""

import pytest

from agents import Agents
from tasks import Tasks

COMPANY_DESCRIPTION = "Empresa de tecnologia focada em RH"
COMPANY_DOMAIN = "www.exemplo.com.br"
HIRING_NEEDS = "Desenvolvedor Python Sênior"
SPECIFIC_BENEFITS = "Trabalho remoto e plano de saúde"


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


@pytest.fixture(scope="module")
def tasks():
    return Tasks()


class TestResearchCompanyCultureTask:
    @pytest.fixture(scope="class")
    def task(self, tasks, research_agent):
        return tasks.research_company_culture_task(
            research_agent, COMPANY_DESCRIPTION, COMPANY_DOMAIN
        )

    def test_inputs_interpolated_in_description(self, task):
        assert COMPANY_DESCRIPTION in task.description
        assert COMPANY_DOMAIN in task.description

    def test_expected_output_not_empty(self, task):
        assert task.expected_output.strip()

    def test_assigned_to_research_agent(self, task, research_agent):
        assert task.agent is research_agent


class TestResearchRoleRequirementsTask:
    @pytest.fixture(scope="class")
    def task(self, tasks, research_agent):
        return tasks.research_role_requirements_task(research_agent, HIRING_NEEDS)

    def test_inputs_interpolated_in_description(self, task):
        assert HIRING_NEEDS in task.description

    def test_expected_output_not_empty(self, task):
        assert task.expected_output.strip()

    def test_assigned_to_research_agent(self, task, research_agent):
        assert task.agent is research_agent


class TestIndustryAnalysisTask:
    @pytest.fixture(scope="class")
    def task(self, tasks, research_agent):
        return tasks.industry_analysis_task(
            research_agent, COMPANY_DOMAIN, COMPANY_DESCRIPTION
        )

    def test_inputs_interpolated_in_description(self, task):
        assert COMPANY_DOMAIN in task.description

    def test_expected_output_not_empty(self, task):
        assert task.expected_output.strip()

    def test_assigned_to_research_agent(self, task, research_agent):
        assert task.agent is research_agent


class TestDraftJobPostingTask:
    @pytest.fixture(scope="class")
    def task(self, tasks, writer_agent):
        return tasks.draft_job_posting_task(
            writer_agent, COMPANY_DESCRIPTION, HIRING_NEEDS, SPECIFIC_BENEFITS
        )

    def test_inputs_interpolated_in_description(self, task):
        assert COMPANY_DESCRIPTION in task.description
        assert HIRING_NEEDS in task.description
        assert SPECIFIC_BENEFITS in task.description

    def test_expected_output_not_empty(self, task):
        assert task.expected_output.strip()

    def test_assigned_to_writer_agent(self, task, writer_agent):
        assert task.agent is writer_agent


class TestReviewAndEditJobPostingTask:
    @pytest.fixture(scope="class")
    def task(self, tasks, review_agent):
        return tasks.review_and_edit_job_posting_task(review_agent, HIRING_NEEDS)

    def test_inputs_interpolated_in_description(self, task):
        assert HIRING_NEEDS in task.description

    def test_expected_output_not_empty(self, task):
        assert task.expected_output.strip()

    def test_assigned_to_review_agent(self, task, review_agent):
        assert task.agent is review_agent

    def test_writes_output_file(self, task):
        assert task.output_file == "job_posting.md"
