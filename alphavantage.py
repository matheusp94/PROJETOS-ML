import pandas as pd
import requests

api_key = 'chave aqui'  # Obtenha gratuitamente no site
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=^GSPC&outputsize=full&apikey={api_key}&datatype=csv'

response = requests.get(url)
with open('SP500.csv', 'wb') as file:
    file.write(response.content)

dados = pd.read_csv('SP500.csv')
print(dados.head())
