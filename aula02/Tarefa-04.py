# Faca um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informacoes possiveis sobre ele.

numero = input("Digite algo: ")
print("O tipo primitivo desse valor e", type(numero))
print("So tem espacos?", numero.isspace())
print("E um numero?", numero.isnumeric())
print("E alfabetico?", numero.isalpha())
print("E alfanumerico?", numero.isalnum())
print("Esta em maiusculas?", numero.isupper())
print("Esta em minusculas?", numero.islower())
print("Esta capitalizada?", numero.istitle())

# O codigo acima solicita ao usuario que digite algo e, em seguida, exibe o tipo primitivo do valor digitado e diversas informacoes sobre ele.
# As informacoes incluem se o valor tem espacos, se e um numero, se e alfabetico, se e alfanumerico, se esta em maiusculas, minusculas ou capitalizado.
# Essas verificacoes sao feitas usando metodos de string, como isspace(), isnumeric(), isalpha(), isalnum(), isupper(), islower() e istitle().
# O objetivo do programa e fornecer uma visao geral sobre o valor digitado pelo usuario, ajudando a entender melhor o tipo de dado que foi inserido.
# O programa e util para aprender sobre os tipos de dados em Python e como manipular strings.