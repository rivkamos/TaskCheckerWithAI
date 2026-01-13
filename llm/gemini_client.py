# llm/gemini_client.py
import google.generativeai as genai
from llm.base import LLMClient

class GeminiClient(LLMClient):
    def __init__(self, api_key: str, model: str = "gemini-2.5-flash"):
        genai.configure(api_key=api_key)
        self.model_name = model

    def complete(self, prompt: str) -> str:
        model = genai.GenerativeModel(
            model_name=self.model_name,
            system_instruction="אתה בודק פרויקטי תוכנה בצורה מדויקת"
        )
        
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                temperature=0,
                max_output_tokens=8192
            )
        )
        
        return response.text
"""Google Gemini LLM client module."""