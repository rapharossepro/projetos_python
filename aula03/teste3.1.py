## Faça um programa que:
# Peça um número inteiro positivo
# Mostre a tabuada completa desse número de 1 a 10

numero = int(input("Digite um número inteiro positivo: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")