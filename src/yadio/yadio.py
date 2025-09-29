import httpx
from typing import Dict, Any

class YadioApi:
    """SDK simple para la API de Yadio"""

    BASE_URL = "https://api.yadio.io/"

    @classmethod
    def _request(cls, endpoint: str) -> Dict[str, Any]:
        url = f"{cls.BASE_URL}{endpoint}"
        response = httpx.get(url, timeout=5)
        response.raise_for_status()
        return response.json()

    @classmethod
    def ping_server(cls) -> Dict[str, Any]:
        """
Checks the server status.
       
        """
        return cls._request("ping")

    @classmethod
    def get_rate(cls, quote: str, base: str) -> Dict[str, Any]:
        """Returns the current exchange rate for a specific currency pair."""
        return cls._request(f"rate/{quote}/{base}")

    @classmethod
    def get_exrates(cls, currency: str = "USD") -> Dict[str, Any]:
        """Retrieves the current foreign exchange rates, using USD as the default base currency."""
        return cls._request(f"exrates/{currency}")

    @classmethod
    def get_currencies(cls) -> Dict[str, Any]:
        """Returns a list of all available currencies."""
        return cls._request("currencies")

    @classmethod
    def get_convert(cls, amount: float, currency_from: str, currency_to: str) -> Dict[str, Any]:
        "Converts a specified amount from a source currency to a target currency."
        return cls._request(f"convert/{amount}/{currency_from}/{currency_to}")


