from time import perf_counter


def main() -> None:
    esquerda: list[int] = [int(peso) for peso in input().split()[1:]]
    direita: list[int] = [int(peso) for peso in input().split()[1:]]

    soma_esquerda: int = sum(esquerda)
    soma_direita: int = sum(direita)

    diferenca: int = abs(soma_esquerda - soma_direita)

    if soma_esquerda > soma_direita:
        print(f"E > D: {diferenca} kg")

    elif soma_direita > soma_esquerda:
        print(f"D > E: {diferenca} kg")

    else:
        print("OK")


if __name__ == "__main__":
    inicio: float = perf_counter()
    main()
    fim: float = perf_counter()

    tempo: float = fim - inicio

    if tempo > 1.0:
        print(f"LIMITE DE TEMPO EXCEDIDO ({tempo} s)")
