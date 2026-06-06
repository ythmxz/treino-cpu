def main() -> None:
    linha: list[str] = input().split("%")
    valor: float = float(linha[0])

    if valor > 0.06:
        print("FLAGRADO ALCOOLIZADO")
    else:
        print("LIVRE")


if __name__ == "__main__":
    main()
