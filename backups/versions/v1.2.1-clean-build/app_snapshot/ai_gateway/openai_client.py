from app.core.settings import settings

class OpenAIClient:
    def __init__(self):
        self.model = 'gpt-5'

openai_client = OpenAIClient()
