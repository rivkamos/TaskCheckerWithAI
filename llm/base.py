# llm/base.py
from abc import ABC, abstractmethod

class LLMClient(ABC):

    @abstractmethod
    def complete(self, prompt: str) -> str:
        pass
"""Base LLM client module."""