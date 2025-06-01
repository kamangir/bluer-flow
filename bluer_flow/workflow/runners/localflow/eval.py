from blueness import module

from bluer_flow import NAME
from bluer_flow.logger import logger


NAME = module.name(__file__, NAME)


def eval(arg: str) -> bool:
    logger.info(f"{NAME}.eval: arg={arg}")
    return True
