from typing import List

from bluer_options.terminal import show_usage, xtra


def help_eval(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("type=<cpu|gpu>,verbose", mono=mono)

    return show_usage(
        [
            "localflow",
            "eval",
            f"[{options}]",
            "<command-line>",
        ],
        "<command-line> -> localflow",
        mono=mono,
    )


def help_list(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "localflow",
            "list",
        ],
        "list localflow jobs.",
        mono=mono,
    )


def help_start(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "localflow",
            "start",
        ],
        "start localflow",
        mono=mono,
    )


help_functions = {
    "eval": help_eval,
    "list": help_list,
    "start": help_start,
}
