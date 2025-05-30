import os

from bluer_objects import file, README

from bluer_flow import NAME, VERSION, ICON, REPO_NAME
from bluer_flow.workflow.README import items as workflow_items
from bluer_flow.workflow.patterns import list_of_patterns


def build():
    return README.build(
        items=workflow_items,
        cols=len(list_of_patterns()) + 1,
        path=os.path.join(file.path(__file__), ".."),
        ICON=ICON,
        NAME=NAME,
        VERSION=VERSION,
        REPO_NAME=REPO_NAME,
    )
