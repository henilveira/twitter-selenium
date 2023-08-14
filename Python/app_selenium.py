from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import datetime
import requests

servico = Service(executable_path=r'C:\Users\henrique_ataide\Documents\Python\chromedriver.exe')
navegador = webdriver.Chrome(service=servico)

try:
    requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']

    navegador.get('https://twitter.com/home')
    input('digite algo')

finally:
    navegador.quit()

