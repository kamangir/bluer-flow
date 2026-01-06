from typing import Tuple

from bluer_ai.env import bluer_ai_gpu_status_cache
from bluer_objects.mlflow.lock.functions import lock, unlock
from bluer_objects.mlflow.tags import search, set_tags

from bluer_flow.logger import logger


def find_job(verbose: bool = True) -> Tuple[bool, str]:
    if not lock(
        object_name="localflow",
        lock_name="find_job",
        verbose=verbose,
    ):
        return False, ""

    success, list_of_jobs = search(
        {
            "contains": "localflow-job",
            "status": "RUNNABLE",
            "type": "gpu" if bluer_ai_gpu_status_cache == "true" else "cpu",
        }
    )
    if not success:
        return False, ""

    job_name = list_of_jobs[0] if len(list_of_jobs) > 0 else ""

    if job_name:
        if not set_tags(
            object_name=job_name,
            tags={
                "status": "RUNNING",
            },
        ):
            return False

    if not unlock(
        object_name="localflow",
        lock_name="find_job",
        verbose=verbose,
    ):
        return False, ""

    return True, job_name
