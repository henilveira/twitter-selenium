# TwitterBot - Bot de Cotação do Dólar

**TwitterBot** é um projeto Python desenvolvido para postar automaticamente a cotação do dólar no Twitter. O bot utiliza o Selenium para automação do navegador e é estruturado com orientação a objetos. Ele obtém a cotação do dólar a partir de uma API e posta o valor em uma conta do Twitter.

## Funcionalidades

- Obtém a cotação atual do dólar a partir de uma API.
- Faz login no Twitter usando Selenium.
- Posta a cotação do dólar na conta do Twitter.
- Utiliza variáveis de ambiente para armazenar credenciais sensíveis.

## Requisitos

- Python 3.x
- Selenium
- Webdriver Manager
- Webdriver do navegador (ChromeDriver)
- Conta no Twitter para postar as atualizações
- Biblioteca `requests` para chamadas de API
- Biblioteca `python-dotenv` para carregar variáveis de ambiente

## Instalação

1. Clone o repositório do projeto:
    ```sh
    git clone https://github.com/imrickss/TwitterBot.git
    ```
2. Navegue até o diretório do projeto:
    ```sh
    cd TwitterBot
    ```
3. Crie e configure o arquivo `.env`:
    ```plaintext
    TWITTER_USERNAME=seu_usuario
    TWITTER_PASSWORD=sua_senha
    DOLLAR_API_URL=https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL
    ```
4. Instale as dependências necessárias:
    ```sh
    pip install -r requirements.txt
    ```
5. Baixe o ChromeDriver e configure o caminho no `main.py`.

## Uso

1. Execute o script principal `main.py` para iniciar o bot:
    ```sh
    python main.py
    ```
