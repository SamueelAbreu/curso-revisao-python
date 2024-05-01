#  Autor: Samuel Moreira Abreu
#  O intuito desse código é revisar os conceitos iniciais de Python para o começo em uma iniciação cientifica.
"""

Dicionarios são conhecidos por mapas

Dicionarios são coleções do tipo chave/valor

Dicionarios são representados por chaves {}

print(type{})

OBS: 
     - Chaves e Valor são separados por ':' (dois pontos)
     - Tanto chave quanto valor podem ser de qualquer tipo de dados
     - podemos misturar quaisquer tipos de dados

# Criação de dicionarios
# forma #1 mais comum
paises = {'br' : 'Brasil', 'eua': 'estados unidos', 'tv':'tuvalu', 'uk': 'ucrania'}

print(paises)
print(type(paises))

# forma #2 menos comum

paises2 = dict(br='brasil', eua='estados unidos')

print(paises2)
print(type(paises2))

# acessando elementos

paises = {'br' : 'Brasil', 'eua': 'estados unidos', 'tv':'tuvalu', 'uk': 'ucrania'}

# forma 1, acesso via chave, da mesma forma que lista/tupla

print(paises['br'])
print(paises['eua'])
# print(paises['ru']) erro!

# forma 2 acessando via get (recomendada)

print(paises.get('br'))
print(paises.get('ru')) # dessa forma não apresenta erro!


# Podemos definir um valor padrão para caso não encontremos com a chave informada

paises = {'br' : 'Brasil', 'eua': 'estados unidos', 'tv':'tuvalu', 'uk': 'ucrania'}

pais = paises.get('ca', 'Não encontrado')

print(f"Enocntrei o pais {pais}")

# podemos verificar se tal valor está no dicionario SOMENTE atraves da chave

print('br' in paises)
print('ca' in paises)
print('Brasil' in paises) # Brasil não é chave, mas sim valor!

if 'ru' in paises:
     russia = paises['ru']

# Podemos utilizar qualquer tipo de dados, inclusive listas, duplas e dicionarios como chaves de dicionarios!
# Tuplas por exemplo são bastante interessantes de serem utilizadas como chaves de dicionarios pois as mesmas são imutaveis
localidades = {
     (35.00, 34.99): 'Escritorio em Tókio',
     (53.00, 24.99): 'Escritorio em Nova York',
     (43.00, 14.99): 'Escritorio em São Paulo',
}

print(localidades)
print(type(localidades))
"""


# adicionar elementos em um dicionario



