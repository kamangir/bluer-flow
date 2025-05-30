import pytest

from bluer_objects.objects import unique_object

from bluer_flow import env
from bluer_flow.workflow.generic import Workflow
from bluer_flow.workflow.patterns import list_of_patterns


@pytest.mark.parametrize(
    ["pattern"],
    [[pattern] for pattern in list_of_patterns()],
)
def test_workflow(pattern: str):
    job_name = unique_object()

    workflow = Workflow(job_name)

    assert workflow.load_pattern(pattern)

    assert workflow.name
    assert workflow.args

    assert workflow.save()

    workflow_reloaded = Workflow(job_name, load=True)
    assert workflow_reloaded.name == workflow.name
    assert workflow_reloaded.args == workflow_reloaded.args
