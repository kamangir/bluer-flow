from blueness import module
from bluer_options import string

from bluer_flow import NAME
from bluer_flow.workflow.runners.localflow.runner import LocalFlowRunner
from bluer_flow.logger import logger


NAME = module.name(__file__, NAME)


def eval(
    command_line: str,
    type: str = "cpu",
    verbose: bool = False,
) -> bool:
    logger.info(f"{NAME}.eval: {command_line}")

    runner = LocalFlowRunner()

    job_name = "localflow-job-{}".format(string.random())

    return runner.submit_command(
        command_line=command_line,
        job_name=job_name,
        dependencies=[],
        verbose=verbose,
        type=type,
    )
