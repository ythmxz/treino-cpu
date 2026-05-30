# GATO GAIATO

Limite de tempo: 1 segundo

## O Problema:

Guilhermina gosta do gato Gatito. Mas ela fala que Gatito é Gaiato quando ele sai de casa. Guilhermina colocou um chip
no Gatito para obter sua localização, e de vez em vez ela olha no aplicativo as coordenadas da posição de Gatito. Só que ela
acha que o aplicativo poderia ser melhorado, pois ela precisa relacionar a localização do gato com a própria casa, ou casa
de campo, ou casa da praia, ou casa da avó, ... seja lá onde ela estiver com o Gatito. Ela pediu para você construir um
algoritmo para adicionar ao aplicativo dela informando se Gatito é "Gato"ou "Gaiato". No mundo de Guilhermina, a casa
sempre é redonda.

## Entrada:

Cada caso de teste constituído de duas linhas, a primeira linha contém três números inteiros H, V e R (−50 <= H, V <= 50
e 0 < R <= 50) representando a localização leste-oeste (H) e sul-norte (V) da casa que Guilhermina e Gatito estão, e o raio
(R) da casa. Na segunda linha são dois números inteiros G_h e G_v (−100 <= G_h, G_v <= 100), a posição de Gatito com G_h a
coordenada leste-oeste e G_v a coordenada sul-norte.

## Saída:

Dada a posição do gato, se ele estiver no exterior do imóvel deve ser impresso a palavra "Gaiato", caso contrário, "Gato".

| Exemplo de entrada: | Saída para o Exemplo de entrada: |
| ------------------- | -------------------------------- |
| 1 3 2               | Gaiato                           |
| 3 1                 |                                  |
|                     |                                  |
| 0 1 3               | Gato                             |
| -2 1                |                                  |
