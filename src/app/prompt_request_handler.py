from app import RequestHandler
import requests

class PromptHandler(RequestHandler):
    def __init__(self, request, port, prompt, url, stream, model='llama3.2'):
        super().__init__(request, port)
        self._prompt = prompt
        self._model = model
        self._url = url
        self._stream = stream

    def handler(self):
        response = requests.post(
            self._url,
            json={
                "prompt": self._prompt,
                "model": self._model,
                "port": self._port,
                "stream": self._stream
            },
            stream=self._stream
        )
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    # def __str__(self):
    #     return f"PromptHandler(prompt={self._prompt}, model={self._model}, url={self._url}, stream={self._stream})"

    def response_iterable(self):
        response_lines = self.handler()
        for line in response_lines.iter_lines():
            if line:
                yield line.decode('utf-8')