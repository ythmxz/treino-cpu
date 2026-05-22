import java.io.FileWriter;
import java.io.IOException;
import java.lang.Math;
import java.net.URISyntaxException;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

static List<List<Integer>> lerArquivo(Path caminho) throws IOException {
    try (Scanner leitor = new Scanner(caminho)) {
        int tamanhoEsquerda = leitor.nextInt();

        if (tamanhoEsquerda <= 0 || tamanhoEsquerda > 100) {
            throw new IllegalArgumentException(
                "E = " + tamanhoEsquerda + " (0 < E <= 100)"
            );
        }

        List<Integer> esquerda = new ArrayList<>(tamanhoEsquerda);

        for (int i = 0; i < tamanhoEsquerda; i++) {
            esquerda.add(leitor.nextInt());

            if (esquerda.getLast() <= 0 || esquerda.getLast() > 50) {
                throw new IllegalArgumentException(
                    "e_i = " + esquerda.getLast() + " (0 < e_i <= 50)"
                );
            }
        }

        int tamanhoDireita = leitor.nextInt();

        if (tamanhoDireita <= 0 || tamanhoDireita > 100) {
            throw new IllegalArgumentException(
                "D = " + tamanhoDireita + " (0 < D <= 100)"
            );
        }

        List<Integer> direita = new ArrayList<>(tamanhoDireita);

        for (int i = 0; i < tamanhoDireita; i++) {
            direita.add(leitor.nextInt());

            if (direita.getLast() <= 0 || direita.getLast() > 50) {
                throw new IllegalArgumentException(
                    "d_i = " + direita.getLast() + " (0 < d_i <= 50)"
                );
            }
        }

        return List.of(esquerda, direita);
    }
}

static String verificarHalteres(List<Integer> esquerda, List<Integer> direita) {
    int somaEsquerda = 0;
    int somaDireita = 0;

    for (int i : esquerda) {
        somaEsquerda += i;
    }

    for (int i : direita) {
        somaDireita += i;
    }

    int diferenca = Math.abs(somaEsquerda - somaDireita);

    if (somaEsquerda > somaDireita) {
        return "E > D: " + diferenca + " kg";
    } else if (somaDireita > somaEsquerda) {
        return "D > E: " + diferenca + " kg";
    }

    return "OK";
}

static void escreverArquivo(Path caminho, String conteudo) throws IOException {
    try (FileWriter escritor = new FileWriter(caminho.toFile())) {
        escritor.write(conteudo);
    }
}

void main() throws IOException, URISyntaxException {
    long inicio = System.nanoTime();

    Path caminhoBase = Path.of(
        getClass().getProtectionDomain().getCodeSource().getLocation().toURI()
    );

    Path caminhoEntrada = caminhoBase.resolveSibling("input").resolve("file");
    Path caminhoSaida = caminhoBase.resolveSibling("output").resolve("file");

    List<List<Integer>> halteres = lerArquivo(caminhoEntrada);
    escreverArquivo(
        caminhoSaida,
        verificarHalteres(halteres.get(0), halteres.get(1))
    );

    long fim = System.nanoTime();
    IO.println("Execução: " + (fim - inicio) + " s");
}
