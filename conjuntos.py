#  Autor: Samuel Moreira Abreu
#  O intuito desse código é revisar os conceitos iniciais de Python para o começo em uma iniciação cientifica.

"""
Conjuntos faz referencia a teoria dos conjuntos da matematica 

Em python conjuntos são chamados de SETS

Sets não possuem valores duplicados
Sets não possuem valores ordenados
Sets não são acessiveis via indice


Sets são referenciados com {}
Diferença entre Sets e Mapas

     - Dicionarios possuem chaves
     - Sets tem apenas o valor
"""

# definindo um conjuto

# forma 1

s = set({1, 2, 3, 4, 5, 6, 6, 7, 8, 8}) # valores duplicados não serão impressos e não apresetará erro
print(s)
print(type(s))
s.add(4)
print(s)
s.remove(5)
print(s)
s.discard(3)
print(s)

# deep copia
novo = s.copy()
print(novo)

# shallow copy
novo1 = s
novo1.add(22323)
print(novo1)
print(s)

# Concatenando conjuntos metodo UNION
estudantes_java = {'maria', 'pedro', 'carlos', 'thaigo', 'ryan'}
estudantes_python = {'ricado', 'mario', 'ryan', 'pedro', 'jose', 'matheus'}
unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)

# Concatenando utilizando o caractere PIPE '|'

unicos2 = estudantes_python | estudantes_java
print(unicos2)

# Apenas os que estão em ambos cursos (interseção)
ambos1 = estudantes_java.intersection(estudantes_python)
print(ambos1)

ambos2 = estudantes_python & estudantes_java
print(ambos2)

# Diferença
so_python = estudantes_python.difference(estudantes_java)
print(so_python)
# Diferença
so_java = estudantes_java.difference(estudantes_python)
print(so_java)

# soma, max, min, tam

s1 = {1,2,3,4,5,6}
print(max(s1))
print(min(s1))
print(len(s1))
print(sum(s1))