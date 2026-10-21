# Atividade MapReduce em Python

## Descrição

Este projeto apresenta uma implementação do modelo **MapReduce utilizando Python**, com o objetivo de demonstrar como grandes conjuntos de dados podem ser processados por meio das etapas de mapeamento, agrupamento e redução.

A atividade utiliza a contagem de palavras de um texto como exemplo prático, incluindo uma simulação de processamento distribuído em três nós.

## Objetivos

- Compreender o funcionamento do modelo MapReduce.
- Implementar as etapas MAP, SHUFFLE/SORT e REDUCE.
- Realizar a contagem de palavras de um texto.
- Validar os resultados obtidos.
- Organizar o código utilizando funções.
- Simular o processamento distribuído em três nós.
- Explorar recursos nativos do Python, como `map()` e `itertools.groupby()`.

## Tecnologias utilizadas

- Python 3
- Biblioteca padrão do Python
- Visual Studio Code
- Git e GitHub

## Estrutura do projeto

```text
AtividadeMapReduce/
├── mapReduce.py
├── mapreduce_funcoes.py
├── mapreduce_extensao.py
├── resultado.txt
├── respostas.md
└── README.md
```

## Etapas do MapReduce

### 1. MAP

O texto é dividido em palavras, e cada palavra é transformada em um par `(palavra, 1)`.

Exemplo:

```python
[("gato", 1), ("cachorro", 1), ("gato", 1)]
```

### 2. SHUFFLE/SORT

As ocorrências são agrupadas de acordo com a palavra.

```python
{
    "gato": [1, 1],
    "cachorro": [1]
}
```

### 3. REDUCE

Os valores associados a cada palavra são somados, produzindo a contagem final.

```python
{
    "gato": 2,
    "cachorro": 1
}
```

## Implementações

**`mapReduce.py`**

Apresenta as etapas básicas de MAP, SHUFFLE/SORT e REDUCE, incluindo a validação da quantidade total de palavras.

**`mapreduce_funcoes.py`**

Organiza o processamento em funções e realiza uma simulação distribuída em três nós, comparando o resultado com o processamento único.

**`mapreduce_extensao.py`**

Apresenta uma implementação alternativa utilizando recursos nativos do Python, incluindo `map()` e `itertools.groupby()`.

**`resultado.txt`**

Contém as saídas das execuções dos três programas, permitindo acompanhar os resultados de cada etapa.

**`respostas.md`**

Contém as respostas teóricas e explicações relacionadas à atividade.

## Como executar

É necessário ter o Python 3 instalado.

No terminal, dentro da pasta do projeto, execute:

```bash
python mapReduce.py
python mapreduce_funcoes.py
python mapreduce_extensao.py
```

## Validação dos resultados

O programa verifica se a quantidade de palavras do texto original corresponde à soma das ocorrências obtidas no REDUCE.

Na execução realizada:

```text
Quantidade de palavras no texto: 16
Soma das ocorrências: 16
Os valores são iguais? True
```

A simulação com três nós também apresentou o mesmo resultado do processamento único:

```text
Os dois resultados são iguais?
True
```

## Conclusão

A atividade permitiu compreender, de forma prática, as principais etapas do MapReduce e sua aplicação na contagem de palavras.

A simulação distribuída demonstrou como diferentes partes de um conjunto de dados podem ser processadas separadamente e posteriormente reunidas para produzir um resultado global consistente.

O projeto também reforçou conceitos de programação em Python, manipulação de listas e dicionários, funções e validação de resultados.