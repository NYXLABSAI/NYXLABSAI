from abc import ABC, abstractmethod
from datetime import datetime
from app.utils.logger import log


class BaseAgent(ABC):
    """
    Abstract base class for NYXLABSAI agents.
    Defines the core structure for any AI agent (e.g., TraderAgent, SentimentAgent).
    """

    def __init__(self, name: str = "UnnamedAgent"):
        self.name = name
        log(f"{self.name} initialized.")

    def start(self):
        log(f"{self.name} started at {datetime.now()}")
        self.setup()
        self.run()
        self.teardown()

    @abstractmethod
    def setup(self):
        """
        Prepare the agent (e.g., load models, connect to APIs).
        """
        pass

    @abstractmethod
    def run(self):
        """
        Core logic loop (e.g., fetch data, predict, take action).
        """
        pass

    @abstractmethod
    def teardown(self):
        """
        Clean up resources (e.g., close connections, flush logs).
        """
        pass
