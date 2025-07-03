from modelos.mistral_client import MistralClient
from herramientas.clima import obtener_tiempo_actual
from datos.ciudades_es import CIUDADES_ESPANA

class AgenteBase:
    def __init__(self):
        self.modelo = MistralClient()

    def es_pregunta_sobre_el_clima(self, pregunta: str) -> bool:
        pregunta = pregunta.lower()
        palabras_clave = ["tiempo", "clima", "temperatura", "llueve", "lloverá", "viento", "hace calor"]
        return any(palabra in pregunta for palabra in palabras_clave)

    def extraer_ciudad(self, pregunta: str) -> str:
        pregunta = pregunta.lower()
        for ciudad in CIUDADES_ESPANA:
            if ciudad in pregunta:
                return ciudad
        return "Madrid"  # ciudad por defecto si no se encuentra ninguna

    def responder(self, pregunta_usuario: str) -> str:
        if self.es_pregunta_sobre_el_clima(pregunta_usuario):
            ciudad = self.extraer_ciudad(pregunta_usuario)
            return obtener_tiempo_actual(ciudad)
        else:
            system_prompt = "Eres un asistente útil que responde preguntas de forma clara."
            return self.modelo.chat(system_prompt, pregunta_usuario)


