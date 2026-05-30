# DOIS DADOS

Limite de tempo: 1 segundo

## O Problema:

Trata-se de um jogo de dados, que se joga com dois dados, que se lançam sucessivamente, multiplicando-se sempre os números
de cada lance um pelo outro, até se atingir a pontuação de 300. Quem atingir o teto dos 300 pontos, com o menor número de
lances ganha. Neste jogo, os dobles (duas faces iguais) são sempre duplicados, ou seja, além da multiplicação de um número
pelo outro, o resultado ainda é dobrado. Com exceção do doble de 1, que é contado como perfazendo 30 pontos. Nesta versão
do jogo cada jogador pode lançar os dois dados 5 vezes, quem obtiver mais pontos ganha.

## Entrada:

A entrada começa com um número N (0 < N <= 10) o número de jogadores, numerados de 1 a N. Em seguida há N linhas
onde em cada linha está o i−ésimo jogador. Em cada linha há 5 conjunto de números: (a, b), separados por um espaço em
branco, onde 1 <= a, b <= 6 que são as faces dos dados de cada uma das 5 jogadas.

## Saída:

Na saída deve sair impresso na primeira linha: ”Pontos do ganhador: ”seguido dos pontos obtidos pelo campeão do jogo.
Na segunda linha a frase: ”Ganhador(es): ”, e após um espaço, os ganhadores (os jogadores que atingiram a pontuação
máxima), se houver mais de 1, separados por vírgula e espaço após a vírgula, em ordem crescente do número do jogador.

| Exemplo de entrada:           | Saída para o Exemplo de entrada: |
| ----------------------------- | -------------------------------- |
| 2                             | Pontos do ganhador: 84           |
| (1,2) (2,3) (3,4) (4,5) (5,6) | Ganhador(es): 2                  |
| (2,2) (3,3) (4,4) (3,3) (2,2) |                                  |
|                               |                                  |
| 2                             | Pontos do ganhador: 84           |
| (6,5) (2,5) (1,4) (5,2) (5,6) | Ganhador(es): 1, 2               |
| (2,2) (3,3) (4,4) (3,3) (2,2) |                                  |
