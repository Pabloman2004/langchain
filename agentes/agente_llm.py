from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool

from modelos.mistral_langchain_wrapper import MistralLangChainWrapper
from herramientas.clima import obtener_tiempo_actual

# Definir la función que actuará como herramienta
def consultar_clima(ciudad: str) -> str:
    return obtener_tiempo_actual(ciudad)

class AgenteLLM:
    def __init__(self):
        # Instanciamos el LLM como antes
        llm = MistralLangChainWrapper()

        # Definimos la herramienta para el clima
        tool_clima = Tool(
            name="ConsultaTiempo",
            func=consultar_clima,
            description=(
                "Devuelve el clima actual de una ciudad española. "
                "Usa esta herramienta cuando el usuario pregunte por el clima, temperatura, si va a llover, etc."
            )
        )

        # Creamos el agente que puede usar herramientas
        self.agente = initialize_agent(
            tools=[tool_clima],
            llm=llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=True,
            handle_parsing_errors=True
        )


    def responder(self, pregunta: str) -> str:
        return self.agente.run(pregunta)

