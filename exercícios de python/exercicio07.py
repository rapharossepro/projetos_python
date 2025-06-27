##  Função com parâmetro
# Crie uma função tabuada(numero) que exiba a tabuada de multiplicação de 1 a 10 do número informado.

def tabuada(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
numero = int(input("Informe um número para ver sua tabuada: "))
tabuada(numero)         