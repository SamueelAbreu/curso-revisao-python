#  Autor: Samuel Moreira Abreu
#  O intuito desse código é revisar os conceitos iniciais de Python para o começo em uma iniciação cientifica.

# loop for


"""
C++
for(int i = 0; i<tam; i++){
     ....
}

python:
for item in intervalo:
     .....

"""

nome = 'Geek university'
lista = [1, 2, 3, 4, 5, 6]
numeros = range (1, 10)
print("-------------------")
# iterando sobre string
for letra in nome:
     print(letra)
print("-------------------")
# iterando sobre lista
for numero in lista:
     print(numero)
print("-------------------")
# iterando sobre um range
for numero in range(1, 10):
     print(numero)

print("-------------------")
# Enumerate: (atribui um valor para cada letra)
# ((0, 'G'), (1 , 'e'), (2, 'e'), (3, 'k') ....)
# i = 0, 1, 2, e V = 'G', 'e', 'e', 'k'....
for i, v in enumerate(nome):
     print(nome[i])

print("-------------------")
for valor in enumerate(nome):
     print(valor)
print("-------------------")
qnt = int(input("Quantas vezes esse loop deve rodar?"))

soma = 0

for n in range(1, qnt+1):
     num = int(input(f"Informe o {n}/{qnt} valor: "))
     soma += num
print(f"A soma é {soma}!")

print("-------------------")

for letra in nome:
     # para não pular linha ao fim do print! end = ''
     print(letra, end='')

print("\n -------------------")
print("Printando um emogi")

# emogi = U+1F60D 
# emogi modificado = U0001F60D

for num in range (1, 11):
     print('\U0001F60D' * num)
