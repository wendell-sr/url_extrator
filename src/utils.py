import requests
from urllib.parse import urlparse
from urllib.robotparser import RobotFileParser

def fetch_page(url: str) -> str:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    return response.text

def is_allowed(url: str, user_agent: str = "*") -> bool:
    parsed = urlparse(url)
    robots_url = f"{parsed.scheme}://{parsed.netloc}/robots.txt"
    rp = RobotFileParser()
    try:
        rp.set_url(robots_url)
        rp.read()
    except Exception:
        # Em caso de falha ao ler o robots.txt, permitir acesso para evitar bloqueios indevidos.
        return True
    return rp.can_fetch(user_agent, url)
