# BOI-BUMBÁ (CPU)

Limite de tempo: 1 segundo

## O Problema:

O Boi-Bumbá é um folguedo folclórico praticado em todo Brasil, mas com ênfase na região Norte-Nordeste. Também conhecido como Bumba-meu-boi, Boi-Calemba, Boi-de-reis, Boi-zumbi entre outros. A história na sua forma mais simples vem da escrava Catarina que grávida queria comer língua do boi mais bonito, pediu ao marido Chico (também conhecido como Pai Francisco ou Mateus) que matou o boi. O casal foi perseguido pelo fazendeiro, e no final com a ajuda de curandeiros o Boi foi ressuscitado, então o fazendeiro fez uma festa. O folclore se baseia na importância do boi nas atividades da época. O Maranhão é onde mais se comemora esta festa, mas seu ápice acontece em Parintis-PA onde a festa envolve a disputa de dois Bois-Bumbá: Caprichoso e Garantido representados pelas cores azul e vermelho respectivamente. O prefeito da cidade de São Bento do Capão (SBC) vendo o Boi-Bumbá como uma festa alternativa às festas-juninas que já têm dominância nas cidades vizinhas quer trazer o folguedo na forma da disputa de Parintins, neste caso já pediu às agremiações carnavalescas para passarem a representar algum Boi-Bumbá em disputa na festa. Só que ainda precisa decidir a forma de premiação. Serão computados pontos (inteiro ou meio) de 0 a 10 em várias alegorias, como: Fantasia, Bateria, Enredo, entre outras e cada alegoria tem seu peso. No final ganha quem tiver mais pontos. Mas se houver empate, o critério de desempate segue por aquele que tiver mais pontos em determinada alegoria por ordem. Se tudo seguir empatado então será por ordem de apresentação. A você foi pedido um algoritmo para definir a ordem final de classificação dos bois.

## Entrada:

A entrada começa com 2 números inteiros em uma linha: $A$ (0 < $A$ <= 10) e $B$ (1 < $B$ <= 10), representando respectivamente as alegorias e os bois. Na segunda linha são 10 valores inteiros representando o peso de cada alegoria na nota, os valores estão na ordem de desempate por nota mais alta nas alegorias, da primeira à última. Em sequida são $B$ linhas onde a bi-ésima linha representa o bi-ésimo boi, na ordem das apresentações, e cada linha contém, uma palavra $N$ representando o nome do boi com no máximo 10 caracteres (ASCII padrão sem acentuação) sendo a primeira maiúscula, e $A$ valores inteiros ou em frações de meio $a_j$ (0 <= $a_j$ <= 10) que são as notas na ordem das alegorias.

## Saída:

Como saída, deve ser impressa $B$ linhas com os nomes dos bois em ordem de classificação na competição.

| Exemplo de entrada:  | Saída para o exemplo de entrada: |
| -------------------- | -------------------------------- |
| 3 3                  | Furioso                          |
| 3 5 1                | Gracioso                         |
| Mimoso 2.5 1.5 3.0   | Mimoso                           |
| Gracioso 4.0 1.0 1.0 |                                  |
| Furioso 3.0 2.0 1.0  |                                  |
|                      |                                  |
| 2 2                  | Saudoso                          |
| 5 5                  | Medroso                          |
| Saudoso 10.0 10.0    |                                  |
| Medroso 10.0 10.0    |                                  |
