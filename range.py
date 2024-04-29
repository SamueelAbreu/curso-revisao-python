#  Autor: Samuel Moreira Abreu
#  O intuito desse código é revisar os conceitos iniciais de Python para o começo em uma iniciação cientifica.

# Entendendo o funcionamento da função range(), precisamos ter conhecimentos sobre o FOR para utiliza-lo, e é bom conhecer o RANGE para trabalhar com FOR

"""
Forma #1

range(valor de-parada)

comeca em 0 e vai ate valor-de-parada -1


for num range(10)
     print(num)

Forma #2     
     
range(valor de inicio, valor de parada)
     
começa no valor de inicio e para no valor de parada -1
     
for num in range(5, 11)


Forma #3

range(valor de inicio, valor de parada, passo ou saltos)

for num in range(10, -1, -2)
     print(num) = 10, 8, 6, 4, 2, 0
"""

for num in range(10, -1, -2):
     print(num)