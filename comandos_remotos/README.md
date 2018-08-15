Executando comandos remotamente usando Python
===

O programa consiste em executar comandos de terminal remotamente. Isso foi feito usando a linguagem *Python* . 
Funciona da seguinte forma:
  
  * O cliente digita o comando a ser executado na parte cliente do programa.
  * O programa verifica o comando, envia o comando para o servidor executar e espera pela resposta do servidor. 
  * O servidor, então, executa o comando recebido e envia a saída gerada pelo comando ao cliente que solicitou
  a execução do comando. 
  * O cliente exibe a saída recebida do servidor
  * Se o comando fornecido for ``exit``, fecha a conexão com o servidor e finaliza a execução do programa. Se não for, o programa
  continua sua execução solicitando um novo comando a ser executado.
