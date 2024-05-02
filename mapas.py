##  Autor: Samuel Moreira Abreu
#  O intuito desse código é revisar os conceitos iniciais de Python para o começo em uma iniciação cientifica.

"""
Iterar sobre dicionarios

receita = {'jan':100, 'fev':250, 'mar':500}

print(receita)
for chave in receita:
     print(receita[chave])

for chave in receita:
     print(f'Em {chave} recebi R$ {receita[chave]}')

# Acessando chaves
print(receita.keys())
# Acesando os valores
for chave in receita.keys():
     print(receita[chave])

receita.values()

for valor in receita.values():
     print(valor)

for chave, valor in receita.items():
     print(f'chave={chave} e valor={valor}')

# Soma, Max, Min, Tam
print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))


"""

receita = {'jan':100, 'fev':250, 'mar':500}

print(receita)
for chave in receita:
     print(receita[chave])

for chave in receita:
     print(f'Em {chave} recebi R$ {receita[chave]}')

# Acessando chaves
print(receita.keys())
# Acesando os valores
for chave in receita.keys():
     print(receita[chave])

receita.values()

for valor in receita.values():
     print(valor)

for chave, valor in receita.items():
     print(f'chave={chave} e valor={valor}')

# Soma, Max, Min, Tam
print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))