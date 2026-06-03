# Frete Certo (CPU)

Limite de tempo: 1 segundo

## Problema:

A “Compras Por Oportunidade” também conhecida como CPU é uma rede varejista online. Ela tem lojas espalhadas em vários cantos do seu país de origem o “Estados Republicanos do BArbo-SErvos”que vamos apelidar de ERBASE. O ERBASE é um país insular, onde há pontes ligando as várias Ilhas-Estados. As pontes são de mão dupla e não possuem interseção, exceto nas ilhas. Não há grupos isolados de Ilhas, todas estão interligadas. O presidente recém eleito resolveu retomar vários impostos que haviam sido extintos, para bancar seu séquito, a exemplo do pedágio-ponte, todas pontes têm pedágios, nos dois sentidos. O fato é, a CPU quer oferecer o menor custo de frete para uma compra realizada, e este custo é basicamente o valor dos pedágios transpostos entre a saída do produto de uma ilha e a entrega na ilha do comprador. Temos então a lista de Ilhas-Estados do ERBASE e identificamos quais Ilhas-Estados possui sede da CPU. Temos também o conjunto de pontes e o valor do pedágio em cada ponte. Por fim, dada a ilha do comprador, e a lista de ilhas das unidades da CPU que possui o produto, queremos saber o menor custo do frete. A você foi pedido que criasse um algoritmo que aponte qual a unidade da CPU que terá o menor custo de frete para entrega do produto e o valor deste frete.

## Entrada:

O caso de teste começa com dois números $N$ e $M$ indicando o número de Ilhas-Estados (0 < $N$ <= 100), que numeramos de 1 a $N$, para evitar o uso de nomes, e o número de pontes que ligam estas Ilhas ($N$ − 1 <= $M$ < N2). Em seguida são $M$ linhas com as seguintes informações: dois números $A$ e $B$ indicando duas ilhas (0 < $A$ <= $B$ <= $N$); $P$, (0 < $P$ <= 100) o número de moedas-pedágio que é o custo para atravessar a ponte que liga as ilhas $A$ e $B$. Em seguida temos uma linha com $L$, (0 < $L$ <= $N$) o número de unidades da CPU na ERBASE, seguido de $L$ inteiros distintos no intervalo de 1 a $N$ indicando em quais ilhas há uma unidade da CPU. Por fim temos $Q$ (0 < $Q$ <= 100) o número de compras realizadas seguidas de $Q$ linhas com as seguintes informações: $C$, (0 < $C$ <= $N$) a ilha do comprador, $D$, (0 < $D$ <= $L$) o número de unidades que que possui o produto comprado e uma sequência de $D$ números que são um subconjunto dos $L$ valores, representando as unidades que possuem o produto. É garantido que somente uma unidade irá oferecer o menor custo de entrega.

## Saída:

A saída deve conter $Q$ linhas onde cada linha contém dois números, o número da ilha onde está a unidade da CPU que irá realizar a entrega e o custo em moedas-pedágio para a entrega.

| Exemplo de entrada: | Saída do exemplo de entrada: |
| ------------------- | ---------------------------- |
| 11 15               | 4 3                          |
| 9 8 4               | 6 5                          |
| 10 7 2              | 10 2                         |
| 10 11 3             | 4 0                          |
| 3 4 3               | 10 4                         |
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
| 4 1 10 4 6          |                              |
| 5                   |                              |
| 11 2 1 4            |                              |
| 8 3 6 4 1           |                              |
| 7 2 10 6            |                              |
| 4 3 1 6 4           |                              |
| 8 4 1 4 6 10        |                              |
