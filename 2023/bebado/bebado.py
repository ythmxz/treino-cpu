from time import perf_counter


def main() -> None:
    linha: list[str] = input().split("%")
    valor: float = float(linha[0])

    if valor > 0.06:
        print("FLAGRADO ALCOOLIZADO")
    else:
        print("LIVRE")


if __name__ == "__main__":
    inicio: float = perf_counter()
    main()
    fim: float = perf_counter()

    tempo: float = fim - inicio

    if tempo > 1.0:
        print(f"LIMITE DE TEMPO EXCEDIDO ({tempo} s)")
