#coding:utf-8

import socket
import modulo as m
import json


PORTA = 19001

def main():
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind(('', PORTA))
    serverSocket.listen(1)

    while True:
        print('Servidor ouvindo na porta 19000....')

        con, addr = serverSocket.accept()

        con.settimeout(60)

        request = con.recv(1024).decode('utf-8')

        jsonRequest = json.loads(request)

        valor1 = int(jsonRequest["valor1"])
        valor2 = int(jsonRequest["valor2"])

        resultado = m.realizarOperacao(jsonRequest, valor1, valor2)

        resultado = str(resultado)

        con.send(resultado.encode('utf-8'))

if __name__ == '__main__':
    main()
