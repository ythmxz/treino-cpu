# Autômato Zigue-Zague (CPU)

Limite de tempo: 1 segundo

## Problema:

Um autômato de fábrica foi construído para fazer dois tipos de movimento: avanço (uma única casa para a direita) e retrocesso (uma única casa para a esquerda).

O autômato sempre parte de um ponto inicial e deve retornar a esse ponto ao final de qualquer sequência de movimentos.

Seguindo da ilustração imediatamente acima, o primeiro movimento sempre deve ser para a direita, e o autômato não pode ser movimentado em um sentido mais vezes que no outro. Também seguindo da segunda ilustração, o espaço de movimentação do autômato é limitado àquele total de onze casas. A você foi solicitado para que, dada uma sequência de operações, indicar se ela é viável ou não.

## Entrada:

A entrada consiste de um conjunto de sequências de movimentos a serem executados pelo autômato, uma sequência em cada linha, sendo que as movimentações para a esquerda são representadas pela letra 'E', e as movimentações para a direita por 'D'. O máximo são 100.000 movimentações por sequência de operações do autômato. O final das sequências coincide com o final da entrada.

## Saída:

Para cada sequência de entrada deve haver em uma linha única a resposta 'S' ou 'N' indicando se esta é viável ou não, para o autômato, conforme as regras.

| Exemplo de entrada: | Saída do exemplo de entrada: |
| ------------------- | ---------------------------- |
| EDEDDE              | N                            |
| DDDEEE              | S                            |
| DEDEDE              | S                            |
| DDE                 | N                            |
