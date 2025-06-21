from app.prompt_request_handler import PromptRequestHandler
from agents.model import (InitalPrompt)
class Agent:
    def __init__(self, model='llama3.2'):
        self._model = model
        self._port = 11434
        self._url = f"http://localhost:{self._port}/api/generate"
        self.agent = PromptRequestHandler(InitalPrompt, self._model, self._url, True)

    def get_response(self, prompt, url, stream=False):
        response = self.agent.handle(prompt, url, stream)
        return response