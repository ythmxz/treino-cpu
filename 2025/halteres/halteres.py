from pathlib import Path
from time import perf_counter


def ler_arquivo(caminho: Path) -> tuple[list[int], list[int]]:
    with open(caminho, "r") as arquivo:
        conteudo: list[str] = arquivo.read().splitlines()

        esquerda: list[int] = [int(valor) for valor in conteudo[0].split()]

        if esquerda[0] <= 0 or esquerda[0] > 100:
            raise ValueError(f"E = {esquerda[0]} (0 < E <= 100)")

        for i in range(1, len(esquerda)):
            if esquerda[i] <= 0 or esquerda[i] > 50:
                raise ValueError(f"e_i = {esquerda[i]} (0 < e_i <= 50)")

        if (len(esquerda) - 1) != esquerda[0]:
            raise ValueError(
                f"E = {esquerda[0]} | len(E) = {len(esquerda) - 1} (E == len(E))"
            )

        esquerda.pop(0)

        direita: list[int] = [int(valor) for valor in conteudo[1].split()]

        if direita[0] <= 0 or direita[0] > 100:
            raise ValueError(f"D = {direita[0]} (0 < D <= 100)")

        for i in range(1, len(direita)):
            if direita[i] <= 0 or direita[i] > 50:
                raise ValueError(f"d_i = {direita[i]} (0 < d_i <= 50)")

        if (len(direita) - 1) != direita[0]:
            raise ValueError(
                f"D = {direita[0]} | len(D) = {len(direita) - 1} (D == len(D))"
            )

        direita.pop(0)

    return esquerda, direita


def verificar_halteres(esquerda: list[int], direita: list[int]) -> str:
    diferenca: int = abs(sum(esquerda) - sum(direita))

    if sum(esquerda) > sum(direita):
        return f"E > D: {diferenca} kg"

    elif sum(esquerda) < sum(direita):
        return f"D > E: {diferenca} kg"

    else:
        return "OK"


def escrever_arquivo(caminho: Path, conteudo: str) -> None:
    with open(caminho, "w") as arquivo:
        arquivo.write(conteudo)


def main():
    inicio: float = perf_counter()

    caminho_entrada: Path = Path(__file__).with_name("input") / "file"
    caminho_saida: Path = Path(__file__).with_name("output") / "file"

    esquerda: list[int] = []
    direita: list[int] = []

    esquerda, direita = ler_arquivo(caminho_entrada)
    escrever_arquivo(caminho_saida, verificar_halteres(esquerda, direita))

    fim = perf_counter()
    print(f"Execução: {(fim - inicio):g} s")


if __name__ == "__main__":
    main()
