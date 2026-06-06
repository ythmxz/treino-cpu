def main() -> None:
    zenit: list[str] = ["z", "e", "n", "i", "t", "Z", "E", "N", "I", "T"]
    polar: list[str] = ["p", "o", "l", "a", "r", "P", "O", "L", "A", "R"]

    entrada: list[str] = []
    saida: list[str] = []

    index: int = 0

    while True:
        try:
            entrada: list[str] = list(input())
        except EOFError:
            break

        saida = []

        for caractere in entrada:
            if caractere in zenit:
                index = zenit.index(caractere)
                caractere = polar[index]

            elif caractere in polar:
                index = polar.index(caractere)
                caractere = zenit[index]

            saida.append(caractere)

        print("".join(saida))


if __name__ == "__main__":
    main()
