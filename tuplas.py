#  Autor: Samuel Moreira Abreu
#  O intuito desse código é revisar os conceitos iniciais de Python para o começo em uma iniciação cientifica.
"""
Tuplas são muito parecidas com listas

existem basicamente duas diferenças basicas

1 - as tuplas são representadas por parenteses
2 - as tuplas são imutaveis, ou seja, ao se criar uma tupla, ela NÃO muda!  toda alteração em uma tupla gera uma nova tupla

# Declaração de tuplas:

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))

tupla3 = (4) # isso não é uma tupla!!!!!
print(tupla3)
print(type(tupla3))

tupla4 = (4,)
print(tupla4)
print(type(tupla4))

tupla5 = 4,
print(tupla5)
print(type(tupla5))

     TUPLAS SÃO DEFINIDAS PELA VIRGULA, E NÃO PELO PARÊNTESES

# Range em tuplas
tupla = tuple(range(10))
print(tupla)
print(type(tuple))


# Desempacotamento de tuplas

tupla = ('Geek univeristy', 'Curso de python')

escola, curso = tupla
print(tupla[0])
print(tupla[1])
print(tupla)
print(escola)
print(curso)


# metodos para adição e remoção NAO EXISTEM, devido as tuplas serem imutaveis!

# se os valores são inteiros e reais, é possivel utilizas soma dos termos, tamanho, min e max
tupla = (1, 2, 4, 5, 6, 7, 8, 3)

print(sum(tupla))
print(len(tupla))
print(max(tupla))
print(min(tupla))

# concatenação de tuplas

tupla = (1, 2, 4, 5, 6, 7, 8, 3)
tupla2 = (1, 2, 4, 5, 6, 7)
print(tupla)
print(tupla2)
print(tupla + tupla2)
tupla3 = tupla2 + tupla
print(tupla3)


# verificaçao em tuplas

tupla1 = (1, 2, 3)

print(7 in tupla1)


# iterando sobre uma tupla
tupla1 = (1, 2, 3)

for num in tupla1:
     print(num)

for indice, valor in enumerate(tupla1):
     print(indice, valor)

# contando elementos dentro de uma tupla

tupla1 = ('a', 'b', 'c', 'b')

print(tupla1.count('b'))

escola = tuple('Samueell')

print(escola)

print(escola.count('l'))


#utilizar tuplas quando não vamos mudar valores em uma lista/tupla

#ex
meses = ("Jan", "Fev", "Mar", "Abr", "Maio", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez")

for indice, mes in enumerate(meses):
     print(indice+1, mes)

print(meses.index("Fev", 1))

# Slicing
# tupla[inicio:fim:passo]
meses = ("Jan", "Fev", "Mar", "Abr", "Maio", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez")
print(meses[5:9])
print(meses[::9])
print(meses[::])
print(meses[::-1])
print(meses[9])

"""


# Junção de tuplas
meses = ("Jan", "Fev", "Mar", "Abr", "Maio", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez")
print(meses)
nova = meses
print(nova)
outra = ('odeio', 'fazer', 'aniversario', 'em', 'Dez')
nova = nova + outra
print(meses)
print(outra)
print(nova)