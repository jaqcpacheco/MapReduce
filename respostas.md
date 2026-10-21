Por que não podemos simplesmente executar o Reduce antes do Shuffle/S​​ort?

Porque precisamos primeiro agrupar os valores das palavras iguais. O Shuffle/Sort realiza esse agrupamento, permitindo que o Reduce some as ocorrências de cada palavra e obtenha o resultado final.

Etapa 8 - Validação 

Quantidade de palavras no texto: 16

Soma das ocorrências: 16

Os valores são iguais? (X) Sim  ( ) Não

Explicação:

Os valores precisam ser iguais porque cada palavra do texto é contabilizada uma vez durante o MAP. O Shuffle/Sort agrupa as ocorrências e o Reduce realiza a soma. Portanto, a soma das contagens deve corresponder ao total de palavras do texto, garantindo que nenhuma ocorrência foi perdida ou contabilizada duas vezes.

Etapa 12 — Comparação dos resultados

Os dois resultados são iguais?

(X) Sim
( ) Não

Por quê?

Os resultados são iguais porque, mesmo dividindo o texto entre três nós, todas as palavras são processadas pelo MAP. Depois, o Shuffle/Sort reúne as ocorrências de cada palavra e o Reduce realiza a soma. Dessa forma, o resultado final é o mesmo que processar todo o texto de uma única vez.

Etapa 13 — Desafio final

1. O que poderia ser dividido entre os computadores?

Os 10 GB de texto poderiam ser divididos em partes menores, distribuindo aproximadamente 1 GB para cada computador.

2. Qual etapa poderia ser executada paralelamente?

A etapa MAP, pois cada computador pode processar sua parte do texto independentemente dos outros.

3. Qual seria a função do Shuffle/Sort?

Agrupar e organizar os dados que possuem a mesma chave, reunindo as ocorrências de cada palavra, mesmo que tenham sido processadas em computadores diferentes.

4. Qual seria a função do Reduce?

Somar os valores agrupados pelo Shuffle/Sort, calculando a quantidade total de ocorrências de cada palavra.

5. Qual seria a principal vantagem de utilizar vários computadores?

A principal vantagem seria distribuir o processamento entre vários computadores, permitindo executar tarefas em paralelo e reduzir o tempo necessário para processar grandes volumes de dados.

Etapa 14 — Extensão

MAP: Utilização da função map() para transformar cada palavra em um par (palavra, 1).

SHUFFLE/SORT: Utilização de sorted() e groupby() para ordenar e agrupar as ocorrências das palavras iguais.

REDUCE: Utilização de sum() para somar os valores agrupados e obter a quantidade de ocorrências de cada palavra.