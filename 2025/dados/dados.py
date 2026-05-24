from time import perf_counter


def main() -> None:
    jogadores: int = int(input())
    jogadas: list[int] = []

    for _ in range(jogadores):
        pares: list[str] = input().split()
        lances: list[int] = []

        for par in pares:
            a, b = [int(valor) for valor in par.strip("()").split(",")]

            if a == b:
                if a == 1 or b == 1:
                    lances.append(30)
                else:
                    lances.append((a * b) * 2)
            else:
                lances.append(a * b)

        jogadas.append(sum(lances))

    ordem: list[tuple[int, int]] = list(enumerate(jogadas, 1))
    maior_pontuacao: int = max(valor for _, valor in ordem)

    ganhadores: list[int] = []

    for jogador, pontuacao in ordem:
        if pontuacao == maior_pontuacao:
            ganhadores.append(jogador)

    print(f"Pontos do ganhador: {maior_pontuacao}")
    print("Ganhador(es): ", end="")
    print(*ganhadores, sep=", ")


if __name__ == "__main__":
    inicio: float = perf_counter()
    main()
    fim: float = perf_counter()

    tempo: float = fim - inicio

    if tempo > 1.0:
        print(f"LIMITE DE TEMPO EXCEDIDO ({tempo} s)")
