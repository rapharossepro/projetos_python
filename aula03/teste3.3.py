#Pedir um número e calcular o fatorial dele.

numero = int(input("digite um numero: "))

fatorial = 1
for i in range(1, numero + 1):
    fatorial *= i
print(f"O fatorial de {numero} é: {fatorial}")