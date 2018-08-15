Executando comandos remotamente usando Python
===

O programa consiste em executar comandos de terminal remotamente. Isso foi feito usando a linguagem *Python* . 
Funciona da seguinte forma:
  
  * O cliente digita o comando a ser executado na parte cliente do programa.
  * O programa verifica o comando, caso o comando seja ``exit``, fecha a conexão e finaliza a execução do programa. 
  Caso não seja, envia o comando para o servidor executar e espera pela resposta do servidor
  * O servidor, então, executa o comando recebido e envia a saída gerada pelo comando de volta ao cliente que solicitou
  a execução do comando.
  * Por fim, o cliente exibe a saída recebida do servidor
