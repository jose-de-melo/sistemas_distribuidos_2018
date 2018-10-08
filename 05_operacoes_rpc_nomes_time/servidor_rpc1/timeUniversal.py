from datetime import datetime, timedelta
import requests
import time
import json

url = 'http://worldclockapi.com/api/json/utc/now'
nome_arquivo = 'difTime.txt'

def get_time():
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()

    seconds = float(conteudo)

    difTime = timedelta(seconds=seconds)
    dataAtual = datetime.now() - difTime

    return str(dataAtual)


def atualizaTempo():
    while True:
        get_tempo_universal()
        time.sleep(300)

def get_tempo_universal():
    try:
        r = requests.get(url)
        json_response = json.loads(r.text)

        date = datetime.strptime(json_response['currentDateTime'], "%Y-%m-%dT%H:%MZ")

        # Ajustando a hora para o UTC atual do Brasil (GMT-3)
        date = date - timedelta(hours=3)
        # Calculando a diferença entre a hora/data do sistema com a recebida da API
        diferenca = datetime.now() - date

        seconds = diferenca.total_seconds()

        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write(str(seconds))
    except:
        return
