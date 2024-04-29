#  Autor: Samuel Moreira Abreu
#  O intuito desse código é revisar os conceitos iniciais de Python para o começo em uma iniciação cientifica.

# Recebendo os dados do usuario

# todo dado recebido via input é STRING!!!
print("Qual seu nome?")
nome = input() # entrada de dados e adicionando a entrada a uma variavel
print("Qual sua idade?")
idade = input()

#                                             conversao de string para inteiro: int(variavel).metodo()   
#print(f"Seja bem vinda {nome.upper()}, voce tem {int(idade).__add__(1)} anos?")
#print(f"Voce nasceu em {2024 - int(idade).__add__(134)}")

print(f"Seja bem vindo(a) {nome.upper()}, voce tem {int(idade)} anos!")
print(f"Voce nasceu em {2024 - int(idade)} ou em {2024 - (int(idade)+1)}?")