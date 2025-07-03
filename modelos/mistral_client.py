import requests
import os
class MistralClient:
    def __init__(self):
        self.api_url = "https://api.together.xyz/v1/chat/completions"
        self.api_key = os.environ.get("TOGETHER_API_KEY")

    def chat(self, system_prompt: str, user_prompt: str) -> str:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        }
        response = requests.post(self.api_url, headers=headers, json=data)
        if response.ok:
            return response.json()["choices"][0]["message"]["content"]
        else:
            raise Exception("Error al consultar el modelo")
