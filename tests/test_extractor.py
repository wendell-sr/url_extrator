from src import extractor, utils

# Conteúdo HTML de exemplo para testes
SAMPLE_HTML = """
<html>
  <body>
    <a href="https://example.com/interno">Link Interno Absoluto</a>
    <a href="/subpagina">Link Interno Relativo</a>
    <a href="https://external.com/">Link Externo</a>
  </body>
</html>
"""

# Função fake para simular o fetch_page retornando o HTML de exemplo
def fake_fetch_page(url):
    return SAMPLE_HTML

# Função fake para is_allowed que sempre retorna True
def fake_is_allowed(url, user_agent="*"):
    return True

def test_extract_urls(monkeypatch):
    monkeypatch.setattr(utils, "fetch_page", fake_fetch_page)
    monkeypatch.setattr(utils, "is_allowed", fake_is_allowed)
    
    main_url = "https://example.com"
    result = extractor.extract_urls(main_url)
    
    # Verifica se os links internos e externos foram extraídos e categorizados corretamente.
    internal_links = result.get("internal_links", [])
    external_links = result.get("external_links", [])
    
    # Os links internos devem incluir o link absoluto e o relativo (normalizado)
    assert "https://example.com/interno" in internal_links
    assert "https://example.com/subpagina" in internal_links
    
    # O link externo deve ser classificado como externo
    assert "https://external.com/" in external_links
