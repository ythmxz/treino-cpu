# Ilhas Isoladas (CPU)

Limite de tempo: 1 segundo

## Problema:

Voltamos aos Estados Republicanos do BArbo-SErvo (ERBASE), infelizmente a natureza foi cruel e um grande maremoto derrubou várias das pontes. Principalmente pelo fato de que haviam sido construídas em um esquema fraudulento com as construtoras em uma época passada. As pontes não eram de prima qualidade e muitas delas ruíram. A grande preocupação é saber se alguma ilha ficou isolada, ou seja, se há ilhas que não tenham mais nenhuma ligação com qualquer outra. Pois estas é quem receberão os primeiros socorros. A você foi solicitado que, dadas as ligações entre as ilhas que restaram que fizesse um algoritmo para saber se há ilhas isoladas.

## Entrada:

A entrada consiste, na primeira linha, em dois valores: $N$, 1 <= $N$ <= 100 que representa o número de ilhas da ERBASE, as ilhas são numeradas para evitar o uso de nomes na indexação, e $M$, 0 <= $M$ <= ($N^2$ − $N$) / 2 que consiste na quantidade de pontes que restaram após a destruição, e em seguida são $M$ linhas contendo dois valores $a$ e $b$ 1 <= $a$, $b$ <= $N$, separados por um espaço em branco, sendo que $a$ $b$ são duas ilhas distintas ainda ligadas por uma ponte.

## Saída:

A saída deve conter em uma única linha para cada caso de teste um caractere 'S' indicando que há ilhas isoladas ou 'N' indicando que não há.

| Exemplo de entrada: | Saída do exemplo de entrada: |
| ------------------- | ---------------------------- |
| 11 14               | S                            |
| 9 8                 | N                            |
| 10 7                |                              |
| 10 11               |                              |
| 3 4                 |                              |
| 4 5                 |                              |
| 11 5                |                              |
| 2 10                |                              |
| 10 9                |                              |
| 7 11                |                              |
| 2 3                 |                              |
| 3 11                |                              |
| 6 7                 |                              |
| 6 11                |                              |
| 7 8                 |                              |
| 6 4                 |                              |
| 1 2                 |                              |
| 2 3                 |                              |
| 4 5                 |                              |
| 5 6                 |                              |
| 0 0                 |                              |
