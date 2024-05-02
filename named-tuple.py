#  Autor: Samuel Moreira Abreu
#  O intuito desse código é revisar os conceitos iniciais de Python para o começo em uma iniciação cientifica.

"""
Tupla Nomeada 
tupla = (1, 2, 3)
print(tupla[1])

Named Tupla -> São tuplas diferenciadas onde nomeamos especificamente um nome para a mesma e tambem parametros

"""


from collections import namedtuple

# Forma 1

cachorro = namedtuple('cachorro', 'idade nome raca')

# forma 2 
cachorro = namedtuple('cachorro', 'idade, nome, raca')

# forma 3

cachorro = namedtuple('cachorro', ['idade','nome', 'raca'])

ray = cachorro(idade=2, nome='Bender', raca='Belgian Sharped Dog')
print(ray)
# forma 1
print(ray[0])
print(ray[1])
print(ray[2])

# forma 2

print(ray.idade)
print(ray.raca)
print(ray.nome)