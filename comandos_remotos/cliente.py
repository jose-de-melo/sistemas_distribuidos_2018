#coding utf-8

import socket

porta = 17017
host = '127.0.0.1'

socketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

dest = (host, porta)

socketTCP.connect(dest)

while True:
    print("\nDigite o comando a ser executado: ")
    comando = input()
    socketTCP.send(comando.encode('utf-8'))
    saidaComando = socketTCP.recv(1024).decode()
    print('\n' + saidaComando)

    if comando == 'exit':
        socketTCP.close()
        break
