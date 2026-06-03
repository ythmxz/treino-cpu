# Hiper-Cubo (CPU)

Limite de tempo: 1 segundo

## Problema:

Um Hiper-Cubo é um cubo no espaço vetorial de dimensão $N$. As figuras abaixo mostram os cubos e suas arestas nos espaços $N$ = 0 (uma abstração matemática já que todo o espaço vetorial está restrito a um ponto), $N$ = 1 (o espaço linear), uma reta, $N$ = 2 (o espaço bidimensional), um quadrado, $N$ = 3 (o espaço tridimensional), o cubo tradicional, $N$ = 4 . . .

Sobre os hipercubos há uma curiosidade, um hipercubo de dimensão $N$ tem seus vértices classificados, ou enumerados, a partir de um conjunto de $N$ bits como podemos ver na figura acima. Em especial, as arestas, desenhadas por uma linha contínua, são representadas pela ligação de 2 vértices, que distam entre si por apenas 1 bit. As diagonais principais, desenhadas por linhas pontilhadas (omitida para $N$ = 4), são representadas pela ligação de 2 vértices onde todos os bits são trocados. As demais diagonais secundárias, terciárias, ... possui a distância entre os bits dos vértices no intervalo (1, $n$) bits. A você foi pedido, dada a dimensão $N$ do espaço (0 <= $N$ <= 20) que indique quantos vértices, quantas arestas, quantas diagonais principais e quantas diagonais não principais o hipercubo possui.

## Entrada:

Cada caso de teste é dado por um número inteiro $N$, 0 <= $N$ <= 20. Os casos de teste terminam com as entradas.

## Saída:

Em cada linha, para cada caso de teste, deve ter 4 números indicando respectivamente: O número de vértices do hipercubo, o número de arestas, o número de diagonais principais e o número de diagonais não principais.

| Exemplo de entrada: | Saída do exemplo de entrada: |
| ------------------- | ---------------------------- |
| 0                   | 1 0 0 0                      |
| 1                   | 2 1 0 0                      |
| 2                   | 4 4 2 0                      |
| 3                   | 8 12 4 12                    |
| 4                   | 16 32 8 80                   |
