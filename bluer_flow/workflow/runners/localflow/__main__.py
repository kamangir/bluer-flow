import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from bluer_flow import NAME
from bluer_flow.workflow.runners.localflow.eval import eval
from bluer_flow.logger import logger

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="eval",
)
parser.add_argument(
    "--arg",
    type=bool,
    default=0,
    help="0|1",
)
args = parser.parse_args()

success = False
if args.task == "eval":
    success = eval(args.arg)
else:
    success = None

sys_exit(logger, NAME, args.task, success)
