#  Autor: Samuel Moreira Abreu
#  O intuito desse código é revisar os conceitos iniciais de Python para o começo em uma iniciação cientifica.

# tipo inteiro e operadores

variavel_inteiro = int(input())

# soma
print(variavel_inteiro + 1)

# subtracao
print(variavel_inteiro - 1)

# multiplicacao
print(variavel_inteiro * 2)

# divisao
print(variavel_inteiro / 2)

# divisao por inteiro
print(variavel_inteiro // 3)

# modulo (resto da divisao)
print(variavel_inteiro % 3)

# exponenciacao
print(variavel_inteiro ** 2)



# tipo float (ponto flutuante, utiliza PONTO ao inves de VIRGULA)

variavel_float = float(input())

# soma
print(variavel_float + 1.1)

# subtracao
print(variavel_float - 1.1)

# multiplicacao
print(variavel_float * 2.3)

# divisao
print(variavel_float / 2)

# divisao por inteiro
print(variavel_float // 3)

# modulo (resto da divisao)
print(variavel_float % 3.2)

# exponenciacao
print(variavel_float ** 2.5)

# conversao de float para inteiro

variavel_float = 1.44
res = int(variavel_float)
# perde a precisao
print(res)
print(type(res))

# tipo boolean

variavel_boleana = True
print(type(variavel_boleana))
print(variavel_boleana)

# negacao
print(not(variavel_boleana))

variavel_boleana2 = False
# logica OR
print((variavel_boleana or variavel_boleana2)) # retorna true se algum dos valores forem true

# porta logica AND
print(variavel_boleana and variavel_boleana2) # retorna true apenas quando ambas forem true

# tipo string
print ("Aqui abaixo está as variaveis tipo 'String'")

variavel_string = input()

print(f"é uma string: {variavel_string}")
print(type(variavel_string))

print("Para colocar uma aspas duplas dentro de uma string, utilizamos a barra invertida \, nesse caso \" a aspas duplas aparece!")

# uma string é um vetor de caracteres em python, dessa forma, a string com o valor "Samuel" será var['s', 'a', 'm', 'u', 'e', 'l']
var = "samuel"
print(var)
print(type(var))

var += " moreira abreu"

print(var)

print(var[7:21])

# [ 0      ,  1        ,  3]
# ['Samuel', 'moreira' , 'abreu']
print(var.split()[0])

print(var.split()[1:4])

print(f"Variave inteira: {var}")


# escopo de variaveis

# globais = acessiveis em todo o código
# locais = apenas dentro do local onde foi criada, por exemplo, funçoes, condicionais e loops.
