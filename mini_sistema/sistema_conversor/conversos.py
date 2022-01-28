import requests
import json

cotacao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
cotacao = cotacao.json()
cotacao_dolar = cotacao['USDBRL']['bid']

print(f'US$ {float(cotacao_dolar)}')
