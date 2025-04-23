import pytest
from bluer_objects.objects import unique_object

from bluer_flow.workflow.runners import list_of_runners, RunnerType
from bluer_flow.workflow.generic import Workflow
from bluer_flow.workflow.patterns import list_of_patterns
from bluer_flow.workflow.runners.factory import runner_class
from bluer_flow.workflow.runners.generic import GenericRunner


def test_list_of_runners():
    assert list_of_runners()


@pytest.mark.parametrize(
    ["pattern"],
    [[pattern] for pattern in list_of_patterns()],
)
@pytest.mark.parametrize(
    ["runner_type"],
    [[runner_type] for runner_type in list_of_runners()],
)
def test_workflow_runners(
    pattern: str,
    runner_type: str,
):
    job_name = unique_object()

    workflow = Workflow(job_name)

    assert workflow.load_pattern(pattern)

    runner = runner_class[RunnerType[runner_type.upper()]]()
    assert isinstance(runner, GenericRunner)

    assert runner.submit(workflow, dryrun=True)
