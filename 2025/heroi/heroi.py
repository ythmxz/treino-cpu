def main():
    nomes: list[str] = input().split()
    iniciais: list[str] = [nome[0].lower() for nome in nomes]

    if any(i != iniciais[0] for i in iniciais):
        print("Bah!")
    else:
        print("Viva!")


if __name__ == "__main__":
    main()
