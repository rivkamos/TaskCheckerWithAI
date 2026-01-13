# llm/openai_client.py
from openai import OpenAI
from llm.base import LLMClient

class OpenAIClient(LLMClient):
    def __init__(self, api_key: str, model: str = "gpt-4o-mini"):
        self.client = OpenAI(api_key=api_key)
        self.model = model

    def complete(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "אתה בודק פרויקטי תוכנה בצורה מדויקת"},
                {"role": "user", "content": prompt}
            ],
            temperature=0
        )

        return response.choices[0].message.content
"""OpenAI LLM client module."""