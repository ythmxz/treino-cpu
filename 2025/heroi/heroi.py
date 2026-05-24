from time import perf_counter


def main() -> None:
    nomes: list[str] = input().split()
    iniciais: list[str] = [nome[0].lower() for nome in nomes]

    if any(i != iniciais[0] for i in iniciais):
        print("Bah!")
    else:
        print("Viva!")


if __name__ == "__main__":
    inicio: float = perf_counter()
    main()
    fim: float = perf_counter()

    tempo: float = fim - inicio

    if tempo > 1.0:
        print(f"LIMITE DE TEMPO EXCEDIDO ({tempo} s)")
