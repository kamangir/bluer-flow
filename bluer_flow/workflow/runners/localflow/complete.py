from tqdm import tqdm

from blueness import module
from bluer_objects.mlflow.lock.functions import lock, unlock
from bluer_objects.mlflow.tags import set_tags, get_tags, search, create_filter_string

from bluer_flow import NAME
from bluer_flow.workflow.runners.localflow import ICON
from bluer_flow.logger import logger

NAME = module.name(__file__, NAME)


def complete_job(
    job_name: str,
    status: str,
    verbose: bool = True,
) -> bool:
    logger.info(f"{NAME}.complete_job: {job_name} @ {status}")

    if not set_tags(
        object_name=job_name,
        tags={
            "status": "SUCCEEDED" if status == "0" else "FAILED",
        },
        icon=ICON,
    ):
        return False

    if status != "0":
        logger.error("job failed, will not clear dependencies.")
        return True

    list_of_dependent_jobs = search(
        create_filter_string(
            {
                f"depends-on-{job_name}": 1,
            }
        )
    )
    if not list_of_dependent_jobs:
        logger.info("no dependent job.")
        return True

    logger.info("examining {} dependent job(s).".format(len(list_of_dependent_jobs)))
    for dependent_job_name in tqdm(list_of_dependent_jobs):
        logger.info(f"examining {dependent_job_name} ...")

        if not lock(
            object_name=dependent_job_name,
            lock_name="complete_job",
            verbose=verbose,
        ):
            return False

        if not set_tags(
            object_name=dependent_job_name,
            tags={
                f"depends-on-{job_name}": 0,
            },
            icon=ICON,
        ):
            return False

        success, list_of_tags = get_tags(object_name=dependent_job_name)
        if not success:
            return False

        remaining_dependencies = [
            dependency.split("depends-on-", 1)[1]
            for dependency, value in list_of_tags
            if dependency.startswith("depends-on-") and value == 1
        ]
        if remaining_dependencies:
            logger.info(
                "{} remaining dependency(s): {}".format(
                    len(remaining_dependencies),
                    ", ".join(remaining_dependencies),
                )
            )
        else:
            logger.info("no remaining dependencies.")
            if not set_tags(
                object_name=dependent_job_name,
                tags={"status": "RUNNABLE"},
                icon=ICON,
            ):
                return False

        if not unlock(
            object_name=dependent_job_name,
            lock_name="complete_job",
            verbose=verbose,
        ):
            return False

    return True
