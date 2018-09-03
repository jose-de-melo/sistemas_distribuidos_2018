#coding:utf-8

import cliente_rpc as c

def main():
    print('A soma de 10 e 20 é {}'.format(c.soma(10,20)))
    print('A subtracao de 10 e 20 é {}'.format(c.subtracao(10,20)))
    print('A divisao entre 5 e 0 é {}'.format(c.divisao(5,0)))
    print('A multiplicao entre 10 e 20 é {}'.format(c.multiplicacao(10,20)))

if __name__ == '__main__':
    main()
