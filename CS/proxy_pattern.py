import requests
from functools import lru_cache

class APIProxy:
    def __init__(self, base_url):
        self.base_url = base_url

    @lru_cache(maxsize=128)
    def get_data(self, endpoint):
        response = requests.get(f"{self.base_url}/{endpoint}")
        return response.json()

api_proxy = APIProxy("https://jsonplaceholder.typicode.com")
print(api_proxy.get_data("todos/1"))