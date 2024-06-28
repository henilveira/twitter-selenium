# TwitterBot - Bot de Cotação do Dólar

**TwitterBot** é um projeto Python desenvolvido para postar automaticamente a cotação do dólar no Twitter. O bot utiliza o Selenium para automação do navegador e é estruturado com orientação a objetos. Ele obtém a cotação do dólar a partir de uma API e posta o valor em uma conta do Twitter.

## Funcionalidades

- Obtém a cotação atual do dólar a partir de uma API.
- Faz login no Twitter usando Selenium.
- Posta a cotação do dólar na conta do Twitter.
- Estruturado com orientação a objetos para facilitar a manutenção e a expansão.

## Requisitos

- Python 3.x
- Selenium
- Webdriver do navegador (ChromeDriver, GeckoDriver, etc.)
- Conta no Twitter para postar as atualizações
- Biblioteca `requests` para chamadas de API

## Instalação

1. Clone o repositório do projeto:
    ```sh
    git clone https://github.com/imrickss/python-selenium.git
    ```
2. Navegue até o diretório do projeto:
    ```sh
    cd TwitterBot
    ```
3. Instale as dependências necessárias:
    ```sh
    pip install -r requirements.txt
    ```

4. Baixe o webdriver do navegador de sua escolha e adicione-o ao PATH do seu sistema.

## Configuração

Crie um arquivo `.env` no diretório raiz do projeto com as seguintes informações:

