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


# adicionar elementos em um dicionario

receita = {'jan': 100, 'fev':120, 'mar':300}
print(receita)
print(type(receita))

# forma 1 (mais comum)
receita['abr'] = 300
print(receita)

# forma 2 (menos comum)
dado = {'maio':500}
receita.update(dado) # receita.update({'maio':500})
print(receita)

# Atualizando dados em um dicionario

# Forma 1

receita['maio'] = 23
print(receita)
receita.update({'maio': 900})
print(receita)

# conclusão: a fomra de adicionar novos elementos ou atualizar dados em um dicionario é a mesma
# conclusão2: em dicionarios, NÃO podemos ter chaves repetidas

# Remover dados em um dicionario

receita = {'jan': 100, 'fev':120, 'mar':300}
print(receita)
print(type(receita))

# Forma 1 (mais comum)
receita.pop('mar') #obrigatorio passar chave / caso não tenha, retorna erro
print(receita)
ret = receita.pop('jan') # pop retorna o valor quando remove
print(ret)
print(receita)

# forma 2 (menos comum)

del receita['fev']



# Exemplo pratico; Comercio eletronico com carrinhos de compras

# Carrinho de compras:
# Produto1:
#      Nome:
#      Qnt:
#      Preço
# Produto2:
#      Nome:
#      Qnt:
#      Preço

# Utilizando listas
carrinho = []

produto1 = ['God Of War', 1, 230.00]
produto2 = ['Harry Potter', 3, 20.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Usando Tuplas

produto1 = ['God Of War', 1, 230.00]
produto2 = ['Harry Potter', 3, 20.00]

carrinho = (produto1, produto2)
print(carrinho)
# Utilizando dicionarios
carrinho = []
produto1 = {'nome':'God Of War', 'quantidade':1, 'preco':230.00}
produto2 = {'nome':'PS5', 'quantidade':1, 'preco':2530.00}
produto3 = {'nome':'Harry Potter', 'quantidade':2, 'preco':20.00}

carrinho.append(produto1)
carrinho.append(produto2)
carrinho.append(produto3)

print(carrinho)
"""

# Metodos dicionarios

d = dict(a=1, b=2, c=3)
print(d)
print(type(d))

# d.clear()
# print(d)

# forma 1
# novo = d.copy()
# print(novo)

# forma 2
# novo = d
# print(novo)
# novo['d'] = 4
# print(novo)

# não usual de criação de dicionarios com fromkeys

outro = {}.fromkeys('a', 'b')
print(outro)

