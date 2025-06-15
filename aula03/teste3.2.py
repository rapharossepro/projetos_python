#Faça um programa que:
#Peça um número inteiro positivo n
#Calcule a soma de todos os números de 1 até n
#Mostre o resultado final

numero = int(input("Digite um número inteiro positivo: "))
soma = 0
for i in range(1, numero + 1):
    soma += i
print("A soma de todos os números de 1 até", numero, "é:", soma)

#O código acima pede um número inteiro positivo ao usuário e calcula a soma de todos os números de 1 até esse número.
# A variável 'soma' é inicializada com 0 e, em seguida, um laço 'for' percorre os números de 1 até o número fornecido.
# A cada iteração, o valor de 'i' é adicionado à variável 'soma'.
# Após o laço, o resultado final é impresso na tela.