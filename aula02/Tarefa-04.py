# Faca um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informacoes possiveis sobre ele.

n = input("Digite algo: ")
print("O tipo primitivo desse valor e", type(n))
print("So tem espacos?", n.isspace())
print("E um numero?", n.isnumeric())
print("E alfabetico?", n.isalpha())
print("E alfanumerico?", n.isalnum())
print("Esta em maiusculas?", n.isupper())
print("Esta em minusculas?", n.islower())
print("Esta capitalizada?", n.istitle())

# O codigo acima solicita ao usuario que digite algo e, em seguida, exibe o tipo primitivo do valor digitado e diversas informacoes sobre ele.
# As informacoes incluem se o valor tem espacos, se e um numero, se e alfabetico, se e alfanumerico, se esta em maiusculas, minusculas ou capitalizado.
# Essas verificacoes sao feitas usando metodos de string, como isspace(), isnumeric(), isalpha(), isalnum(), isupper(), islower() e istitle().
# O objetivo do programa e fornecer uma visao geral sobre o valor digitado pelo usuario, ajudando a entender melhor o tipo de dado que foi inserido.
# O programa e util para aprender sobre os tipos de dados em Python e como manipular strings.