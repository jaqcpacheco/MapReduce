# ETAPA 3 MAP

def map_word(word):
    return (word, 1)


# ETAPA 4 APLICANDO O MAP

texto = "o gato subiu no telhado o cachorro correu atras do gato o gato desceu do telhado"

palavras = texto.split()

resultado_map = []

for palavra in palavras:
    resultado_map.append(map_word(palavra))

print("Resultado MAP:")
print(resultado_map)

# ETAPA 5 SHUFFLE/SORT

shuffle = {}

for palavra, valor in resultado_map:

    if palavra not in shuffle:
        shuffle[palavra] = []

    shuffle[palavra].append(valor)

print("\nResultado SHUFFLE/SORT:")
print(shuffle)

# ETAPA 6 REDUCE

def reduce_word(values):
    return sum(values)

print("\nTeste REDUCE:")
print(reduce_word([1, 1, 1]))

# ETAPA 7 EXECUTANDO O REDUCE

resultado_final = {}

for palavra, valores in shuffle.items():
    resultado_final[palavra] = reduce_word(valores)

print("\nResultado final do MapReduce:")
print(resultado_final)

# ETAPA 8 VALIDAÇÃO

quantidade_palavras = len(palavras)
soma_ocorrencias = sum(resultado_final.values())

print("\nValidação dos resultados:")
print("Quantidade de palavras no texto:", quantidade_palavras)
print("Soma das ocorrências:", soma_ocorrencias)
print("Os valores são iguais?", quantidade_palavras == soma_ocorrencias)