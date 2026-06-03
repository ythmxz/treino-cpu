from time import perf_counter


def kelvin(valor: float, unidade: str) -> float:
    match unidade:
        case "F":
            return (valor + 459.889) / 1.8
        case "C":
            return valor + 273.15
        case "Ra":
            return valor / 1.8
        case "Re":
            return (valor / 0.8) + 273.15
        case "Ro":
            return (((valor - 7.5) * 40) / 21) + 273.15

    return valor


def fahrenheit(valor: float, unidade: str) -> float:
    return kelvin(valor, unidade) * 1.8 - 459.889


def celsius(valor: float, unidade: str) -> float:
    return kelvin(valor, unidade) - 273.15


def rankine(valor: float, unidade: str) -> float:
    return kelvin(valor, unidade) * 1.8


def reaumur(valor: float, unidade: str) -> float:
    return (kelvin(valor, unidade) - 273.15) * 0.8


def romer(valor: float, unidade: str) -> float:
    return (kelvin(valor, unidade) - 273.15) * 21 / 40 + 7.5


def main() -> None:
    linha_inutil = input()
    linha = input().split()

    valor_temp = float(linha[0])
    unidade_temp = linha[1]

    print(f"{kelvin(valor_temp, unidade_temp):.2f} K")
    print(f"{fahrenheit(valor_temp, unidade_temp):.2f} F")
    print(f"{celsius(valor_temp, unidade_temp):.2f} C")
    print(f"{rankine(valor_temp, unidade_temp):.2f} Ra")
    print(f"{reaumur(valor_temp, unidade_temp):.2f} Re")
    print(f"{romer(valor_temp, unidade_temp):.2f} Ro")


if __name__ == "__main__":
    inicio: float = perf_counter()
    main()
    fim: float = perf_counter()

    tempo: float = fim - inicio

    if tempo > 1.0:
        print(f"LIMITE DE TEMPO EXCEDIDO ({tempo} s)")
