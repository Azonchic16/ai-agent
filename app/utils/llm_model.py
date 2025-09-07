import os
from pathlib import Path
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage


class LlmModel:

    def __init__(self, api_key, model="mistral-large-latest"):
        self.llm_model = ChatMistralAI(model=model,
                                       api_key=api_key,
                                       max_retries=2)

    def do_req(self, req):
        messages = [HumanMessage(content=req)]
        response = self.llm_model.invoke(messages)
        return response.content