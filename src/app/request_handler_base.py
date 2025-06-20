class RequestHandler:
    def __init__(self, request, port):
        self._request = request
        self._port = port

    @property
    def handle(self):
        # Process the request here
        return f"Request handled: {self.request}"