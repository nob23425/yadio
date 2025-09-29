import httpx
from typing import Dict

class YadioApi():

    def __init__(self):
        self.base_url= "https://api.yadio.io/"
    def _request(self, enpoint : str) -> Dict:
        url=f"{self.base_url}{enpoint}"
        requests= httpx.get(url)
        requests.raise_for_status()
        
        return requests.json()


    def ping_server(self):
        return self._request("ping")
    def get_convert(self, amount: float , currency_from : str , currency_to: str):
        return self._request(f"convert/{amount}/{currency_from}/{currency_to}")


cliente= YadioApi()

print(cliente.get_convert(1,"USD", "CUP"))