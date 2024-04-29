##  Autor: Samuel Moreira Abreu
#  O intuito desse código é revisar os conceitos iniciais de Python para o começo em uma iniciação cientifica.


# if, else e elif

print("Digite uma nota:")
var = int(input())
print("Digite mais uma nota:")
var2 = int(input())
print("Digite outra nota:")
var3 = int(input())

media_simples = (var + var2 + var3) / 3

print(f"Media simples: {media_simples}")

media_ponderada = ((var*1) + (var2*3) + (var3*6)) / 10 

print(f"Media ponderada(peso: 10): {media_ponderada}")

print("---Resultado media simples----")
if media_simples >= 6:
     print(f"Aprovado - Nota: {media_simples}")
elif media_simples < 6 and media_simples >= 4:
     print(f"Recuperacao - Nota: {media_simples}")
else:
     print(f"Reprovado - Nota: {media_simples}")



print("---Resultado media ponderada----")
if media_ponderada >= 6:
     print(f"Aprovado - Nota: {media_ponderada}")
elif media_ponderada < 6 and media_ponderada >= 4:
     print(f"Recuperacao - Nota: {media_ponderada}")
else:
     print(f"Reprovado - Nota: {media_ponderada}")

