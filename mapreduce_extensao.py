from itertools import groupby

# ETAPA 14 EXTENSÃO MAPREDUCE

texto = "o gato subiu no telhado o cachorro correu atras do gato o gato desceu do telhado"

palavras = texto.split()

# MAP
resultado_map = list(map(lambda palavra: (palavra, 1), palavras))

# SHUFFLE/SORT
dados_ordenados = sorted(resultado_map, key=lambda item: item[0])

resultado_shuffle = {
    palavra: [valor for _, valor in grupo]
    for palavra, grupo in groupby(
        dados_ordenados, key=lambda item: item[0]
    )
}

# REDUCE
resultado_reduce = {
    palavra: sum(valores)
    for palavra, valores in resultado_shuffle.items()
}

print("MAP:")
print(resultado_map)

print("\nSHUFFLE/SORT:")
print(resultado_shuffle)

print("\nREDUCE:")
print(resultado_reduce)