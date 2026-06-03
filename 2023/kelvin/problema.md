# Kelvin, Celsius e Fahrenheit (CPU)

Limite de tempo: 1 segundo

## Problema:

A noção de quente e frio, falando sobre temperatura, sempre esteve presente entre nós, tanto que urgiu medir a temperatura. Vários pioneiros criaram um sistema de medidas. Os primórdios das medidas veio com Isaac Newton, por volta de 1700, criou uma escala forma qualitativa, compreendendo cerca de 20 pontos de referência que variavam de "ar frio no inverno" para "brasas no fogo da cozinha", mas se sentiu insatisfeito e tomou dois pontos o derretimento da neve 0 $N$ e a ebulição da água 33 $N$, sendo a precursora da escala Centígrada ou Celsius. Na mesma época Ole Christensen R∅mer criou a escala com o congelamento da salmoura 0 $R∅$ e ebulição da água 60 $R∅$. Daniel Gabriel Fahrenheit em 1724 criou sua escala de temperatura, definindo o 0 $F$ uma mistura de água, gelo picado, sal e amônia e o 100 $F$ que foi a temperatura do corpo de sua mulher (ela estava febril). Uma grande contribuição de Fahrenheit foi o termômetro de mercúrio. O grande problema desta escala adotada em países de língua inglesa,é a definição formal dos pontos fixos. Anders Celsius em 1742 publicou um trabalho "Observações sobre 2 graus persistentes em um termômetro", que são o ponto de fusão do gelo e o ponto de evaporação da água, e tabelou-os como 0 e 100. Por ser baseada em centésimos, a escala ganhou o nome de Centígrada, mas futuramente foi nomeada em homenagem a seu criador: Celsius. Também tem problemas com a definição formal, pois estas temperaturas dependem da pressão atmosférica e acabou sendo adotada pelo sistema métrico. Em paralelo René-Antoine Ferchault de Réaumur criou sua escala o mesmo 0, mas a temperatura de ebulição ficou como 80 $R$. Por fim veio uma escala científica, como a Kelvin, em homenagem ao físico e engenheiro irlandês William Thomson (1824–1907), 1º barão Kelvin, que em 1848 escreveu sobre a necessidade de uma escala absoluta. Esta escala toma como 0 a temperatura 0 absoluta, onde não há mais movimento de átomos (já que a temperatura vem da agitação dos átomos), e adotou-se a temperatura tripla da água como 273.16 $K$, isto feito para que a escala Kelvin e Celsius tenha a mesma largura de uma unidade. A temperatura tripla da água na escala Celsius é 0.01 $C$, e o zero absoluto −273.15 $C$. Por fim o engenheiro e físico escocês William John Macquorn Rankine propôs em 1859 a escala Rankine, também absoluta, mas com a diferença de grau igual à da escala Fahrenheit, 0 $Ra$ = −459.67 $F$. No passado adotava-se o símbolo de grau 'o' antes da unidade da escala mas isto tornou-se obsoleto. Abaixo está uma tabela de conversões, com base na escala Kelvin. A você foi solicitado um algoritmo que realize as conversões.

| Escala     |              Fórmula              |
| ---------- | :-------------------------------: |
| Fahrenheit |      $F = K × 1.8 − 459.889$      |
| Celsius    |         $C = K − 273.15$          |
| Rankine    |          $Ra = K × 1.8$           |
| Réaumur    |     $Re = (K − 273.15) × 0.8$     |
| R∅mer      | $Ro = (K − 273.15) × 21/40 + 7.5$ |

## Entrada:

A entrada é um caso de teste de duas linhas, a primeira linha é um texto representando um evento com no máximo 100 caracteres UTF-8 e a segunda linha é a temperatura do evento, em ponto flutuante, em uma determinada escala, que pode ser: $K$ - Kelvin, $F$ - Fahrenheit, $C$ - Celsius, $Ra$ - Rankine, $Re$ - Réaumur ou $Ro$ - R∅mer. A unidade está separada da medida por um espaço em branco.

## Saída:

A saída deve conter seis linhas onde cada linha temos temperatura do evento em cada uma das seis escalas, nesta ordem: $K$, $F$, $C$, $Ra$, $Re$, $Ro$. Todas com duas casas decimais. A unidade deve estar separada da medida por exatamente um espaço em branco.

| Exemplo de entrada:                  | Saída do Exemplo de entrada: |
| ------------------------------------ | ---------------------------- |
| Temperatura de fusão do Mercúrio     | 234.32 K                     |
| 234.32 K                             | -38.11 F                     |
|                                      | -38.83 C                     |
|                                      | 421.78 Ra                    |
|                                      | -31.06 Re                    |
|                                      | -12.89 Ro                    |
|                                      |                              |
| Temperatura da mulher de Fahreinheit | 311.05 K                     |
| 100 F                                | 100.00 F                     |
|                                      | 37.90 C                      |
|                                      | 559.89 Ra                    |
|                                      | 30.32 Re                     |
|                                      | 27.40 Ro                     |
