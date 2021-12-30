import pandas as pd
import requests
import awswrangler as wr


#fazendo a requisição na API
CSV_URL = 'https://queimadas.dgi.inpe.br/api/focos/'
response = requests.get(CSV_URL)
response.raise_for_status()

data = response.json()

#trabalhando as colunas
df = pd.json_normalize(data)
df.to_csv('queimadas.csv')

#upload to s3
wr.s3.to_csv(df=df, path='s3://data-queimadas/folder-queimadas/queimadas.csv')