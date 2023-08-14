from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import requests

servico = Service(executable_path=r'C:\Users\Administrator\Documents\Python\Selenium\chromedriver.exe')
navegador = webdriver.Chrome(service=servico)

requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
requisicao_dic = requisicao.json()

cotacao_dolar = requisicao_dic['USDBRL']['bid']

cotacao_msg = 'COTAÇÃO ATUAL DÓLAR \nDÓLAR: '+cotacao_dolar

class TwitterBot:
    def __init__(self,usuario, senha, tweet):
        self.usuario = usuario
        self.senha = senha
        self.tweet = tweet
        self.path = Service(executable_path=r'C:\Users\Administrator\Documents\Python\Selenium\chromedriver.exe')
        self.bot = webdriver.Chrome(service=servico)

    def login(self): 
        bot = self.bot
        bot.get('https://twitter.com/home')
        time.sleep(3)
        usuario = bot.find_element('xpath', '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        usuario.send_keys(self.usuario)
        usuario.send_keys(Keys.RETURN)
        time.sleep(1)
        senha = bot.find_element('xpath', '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        senha.send_keys(self.senha)
        senha.send_keys(Keys.RETURN)
        time.sleep(5)

#//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a
    def post(self):
        bot = self.bot
        tweet_btn = bot.find_element('xpath', '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a').click()
        time.sleep(2)
        tweet = bot.find_element('xpath', '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div')
        tweet.send_keys(self.tweet)
        postar = bot.find_element('xpath', '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]')
        postar.click()
        



ed = TwitterBot('@anyonerickss', 'hsa#1602', cotacao_msg)
ed.login()
ed.post()