from langchain_core.language_models import SimpleChatModel
from langchain_core.messages import HumanMessage
from modelos.mistral_client import MistralClient
from pydantic import PrivateAttr

class MistralLangChainWrapper(SimpleChatModel):
    _client: MistralClient = PrivateAttr()

    def __init__(self):
        super().__init__()
        self._client = MistralClient()

    def _call(self, messages: list, **kwargs) -> str:
        user_message = next((m.content for m in messages if isinstance(m, HumanMessage)), "")
        system_message = "Eres un asistente útil que responde con claridad."
        return self._client.chat(system_message, user_message)

    @property
    def _llm_type(self) -> str:
        return "mistral_custom"
