#  Autor: Samuel Moreira Abreu
#  O intuito desse código é revisar os conceitos iniciais de Python para o começo em uma iniciação cientifica.

"""
Listas funcionam como vetores e matrizes, podemos colocar qualquer tipo de dado em listas, e é 
DINAMICO

Outras linguagens possuem tamanhos pré definidos e fixos

Já em python, não possui tamanho fixo, podemos criar a lista e ir colocando elementos até que haja memoria disponivel
As lista não possuem tipos de dados definidos, podemos colocar qualquer tipo de dados

listas são representadas com colchetes "[]"

"""

type([])

lista1 = [100, 7, 15, 22, 3, 66, 7]

lista2 = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'i']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

#podemos checar se valores estão na lista
num = 13
if num in lista4:
     print(f"encontrei o numero {num}!")
else:
     print(f"não encontrei o {num}")

print(lista1)
lista1.sort()
print(lista1)

# Podemos facilmente contar o numero de ocorrencias de um valor em uma lista

print(lista1.count(7))
print(lista5.count('e'))

# Adicionar elementos em lista

"""
Para adicionar elementos ou valores em lista, utilizamos a função
APPEND
"""

print(lista1)
# apenas podemos passar 1 elemento por vez!!!!!
lista1.append(43)
print(lista1)
lista1.sort()
print(lista1)

# lista de listas

lista1.append([12, 67, 33]) # adiciona uma lista dentro de uma posição
print(lista1)
if [12, 67, 33] in lista1:
     print("encontrei")
else:
     print("não encontrei")

lista1.extend([123, 44, 67]) # adiciona esses valores ao fim da lista
print(lista1)

lista1.insert(2, 'novo valor')
print(lista1)

# juntar 2 lista

lista6 = lista1 + lista2
print(lista6)


#  inverso da lista
print(lista1)
print(lista2)
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)

# apenas imprime inverso
print(lista1[::-1])

# copiar lista

lista7 = lista2.copy()
print(lista7)

# saber tamanho de lista
print(len(lista5))

# remover o ultimo elemento
# pop não só remove como também retorna o valor(pilha)
print(lista5)
lista5.pop()
print(lista5)

# remover elemento pelo indice

print(lista5)
lista5.pop(11)
print(lista5)

# lista11.clear() # apaga tudo da lista

# trnasformar STRING em LISTA

curso = "Samuel Moreira Abreu"
print(curso)
curso = curso.split()
print(curso)

curso2 = "Samuel,Moreira,Abreu"
print(curso2)
curso2 = curso2.split(',')
print(curso2)

# LISTA para STRING

lista8 = ["Samuel", "Moreira" , "Abreu"]
print(lista8)
# pega a lista 8, e entre cada valor, coloque o que esta entre aspas
string1 = '$$'.join(lista8)
print(string1)

# lista circular

cores = ['verde', 'rosa', 'azul', 'magenta']

print(cores[0])
print(cores[1])
print(cores[2])
print(cores[3])
# print(cores[4]) #erro

# roda negativa

print(cores[-1])
print(cores[-2])
print(cores[-3])
print(cores[-4])
# print(cores[-5]) # erro

# retornando o index atráves do valor 
lista_numerada = [11, 30, 93, 74, 565, 26, 57, 82, 19]

print(lista_numerada.index(93))
print(lista_numerada.index(565))
# caso não tenha o valor, será apresentado ERRO
# se tiver mais de um valor, será retornado o index do primeiro!

# soma, minimo, maximo e tamanho

lista_ultima = [1, 2, 3, 4, 5, 6]

print(sum(lista_ultima))
print(min(lista_ultima))
print(max(lista_ultima))
print(len(lista_ultima))

# desempacotamento de listas

lista_ultima2 = [1, 2, 3]

num1, num2, num3 = lista_ultima2

print(num1)
print(num2)
print(num3)