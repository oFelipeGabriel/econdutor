import requests
import urllib.request
import os
import json
#faz web scraping do site
from bs4 import BeautifulSoup as bs
resp = requests.get('https://econdutorcfc.com.br')
soup = bs(resp.content,'html.parser')

#prepara json
depoimentos = {}
depoimentos['depo'] = []
for divs in soup.find_all("div", class_= "depoimento"):
    text = divs.find_all('div', class_='dep-texto')
    local = divs.find_all('div', class_='dep-local')
    #inclui dados de cada depoimento no json
    depoimentos['depo'].append({
        'mensagem': text[0].getText(),
        'local': local[0].getText().strip()
        })
#salva em arquivo
with open('depoimentos.json', 'w') as outfile:  
    json.dump(depoimentos, outfile, ensure_ascii=False, indent=4)

#cria pasta para salvar imagens das autoescolas
if not os.path.exists('econdutor'):
    os.mkdir('econdutor')

#percorre imagens para serem salvas
for div in soup.find_all('div', class_='logo-parceiro'):
    file = div['style'].replace(' background-image: url(', '').replace(');', '')
    print(file.split('/')[-1])
    #salva imagem
    urllib.request.urlretrieve(file, "econdutor/"+file.split('/')[-1])

