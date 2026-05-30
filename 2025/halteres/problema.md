# HALTERES EQUILIBRADOS

Limite de tempo: 1 segundo

## O Problema:

A Academia Esportiva Sociedade dos Bons Competidores (SBC) é uma academia de ginástica e entre as atividades há o uso
de halteres. Porém a academia é muito bagunçada e os "pesos" que são afixados nas duas pontas da barra do halteres estão
todos espalhados e misturados, fica difícil achar 2 iguais para equilibrar. Principalmente quando queremos um conjunto
maior, pois há muitos "leves" no meio. A opção é colocar vários e tentar equilibar nos 2 lados. Por exemplo a distribuição
seguinte é suficiente:

|          |     |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- |
| Esquerdo | 10  | 15  | 3   | 2   | 30  | kg  |
| Direito  | 20  | 5   | 5   | 30  | 0   | kg  |

De cada lado ficamos com 30kg, equilibrados um total de 60kg.
Por outro lado a distribuição a seguir não é boa:

|          |     |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- |
| Esquerdo | 10  | 25  | 3   | 5   | 43  | kg  |
| Direito  | 20  | 5   | 5   | 10  | 40  | kg  |

Neste caso o lado esquerdo é 3 quilogramas mais pesado que o direito. A você foi pedido que verifique se a distribuição
Esquerdo - Direito colocado nos halteres está Ok.

## Entrada:

Cada caso de entrada possui duas linhas, na primeira linha um inteiro E (0 < E <= 100) e a seguir E valores inteiros e_i
(0 < e_i <= 50). Na segunda linha um inteiro D (0 < D <= 100) e a seguir D valores inteiros d_i (0 < d_i <= 50). Representando
respectivamente a distribuição dos pesos no lado esquerdo e no direito. Todos os valores dos pesos são em quilogramas (kg).

## Saída:

Para cada caso de entrada deve ser impresso em uma linha: "OK" se os pesos estiverem equilibrados. Ou "E > D: p kg" se
o lado esquerdo for mais pesado que o direito por "p" quilogramas. Ou "D > E: p kg" caso o direito seja mais pesado.

| Exemplo de entrada: | Saída para o exemplo de entrada: |
| ------------------- | -------------------------------- |
| 4 10 15 3 2         | OK                               |
| 3 20 5 5            |                                  |
|                     |                                  |
| 4 10 25 3 5         | E > D: 3 kg                      |
| 4 20 5 5 10         |                                  |
