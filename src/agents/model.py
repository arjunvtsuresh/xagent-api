from dataclasses import dataclass
from enum import Enum

class InitalPrompt(Enum):
    """
    Enum for initial prompts used by the agent.
    """
    DEFAULT = "Hi How can I help you today?"
    CUSTOM = "What can I do for you today?"