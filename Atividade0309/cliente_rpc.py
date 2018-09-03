#coding:utf-8

import socket
import json

PORTA = 25900
servidor = '10.3.1.21'

def soma(n1, n2):
    return montarEnviarOperacao({"op":"+", "n1": n1, "n2": n2})

def subtracao(n1, n2):
    return montarEnviarOperacao({"op":"-", "n1": n1, "n2": n2})

def multiplicacao(n1, n2):
    return montarEnviarOperacao({"op":"*", "n1": n1, "n2": n2})

def divisao(n1, n2):
    return montarEnviarOperacao({"op":"/", "n1": n1, "n2": n2})

def montarEnviarOperacao(operacaoEmJSON):
    socketCliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketCliente.settimeout(10)
    socketCliente.connect((servidor, PORTA))
    socketCliente.send(json.dumps(operacaoEmJSON).encode('utf-8'))
    resp = socketCliente.recv(2048).decode('utf-8')

    return resp
