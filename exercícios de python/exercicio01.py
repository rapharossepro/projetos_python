# Crie uma lista com cinco números digitados pelo usuário. Depois:
# Exiba a soma desses números.
# Exiba o maior e o menor número.

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
n3 = int(input("Digite o terceiro numero: "))
n4 = int(input("Digite o quarto numero: "))
n5 = int(input("Digite o quinto numero: "))

numeros = [n1 , n2 , n3 , n4 , n5]

soma = sum(numeros)
maior = max(numeros)
menor  = min(numeros)

print(f"O maior numero é {maior}, o menor número é {menor} e a soma entre todos eles é: {soma}")