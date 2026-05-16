import requests
import llm
from llm import Model


class AliceModel(Model):
    model_id = "alice"

    def execute(self, prompt, stream=False, response=None, conversation=None):

        api_key = llm.get_key("alice")

        folder_id = "b1ggjj2mf36ekuhsqgr1" # мой каталог

        url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"

        headers = {
            "Authorization": f"Api-Key {api_key}",
            "Content-Type": "application/json"
        }

        data = {
            "modelUri": f"gpt://{folder_id}/yandexgpt/latest",
            "completionOptions": {
                "stream": False,
                "temperature": 0.6,
                "maxTokens": 2000
            },
            "messages": [
                {
                    "role": "user",
                    "text": str(prompt)
                }
            ]
        }

        resp = requests.post(
            url,
            json=data,
            headers=headers
        )

        resp = requests.post(
            url,
            json=data,
            headers=headers
        )

        resp.raise_for_status()

        result = resp.json()["result"]["alternatives"][0]["message"]["text"]

        yield result


@llm.hookimpl
def register_models(register):
    register(AliceModel())