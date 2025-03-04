#!/usr/bin/env python
import argparse
import json
from src import extractor
import uvicorn
from src.api import app as api_app

def main_cli():
    parser = argparse.ArgumentParser(description="Extrator de URLs")
    parser.add_argument("--url", type=str, help="URL para extrair links")
    parser.add_argument("--api", action="store_true", help="Executa o servidor da API")
    args = parser.parse_args()

    if args.api:
        print("Executando API em http://127.0.0.1:8000")
        uvicorn.run(api_app, host="127.0.0.1", port=8000)
    elif args.url:
        result = extractor.extract_urls(args.url)
        output_file = "output.json"
        with open(output_file, "w") as f:
            json.dump(result, f, indent=4)
        print(f"Extração concluída. Resultados salvos em {output_file}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main_cli()
