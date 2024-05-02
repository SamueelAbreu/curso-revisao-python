#  Autor: Samuel Moreira Abreu
#  O intuito desse código é revisar os conceitos iniciais de Python para o começo em uma iniciação cientifica.

"""
Modulo collections = Default dict

Ao criar um dicionario utilizando o Default dict utilizamos um valor padrão
esse valor será utilizado sempre que não houver valor definido
Caso tentemos acessar um valor inexistente, essa chave será criado e o valor padrão será definido
"""

from collections import defaultdict

# lambdas são funçoes sem nome são funções que podem ou não receber parametros e retornam valores
dicionario = defaultdict(lambda: 'Não encontrado')
print(dicionario)

dicionario['curso'] = 'Programação em python'
print(dicionario)
print(dicionario['outro'])
print(dicionario)


"""
Ordered Dict
é um dicionario que nos garante a ordem de inserção de um elemento

"""

from collections import OrderedDict

dicionario2 = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,}

for chave, valor in dicionario2.items():
     print(f'Chave={chave} e Valor={valor}')

# Dicionarios comuns

diciComum = {'a':1, 'b':2}
dictComum2 = {'b':2, 'a':1}

print(diciComum == dictComum2) # TRUE -> OREDEM NÃO IMPORTA

# Dicionario ordered

diciOrdered = OrderedDict({'a':1, 'b':2})
dictOrdered2 = OrderedDict({'b':2, 'a':1})

print(diciOrdered == dictOrdered2) # FALSE -> ORDEM IMPORTA