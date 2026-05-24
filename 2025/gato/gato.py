class Casa:
    def __init__(self, longitude: str, latitude: str, raio: str) -> None:
        self.longitude: int = int(longitude)
        self.latitude: int = int(latitude)
        self.raio: int = int(raio)


class Gatito:
    def __init__(self, longitude: str, latitude: str) -> None:
        self.longitude: int = int(longitude)
        self.latitude: int = int(latitude)


def main():
    valores_casa: list[str] = input().split()
    casa: Casa = Casa(valores_casa[0], valores_casa[1], valores_casa[2])

    valores_gatito: list[str] = input().split()
    gatito: Gatito = Gatito(valores_gatito[0], valores_gatito[1])

    diferenca_longitude: int = gatito.longitude - casa.longitude
    diferenca_latitude: int = gatito.latitude - casa.latitude

    distancia_quadrado: int = diferenca_longitude**2 + diferenca_latitude**2

    if distancia_quadrado <= casa.raio**2:
        print("Gato")
    else:
        print("Gaiato")


if __name__ == "__main__":
    main()
