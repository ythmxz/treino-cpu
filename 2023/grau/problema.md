# Um Grau no Asfalto (CPU)

Limite de tempo: 1 segundo

## Problema:

A cidade de Cafundós do Porto Úmido, carinhosamente apelidada de CPU tem uma característica semelhante à turística cidade de Canavieiras/BA: seu prefeito ́e um simpático motociclista. A cidade possui vários distritos que são interligados todos por estrada de chão. O prefeito, agora com um Harlão de seus sonhos, percebeu que não ́e tão agradável por a moto na estrada de chão. Ele tomou a decisão de que irá dar um grau na cidade asfaltando as estradas que ligam os vários distritos, no entanto, ele quer economizar. Ou seja, ́e necessário que de um distrito para qualquer outro, exista um caminho asfaltado, mas isto tem de acontecer asfaltando o mínimo necessário, nem todas as estradas serão asfaltadas. Ele pediu para você para que dado o conjunto de estradas e o comprimento de cada estrada, que faça um algoritmo para determinar quantos quilômetros precisam ser asfaltados no mínimo.

## Entrada:

O caso de teste começa com dois números $N$ e $M$ indicando o número de Distritos (0 < $N$ <= 100), que numeramos de 1 a $N$, para evitar o uso de nomes, e o número de estradas que ligam estes distritos ($N$ − 1 <= $M$ < $N^2$). Em seguida são $M$ linhas com as seguintes informações: dois números $A$ e $B$ indicando dois distritos (0 < $A$ <= $B$ <= $N$); K, (0 < $K$ <= 100) a distância em quilômetros da estrada que liga os distritos $A$ e $B$.

## Saída:

A saída deve conter em uma única linha um inteiro indicando o tanto de quilômetros que deve ser asfaltado, no mínimo, para ter todos os distritos ligados por um caminho asfaltado.

| Exemplo de entrada: | Saída do exemplo de entrada: |
| ------------------- | ---------------------------- |
| 11 15               | 17                           |
| 9 8 4               |                              |
| 10 7 2              |                              |
| 10 11 3             |                              |
| 3 4 3               |                              |
| 4 5 1               |                              |
| 11 5 2              |                              |
| 1 2 2               |                              |
| 2 10 4              |                              |
| 10 9 1              |                              |
| 7 11 1              |                              |
| 2 3 1               |                              |
| 3 11 2              |                              |
| 6 7 3               |                              |
| 6 11 4              |                              |
| 7 8 2               |                              |
