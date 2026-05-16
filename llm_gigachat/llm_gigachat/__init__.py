import requests
import llm
from llm import Model
import urllib3
import uuid

urllib3.disable_warnings()


class GigaChatModel(Model):
    model_id = "gigachat"

    def _get_token(self):

        auth_key = llm.get_key("gigachat")

        url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"

        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json",
            "RqUID": str(uuid.uuid4()),
            "Authorization": f"Basic {auth_key}"
        }

        data = {
            "scope": "GIGACHAT_API_PERS"
        }

        resp = requests.post(
            url,
            headers=headers,
            data=data,
            verify=False
        )

        resp.raise_for_status()

        return resp.json()["access_token"]

    def execute(self, prompt, stream=False, response=None, conversation=None):

        token = self._get_token()

        url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"

        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        data = {
            "model": "GigaChat",
            "messages": [
                {
                    "role": "user",
                    "content": str(prompt)
                }
            ],
            "temperature": 0.7,
            "max_tokens": 2000,
            "stream": False
        }

        resp = requests.post(
            url,
            json=data,
            headers=headers,
            verify=False
        )

        resp.raise_for_status()

        result = resp.json()["choices"][0]["message"]["content"]

        yield result


@llm.hookimpl
def register_models(register):
    register(GigaChatModel())