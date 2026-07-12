import logging
import os


os.makedirs("output", exist_ok=True)

logging.basicConfig(
    filename="output/agentic_ai.log",
    level=logging.DEBUG,
    filemode="w",
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger()