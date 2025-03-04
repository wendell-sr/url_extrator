from fastapi import FastAPI, HTTPException
from src import extractor

app = FastAPI(title="Extrator de URLs", description="API para extração e categorização de links")

@app.get("/", include_in_schema=False)
async def index():
    return {"message": "Bem-vindo à API de Extração de URLs. Use o endpoint /extract para iniciar a extração."}

@app.get("/extract")
async def extract(url: str, ignore_robots: bool = False):
    result = extractor.extract_urls(url, ignore_robots=ignore_robots)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result
