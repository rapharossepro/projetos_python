# Pedir um número e informar se ele é primo ou não.

numero = int(input("Digite um número: "))
if numero <= 1:
    print(f"{numero} não é um número primo.")
else:
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            print(f"{numero} não é um número primo.")
            break
    else:
        print(f"{numero} é um número primo.")

# O código acima verifica se um número é primo.
# Um número é considerado primo se for maior que 1 e não tiver divisores além de 1 e ele mesmo.
# O programa pede ao usuário para digitar um número.
# Se o número for menor ou igual a 1, ele não é primo.



