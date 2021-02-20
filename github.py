import requests
from pydantic.main import BaseModel


class Github:
    def search(self, text: str, per_page: int = 100):
        resp = requests.get(f'https://api.github.com/search/repositories?q={text}&per_page={per_page}',
                            headers={"Accept": "application/vnd.github.v3+json"})
        if resp.status_code == 200:
            return resp.json()
        return None


class Request(BaseModel):
    text: str