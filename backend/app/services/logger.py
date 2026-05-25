
from loguru import logger

logger.add(
    "znoc.log",
    rotation="100 MB",
    retention="14 days",
    serialize=True
)
