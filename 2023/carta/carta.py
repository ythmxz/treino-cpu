from time import perf_counter


def fib(index: int) -> int:
    if index <= 2:
        return 1

    tabela: list[int] = [0] * (index + 1)

    tabela[1] = 1
    tabela[2] = 1

    for i in range(3, index + 1):
        tabela[i] = tabela[i - 1] + tabela[i - 2]

    return tabela[index]


def main() -> None:
    alfabeto: list[str] = [ "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ]

    tipo: str = input()
    entrada: list[str] = list(input())
    saida: list[str] = []

    index_original: int = 0
    index_modificado: int = 0

    for posicao, letra in enumerate(entrada, 1):
        if letra not in alfabeto:
            saida.append(letra)
            continue

        index_original = alfabeto.index(letra) + 1

        if tipo == "C":
            index_modificado = (index_original + fib(posicao)) % 26

        elif tipo == "D":
            index_modificado = (index_original - fib(posicao)) % 26

        saida.append(alfabeto[index_modificado - 1])

    print("".join(saida))


if __name__ == "__main__":
    inicio: float = perf_counter()
    main()
    fim: float = perf_counter()

    tempo: float = fim - inicio

    if tempo > 1.0:
        print(f"LIMITE DE TEMPO EXCEDIDO ({tempo} s)")
