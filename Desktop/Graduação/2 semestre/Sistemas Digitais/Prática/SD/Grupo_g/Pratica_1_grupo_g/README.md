--------- dados dos alunos do grupo G--------
nome: André Thiago Pfleger
matricula: 22200345

nome: Heryk dos Santos Barros
matricula: 19250116

--------------------------------------------------------------------------------------------------------------------------------------------------

#Circuito1: Mux4_1
Um circuito de um multiplexador de 4 entradas para 1 saída, feito com uma lógica de caso.

Simulação: O valor da saída do sistema torna-se uma das entradas em específico, dependendo da alteração dos bits do seletor.

--------------------------------------------------------------------------------------------------------------------------------------------------

#Circuito2: Demux1_4
Um circuito de um demultiplexador de 1 entrada para 4 saídas, feito usando case-when.

Simulação: Dependendo do input no seletor a entrada é redirecionada para uma saída específica.

--------------------------------------------------------------------------------------------------------------------------------------------------

#Circuito3: decoderbcd7seg_log
Um circuito de um decodificador em binário com 1 vetor de entrada de 4 bits e 7 saídas de 1 bit para display de 7 segmentos, feito usando lógica combinatória entre os bits da entrada para cada saída, baseando-se no mapa de Karnaugh.

Simulação: As ondas dos sinais de saída alteram-se individualmente conforme alterado o vetor de entrada do sistema.

--------------------------------------------------------------------------------------------------------------------------------------------------

#Circuito4: decoderbcd7seg_case
Um circuito de um decodificador em binário com 1 vetor de entrada de 4 bits e 1 vetor de saída com 7 bits para display de 7 segmentos, feito usando case-when.

Simulação: Há apenas um vetor de saída, o qual é gerado a partir do valor do vetor de entrada.

--------------------------------------------------------------------------------------------------------------------------------------------------

Obs. A utilização dos vetores e do case-when diminuiu consideravelmente o trabalho quando feito o arquivo de estímulos e a simulação.