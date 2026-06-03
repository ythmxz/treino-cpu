# Jobs em Ordem (CPU)

Limite de tempo: 1 segundo

## Problema:

Limite de tempo: 1 segundo

Todos os dias diversos estudantes mundo afora fazem as suas listas “TO-DO”, com o intuito de organizar as seus jobs de maneira que nada deixe de ser feito. Porém, organizar a ordem em que os jobs devem ser executados nem sempre é fácil, uma vez que alguns jobs têm que ser executados antes de outros, e não saber nem por onde começar leva muita gente a procrastinar e até desistir das obrigações! Na tentativa de organizar isso no seu caso, a Lara desenvolveu um esquema de enumeração dos jobs em uma ordem em que ela desejaria executar, sem quebrar requisito (justo sem se preocupar com a dependência de ordem entre os jobs). Em seguida ela criou uma lista de pares ordenados dos jobs, indicando qual job tem prioridade sobre outro. O que ela deseja fazer então é estabelecer uma ordem em que os jobs possam ser executados a contento, e pediu a você que crie um algoritmo para organizar os jobs.

## Entrada:

A entrada consiste, na primeira linha, em dois valores: $N$, 1 <= $N$ <= 100 que representa o número de jobs na lista, e $M$, 0 <= $M$ < $N^2$ que consiste na quantidade de pares ordenados de dependência entre os jobs, e em seguida são $M$ linhas contendo dois valores $a$ e $b$ 1 <= $a$, $b$ <= $N$, separados por um espaço em branco, sendo que $a$ representa um job que deve ser executado antes do job $b$. Sabe-se que não há dependências circulares entre os jobs, ou seja, sempre é possível obter uma ordenação dos jobs que satisfaça as dependências.

## Saída:

Para cada lista de jobs, apresentar uma ordem de execução plausível dos mesmos que portanto atenda às necessidades da Lara.

| Exemplo de entrada: | Saída do Exemplo de entrada: |
| ------------------- | ---------------------------- |
| 9 11                | 6 1 3 9 8 7 5 2 4            |
| 1 3                 |                              |
| 3 4                 |                              |
| 3 5                 |                              |
| 3 9                 |                              |
| 5 2                 |                              |
| 9 8                 |                              |
| 6 1                 |                              |
| 6 8                 |                              |
| 7 2                 |                              |
| 7 5                 |                              |
| 8 7                 |                              |
