# Carta Criptografibonacciada (CPU)

Limite de tempo: 1 segundo

## Problema:

Um grupo de três amigos iam fazer intercâmbio em países diferentes, e planejaram trocar cartas enquanto distantes. Como não queriam que outras pessoas soubessem do teor das conversas, resolveram criar um esquema de criptografia baseado na sequência de Fibonacci. Sendo O(letra) a posição original do caractere 'letra' no alfabeto latino (composto por 26 letras), ou seja, $O(a)$ = 1, $O(b)$ = 2, ..., $O(z)$ = 26, e sendo M(letra) a posição do caractere 'letra' na mensagem a ser criptografada. Por exemplo, na mensagem 'alo mundo!', $M(a)$ = 1, $M(l)$ = 2, $M(o)$ = 3, $M(m)$ = 5, ..., $M(o)$ = 9. Nesse esquema de criptografia, criado por eles, cada letra '$l$' da mensagem original deve ser trocada por uma outra letra $C(x)$, cuja posição no alfabeto é determinada por $x$. Para calcular $x$ tem-se:

$x = O(l) + Fib(M(l))$

onde $Fib(i)$ corresponde ao i-ésimo elemento na sequência de Fibonacci. Vale lembrar que, como o alfabeto contém 26 letras, este deve ser tratado em círculo se necessário, ou seja, a posição $C(27)$ = 'a', $C(28)$ = 'b' e assim por diante. Os caracteres de pontuação e tabulação não são criptografáveis, mas suas posições contam!

## Entrada:

A primeira linha da entrada deve conter um caractere 'C' ou 'D', informando se a mensagem deve ser criptografada ou decriptografada, respectivamente. Na segunda linha estará contida a mensagem-alvo, composta apenas por caracteres minúsculas e de no máximo 200 caracteres. Existem pontuações, mas não há caracteres acentuados.

## Saída:

A mensagem resultado.

| Exemplo de entrada: | Saída do Exemplo de entrada: |
| ------------------- | ---------------------------- |
| C bmq rcayw!        | alo mundo!                   |
| D boa sorte!        | cpc xweom!                   |
