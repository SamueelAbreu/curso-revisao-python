#  Autor: Samuel Moreira Abreu
#  O intuito desse código é revisar os conceitos iniciais de Python para o começo em uma iniciação cientifica.

"""
Deque -> listas de alta performace


"""

from collections import deque

deq = deque('geek')

print(deq)

# Adicionando elementos

deq.append('y')
print(deq)

deq.appendleft('k') # adiciona no começo
print(deque)

# remove elementos 

print(deq.pop()) # remove e retorna o ultimo elemento

print(deq)

print(deq.popleft()) # remove e retorna o elemento do inicio
print(deq)
