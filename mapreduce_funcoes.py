# ETAPA 9 MAPREDUCE ORGANIZADO EM FUNÇÕES

# MAP Transforma cada palavra em um par
def map_word(word):
    return (word, 1)


# SHUFFLE/SORT Agrupa palavras iguais
def shuffle_sort(mapped_data):
    shuffle = {}

    for palavra, valor in mapped_data:
        if palavra not in shuffle:
            shuffle[palavra] = []

        shuffle[palavra].append(valor)

    return dict(sorted(shuffle.items()))


# REDUCE Soma os valores
def reduce_word(values):
    return sum(values)


# MAPREDUCE Executa todas as etapas
def mapreduce(text):
    palavras = text.split()

    # Etapa MAP
    resultado_map = []

    for palavra in palavras:
        resultado_map.append(map_word(palavra))

    # Etapa SHUFFLE/SORT
    resultado_shuffle = shuffle_sort(resultado_map)

    # Etapa REDUCE
    resultado_final = {}

    for palavra, valores in resultado_shuffle.items():
        resultado_final[palavra] = reduce_word(valores)

    return resultado_final


# TEXTO UTILIZADO
texto = "o gato subiu no telhado o cachorro correu atras do gato o gato desceu do telhado"

# EXECUÇÃO
resultado = mapreduce(texto)

print("Resultado final do MapReduce:")
print(resultado)

# ETAPA 10 SIMULANDO TRÊS NÓS

parte_1 = "o gato subiu no telhado"
parte_2 = "o cachorro correu atras do gato"
parte_3 = "o gato desceu do telhado"


# Cada nó executa somente o MAP
def processar_no(texto):
    palavras = texto.split()
    resultado = []

    for palavra in palavras:
        resultado.append(map_word(palavra))

    return resultado


# Processamento independente dos nós
resultado_no_1 = processar_no(parte_1)
resultado_no_2 = processar_no(parte_2)
resultado_no_3 = processar_no(parte_3)


print("\nResultado do Nó 1:")
print(resultado_no_1)

print("\nResultado do Nó 2:")
print(resultado_no_2)

print("\nResultado do Nó 3:")
print(resultado_no_3)

# ETAPA 11 SHUFFLE ENTRE OS NÓS

# Juntando os resultados dos três nós
todos_os_resultados = (
    resultado_no_1
    + resultado_no_2
    + resultado_no_3
)

print("\nResultados reunidos dos três nós:")
print(todos_os_resultados)

# Aplicando o Shuffle/Sort
resultado_shuffle_nos = shuffle_sort(todos_os_resultados)

print("\nResultado do Shuffle/Sort entre os nós:")
print(resultado_shuffle_nos)

# ETAPA 12 REDUCE DOS TRÊS NÓS

resultado_final_nos = {}

for palavra, valores in resultado_shuffle_nos.items():
    resultado_final_nos[palavra] = reduce_word(valores)

print("\nResultado final dos três nós:")
print(resultado_final_nos)


# COMPARAÇÃO COM O PROCESSAMENTO ÚNICO

resultado_unico = mapreduce(texto)

print("\nResultado do processamento único:")
print(resultado_unico)

print("\nOs dois resultados são iguais?")
print(resultado_final_nos == resultado_unico)