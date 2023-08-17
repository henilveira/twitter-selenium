from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import requests

servico = Service(executable_path=r'C:\Users\Administrator\Documents\Python\Selenium\chromedriver.exe')
navegador = webdriver.Chrome(service=servico)

requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL') #API DE COTAÇÃO
requisicao_dic = requisicao.json() #PEGAR A API

cotacao_dolar = requisicao_dic['USDBRL']['bid'] #REQUISITAR VALOR DE COMPRA DO DOLAR EM BRL

cotacao_msg = 'COTAÇÃO ATUAL DÓLAR \nDÓLAR: '+cotacao_dolar #MENSAGEM DO TWEET

class TwitterBot:
    def __init__(self,usuario, senha, tweet): #DECLARAR AS VARIAVEIS VAZIAS
        self.usuario = usuario
        self.senha = senha
        self.tweet = tweet
        self.path = Service(executable_path=r'C:\Users\Administrator\Documents\Python\Selenium\chromedriver.exe') #LOCALIZAR DRIVER
        self.bot = webdriver.Chrome(service=servico)

    def login(self): 
        bot = self.bot
        bot.get('https://twitter.com/home') #PÁGINA QUE VAI SER ACESSADA
        time.sleep(3)
        usuario = bot.find_element('xpath', '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input') #SELECIONAR INPUT USUARIO
        usuario.send_keys(self.usuario) #ENVIAR AS INFORMAÇÕES DE USUÁRIO
        usuario.send_keys(Keys.RETURN) #ENTER PARA ENTRAR SEGUIR AO PROXIMO PASSO
        time.sleep(1)
        senha = bot.find_element('xpath', '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input') #SELECIONAR INPUT DE SENHA
        senha.send_keys(self.senha) #ENVIAR A SENHA DECLARADA NA CLASSE
        senha.send_keys(Keys.RETURN) #ENTER PARA ENTRAR COM A CONTA
        time.sleep(5)

    def post(self):
        bot = self.bot
        tweet_btn = bot.find_element('xpath', '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a').click() #CLICAR NO BOTÃO DE TWEET
        time.sleep(2)
        tweet = bot.find_element('xpath', '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div') #INPUT DE TEXTO PARA TWEET
        tweet.send_keys(self.tweet) #COLOCAR O QUE VAI NO TWEET
        postar = bot.find_element('xpath', '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]') #ACHAR O BOTAO DE POST
        postar.click() #TUITAR FINALIZADO!
        



hs = TwitterBot('@usuario', 'senha', cotacao_msg) #@usuario(COLOQUE SEU USUARIO OU EMAIL DO TWITTER), senha(COLOQUE SUA SENHA), cotacao_msg(MENSAGEM DE COTAÇÃO ATUAL)
hs.login() #INICIAR LOGIN
hs.post() #INICIAR POST