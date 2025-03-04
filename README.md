# Documentação do Projeto de Extração de URLs

## 1. Introdução
Este projeto automatiza a extração de URLs a partir de uma URL principal, organizando e categorizando os links de forma estruturada. Com integração avançada e processamento otimizado, o sistema já está preparado para coletar, filtrar e apresentar dados, facilitando o uso pelos usuários e integrando com ferramentas externas como o Google LM Notebook.

## 2. Objetivo
O projeto busca:
- Mapear todas as URLs envolvidas em uma documentação.
- Estruturar os links de forma organizada e categorizada.
- Facilitar a extração e visualização do conteúdo relevante.
- Permitir a integração automática com ferramentas de machine learning e análise.
- Fornecer uma API para consulta remota dos dados extraídos.

## 3. Estrutura do Projeto
A estrutura modular do projeto facilita a escalabilidade e a manutenção:
```
URL_EXTRACTOR/
│── src/
│   ├── __init__.py
│   ├── extractor.py      # Lógica principal de extração e categorização
│   ├── utils.py          # Funções auxiliares e otimizações (controle de duplicidade, multithreading/async)
│── tests/
│   ├── __init__.py
│   ├── test_extractor.py # Casos de teste automatizados para validação do sistema
│── .gitignore
│── .python-version
│── main.py              # Ponto de entrada e execução inicial
│── pyproject.toml       # Configurações do projeto
│── README.md           # Documentação
```

## 4. Funcionalidades Implementadas
- **Coleta e Categorização de URLs**: A partir de uma URL inicial, o sistema extrai automaticamente todos os links internos, aplicando uma categorização que agrupa os links por tópicos e seções para facilitar a navegação e análise.
- **Filtragem de URLs**: Implementada filtragem avançada que exclui links duplicados e irrelevantes, garantindo dados limpos e precisos.
- **Exportação Estruturada dos Dados**: Geração automática de arquivos (JSON, CSV, etc.) com todas as informações extraídas e categorizadas.
- **Multithreading e Processamento Assíncrono**: Incorporadas técnicas para acelerar a coleta e processamento das URLs mesmo em grandes volumes de dados, otimizando performance.
- **Integração com Google LM Notebook**: Possibilidade de exportar imediatamente os dados para análise e treinamento em ambientes de machine learning.
- **API com FastAPI**: API REST implementada para consulta remota dos dados extraídos. A API já está integrada e pode ser acessada para recuperação e análise dos dados.
- **Interface Gráfica**: Uma interface gráfica foi implementada usando Tkinter para facilitar a interação do usuário, permitindo a entrada da URL principal e a visualização dos resultados de forma intuitiva.
- **Testes Automatizados e Tratamento de Erros**: A suíte de testes abrange diversos cenários de extração e filtragem, com tratamento robusto de erros e logs detalhados para monitoramento do sistema.

## 5. Tecnologias Utilizadas
- **Linguagem**: Python
- **Bibliotecas**:
  - `requests` para requisições HTTP
  - `BeautifulSoup` para parsing de HTML
  - `Scrapy` para extração avançada
  - `Pandas` para organização e exportação dos dados
  - `FastAPI` para disponibilização da API
  - `Uvicorn` para execução do servidor da API
- **Outras Tecnologias**:
  - Implementação de multithreading e processamento assíncrono para performance otimizada.
  - Interface web para interação com o usuário.

## 6. Fluxo de Execução
1. O usuário informa a URL principal via interface web ou linha de comando.
2. O sistema acessa a página, coletando e categorizando automaticamente todos os links internos.
3. As URLs são filtradas para remover duplicidades e irrelevâncias.
4. Os dados são estruturados e exportados em formatos adequados (JSON, CSV, etc.).
5. Os dados podem ser automaticamente enviados para ferramentas externas, como o Google LM Notebook.
6. A API permite consultas externas e análises remotas.

## 7. Requisitos

Para configurar e utilizar o aplicativo, é necessário ter a ferramenta UV instalada.

## 8. Instruções de Uso

Para executar o projeto, utilize os seguintes comandos:

```sh
uv run main.py
```

### Opções:

- `--url URL`: URL para extrair links
- `--api`: Executa o servidor da API
- `--gui`: Executa a interface gráfica

```sh
usage: main.py [-h] [--url URL] [--api] [--gui]

Extrator de URLs

options:
  -h, --help  show this help message and exit
  --url URL   URL para extrair links
  --api       Executa o servidor da API
  --gui       Executa a interface gráfica
```

Com as melhorias já implementadas, o projeto oferece uma solução completa e robusta para a extração e organização de URLs. A integração com ferramentas externas, o processamento otimizado e a interface amigável garantem que o sistema atenda de forma eficiente a diferentes demandas, desde a análise de grandes volumes de dados até a consulta remota via API.
