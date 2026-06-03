# Dominó Oculto (CPU)

Limite de tempo: 3 segundos

## Problema:

O jogo de dominó é viciante, tanto que até se inventam variantes do jogo, até mesmo para uma pessoa. Um exemplo é a paciência com Dominó Oculto. Ao jogador é sorteada N peças de dominó, e ele irá abrindo uma por uma de forma oculta, a primeira é colocada na mesa, sempre que encontra uma peça que caiba na mesa, seguindo a regra do jogo de dominó, esta deve ser colocada, quando não cabe, fica guardada como pedra na mão. As pedras nas mãos quando cabem devem também ser colocadas, antes da retirada da próxima pedra oculta. A principal dúvida é se a versão final que foi criada na mesa, após tomar todos os dominós ocultos é a maior possível. Vamos considerar a seguinte situação:

Em mãos - {3,5} {4,5}

Na mesa - {1,2} {2,6}

Próximos - {6,1}

Na sequência da jogada podemos ficar com 1 nas duas pontas ou 6 nas duas pontas. A jogada deve ser feita. Vamos considerar a que próxima peça fosse {3,6}, se tivéssemos ficado com 1 nas duas pontas, o jogo teria acabado com 3 peças na mesa e 3 nas mãos. Mas se tivéssemos feito 6 nas duas pontas, aí conseguiríamos encaixar a peça {3,6}, ficando com 3 e 6 nas pontas, aí encaixaria a peça {3,5}, ficando com 5 e 6 nas pontas e por fim a peça {4,5}, concluindo a jogada: 6 peças na mesa e nenhuma nas mãos. A você foi solicitado um algoritmo que retorne qual a maior sequência possível na mesa seguindo uma ordem de pedras ocultas.

## Entrada:

São vários casos de teste, cada caso de teste possui duas linhas, a primeira linha $N$,(0 < $N$ <= 28) o número de peças ocultas, e na segunda linha são $N$ pares de valores {$v_i$, $v_j$} separados por espaço, onde 0 <= $v$ <= 6 e cada par é único (não importando a ordem). Os casos de teste terminam com $N$ = 0, que não deve ser considerado.

## Saída:

Para cada caso de teste deve haver em uma linha exclusiva um número inteiro indicando a quantidade máxima de dominós que pode-se colocar na mesa.

| Exemplo de entrada:                 | Saída do exemplo de entrada: |
| ----------------------------------- | ---------------------------- |
| 6                                   | 6                            |
| {1,2} {3,5} {4,5} {2,6} {1,6} {3,6} | 1                            |
| 2                                   | 1                            |
| {3,4} {2,6}                         |                              |
| 1                                   |                              |
| {0,0}                               |                              |
| 0                                   |                              |
