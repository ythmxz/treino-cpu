def main() -> None:
    movimentos: list[list[str]] = []

    while True:
        try:
            linha = input().strip()
        except EOFError:
            break

        if linha:
            movimentos.append(list(linha))

    posicao: int = 0

    for movimento in movimentos:
        for direcao in movimento:

            if direcao == "E":
                posicao -= 1

                if posicao < 0:
                    break

            if direcao == "D":
                posicao += 1

                if posicao > 10:
                    break

        print("S") if posicao == 0 else print("N")

        posicao = 0


if __name__ == "__main__":
    main()
