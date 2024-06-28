from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import requests
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configurar o webdriver
servico = Service(executable_path=r'C:\Users\Administrator\Documents\Python\Selenium\chromedriver.exe')
navegador = webdriver.Chrome(service=servico)

# Obter a cotação do dólar da API
api_url = os.getenv('DOLLAR_API_URL')
requisicao = requests.get(api_url)
requisicao_dic = requisicao.json()

cotacao_dolar = requisicao_dic['USDBRL']['bid']
cotacao_msg = 'COTAÇÃO ATUAL DÓLAR \nDÓLAR: ' + cotacao_dolar

class TwitterBot:
    def __init__(self, usuario, senha, tweet):
        self.usuario = usuario
        self.senha = senha
        self.tweet = tweet
        self.path = Service(executable_path=r'C:\Users\Administrator\Documents\Python\Selenium\chromedriver.exe')
        self.bot = webdriver.Chrome(service=self.path)

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/login')
        time.sleep(3)
        usuario = bot.find_element('xpath', '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        usuario.send_keys(self.usuario)
        usuario.send_keys(Keys.RETURN)
        time.sleep(1)
        senha = bot.find_element('xpath', '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        senha.send_keys(self.senha)
        senha.send_keys(Keys.RETURN)
        time.sleep(5)

    def post(self):
        bot = self.bot
        tweet_btn = bot.find_element('xpath', '//*[@aria-label="Tweet"]').click()
        time.sleep(2)
        tweet = bot.find_element('xpath', '//*[@aria-label="Tweet text"]')
        tweet.send_keys(self.tweet)
        postar = bot.find_element('xpath', '//*[@data-testid="tweetButtonInline"]')
        postar.click()
        time.sleep(2)
        bot.quit()

# Obter credenciais do Twitter do arquivo .env
usuario = os.getenv('TWITTER_USERNAME')
senha = os.getenv('TWITTER_PASSWORD')

hs = TwitterBot(usuario, senha, cotacao_msg)
hs.login()
hs.post()
