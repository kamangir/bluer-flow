import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from bluer_flow import NAME
from bluer_flow.workflow.runners.localflow.complete import complete_job
from bluer_flow.workflow.runners.localflow.eval import eval
from bluer_flow.workflow.runners.localflow.find import find_job
from bluer_flow.logger import logger

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="complete_job | eval | find_job",
)
parser.add_argument(
    "--command_line",
    type=str,
)
parser.add_argument(
    "--job_name",
    type=str,
)
parser.add_argument(
    "--status",
    type=str,
)
parser.add_argument(
    "--type",
    type=str,
    default="cpu",
    help="cpu | gpu",
)
parser.add_argument(
    "--verbose",
    type=int,
    default=0,
    help="0 | 1",
)
args = parser.parse_args()

success = False
if args.task == "complete_job":
    success = complete_job(
        job_name=args.job_name,
        status=args.status,
    )
elif args.task == "eval":
    success = eval(
        command_line=args.command_line,
        type=args.type,
        verbose=args.verbose == 1,
    )
elif args.task == "find_job":
    success, job_name = find_job()
    print(job_name)
else:
    success = None

sys_exit(logger, NAME, args.task, success)
