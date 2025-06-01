from blueness import module

from bluer_flow import NAME
from bluer_flow.logger import logger

NAME = module.name(__file__, NAME)


def complete_job(
    job_name: str,
    status: str,
) -> bool:
    logger.info(f"{NAME}.complete_job: {job_name} @ {status}")

    logger.info("🪄")

    return True
