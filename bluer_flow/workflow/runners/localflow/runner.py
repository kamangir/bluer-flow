from typing import Any, List, Tuple
from tqdm import tqdm

from bluer_objects.mlflow.tags import set_tags, get_tags
from bluer_objects.metadata import post_to_object

from bluer_flow.workflow.generic import Workflow
from bluer_flow.workflow.runners.generic import GenericRunner
from bluer_flow.workflow.runners.localflow import ICON


class LocalFlowRunner(GenericRunner):
    def __init__(self, **kw_args):
        super().__init__(**kw_args)
        self.type_name: str = "localflow"

    def monitor_function(
        self,
        workflow: Workflow,
        hot_node: str,
    ) -> Workflow:
        workflow = super().monitor_function(workflow, hot_node)

        for node in tqdm(workflow.G.nodes):
            workflow.G.nodes[node]["status"] = get_tags(
                object_name=workflow.node_job_name(node),
            )[1].get("status", "UNKNOWN")

        return workflow

    def submit_command(
        self,
        command_line: str,
        job_name: str,
        dependencies: List[str],
        verbose: bool = False,
        type: str = "cpu",
    ) -> Tuple[bool, Any]:
        assert super().submit_command(
            command_line,
            job_name,
            dependencies,
            verbose,
            type,
        )[0]

        if not post_to_object(
            object_name=job_name,
            key="command_line",
            value=command_line,
            upload=True,
        ):
            return False, {"job_id": job_name}

        list_of_tags = {
            f"depends-on-{dependency}": "yes" for dependency in dependencies
        }
        list_of_tags.update(
            {
                "contains": "localflow-job",
                "status": "PENDING" if dependencies else "RUNNABLE",
                "type": type,
            }
        )

        return set_tags(
            object_name=job_name,
            tags=list_of_tags,
            icon=ICON,
        ), {"job_id": job_name}
