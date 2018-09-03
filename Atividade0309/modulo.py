#coding:utf-8



def soma(n1, n2):
    print(n1)
    print(n2)
    return n1 + n2

def subtracao(n1, n2):
    return n1 - n2

def multiplicacao(n1, n2):
    return n1 * n2

def divisao(n1, n2):
    return n1/n2

def realizarOperacao(jsonRequest, valor1, valor2):
    ops = {'+': soma, '-': subtracao, '/':divisao, '*': multiplicacao}

    return ops[jsonRequest["op"]](valor1, valor2)
