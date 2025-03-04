from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
from src import utils
import concurrent.futures

def extract_urls(main_url: str, ignore_robots: bool = False) -> dict:
    # Verifica permissão no robots.txt somente se ignore_robots estiver desativado
    # if not ignore_robots and not utils.is_allowed(main_url):
    #     return {"error": "Acesso desabilitado pelo robots.txt"}
    
    try:
        content = utils.fetch_page(main_url)
    except Exception as e:
        return {"error": f"Falha ao acessar a URL principal: {e}"}
    
    soup = BeautifulSoup(content, "html.parser")
    all_links = set()
    
    # Extração de links do conteúdo principal
    for tag in soup.find_all("a"):
        href = tag.get("href")
        if href:
            full_url = urljoin(main_url, href)
            all_links.add(full_url)

    # Categorização: interna vs. externa
    parsed_main = urlparse(main_url)
    internal = set()
    external = set()
    for link in all_links:
        parsed_link = urlparse(link)
        if parsed_link.netloc == parsed_main.netloc:
            internal.add(link)
        else:
            external.add(link)

    # Rastreamento adicional: para cada link interno, extrai mais links (crawling em profundidade 2)
    additional_internal = set()
    def process_internal(internal_url):
        if not ignore_robots and not utils.is_allowed(internal_url):
            return set()
        try:
            page = utils.fetch_page(internal_url)
            s = BeautifulSoup(page, "html.parser")
            links = set(urljoin(internal_url, a.get("href")) for a in s.find_all("a") if a.get("href"))
            return {link for link in links if urlparse(link).netloc == parsed_main.netloc}
        except Exception:
            return set()

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(process_internal, link): link for link in internal}
        for future in concurrent.futures.as_completed(futures):
            additional_internal.update(future.result())

    all_internal = list(internal.union(additional_internal))
    return {
        "main_url": main_url,
        "internal_links": sorted(all_internal),
        "external_links": sorted(external)
    }
