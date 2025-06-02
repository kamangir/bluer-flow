from bluer_ai.tests.test_env import test_bluer_ai_env
from bluer_objects.tests.test_env import test_bluer_objects_env

from bluer_flow import env


def test_required_env():
    test_bluer_ai_env()
    test_bluer_objects_env()


def test_bluer_flow_env():
    assert env.BLUER_FLOW_DEFAULT_WORKFLOW_PATTERN

    assert isinstance(env.LOCALFLOW_SLEEP_BETWEEN_JOBS, int)
    assert env.LOCALFLOW_SLEEP_BETWEEN_JOBS > 0
