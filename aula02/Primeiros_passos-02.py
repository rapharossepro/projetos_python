## Tipos Primitivos, int, float, str, bool
# Exemplos: 
# int(1,7,-5,-10) Representa os numeros inteiros, positivos e negativos/ 
# float(4.5, 0.076, -15.223) Representa os numeros reais, positivos e negativos com ponto flutuante.
# str("Ola mundo!, Rapha, DevOps, Python") Representa as strings, ou seja, textos e esta sempre entre aspas simples ou duplas.
# bool(True, False) -> Sempre retorna verdadeiro ou falso, ou seja, se a condicao for verdadeira ou falsa.

print("DevOps Academy - Python")
soma = int(input("digite um numero: ")) + int(input("Digite outro numero: ")) # deixando o codigo mais linear e legivel.
print("O resultado da operacao e: {}".format(soma))
print(f'O resultado da operacao e: {soma}\n') 
# Outra forma de fazer a mesma coisa.
# f-string, mais moderno e recomendado. 
# f-strings permitem interpolacao de variaveis diretamente na string, tornando o codigo mais legivel e facil de entender.

# Primeiro exemplo
n1 = input("Digite novamente um numero: ")
n2 = input("digite mais um numero: ")
soma = n1 + n2
print("A soma entre os numeros e:", soma)
print(f"A soma entre os numeros e: {soma}")
print("A soma entre os numeros e: {}\n".format(soma))

# Erro proposital, pois input retorna uma string, e nao um numero inteiro.
# Para resolver isso, devemos converter as strings para int ou float antes de realizar a operacao.

# Corrigindo o erro
n10 = int(input("Digite um numero: "))
n20 = int(input("Digite outro numero: "))
soma = n10 + n20
print("A soma entre os numeros e:", soma)
print(f"A soma entre os numeros e: {soma}")
print("A soma entre os numeros e: {}\n".format(soma))


# if condicao:
    # se for verdadeiro, roda isso
#elif outra_condicao:
    # se a primeira não for, testa essa
# else:
    # se nenhuma for, roda isso

idade = int(input("Qual sua idade? "))

if idade >= 18:
    print("Você é maior de idade.")
elif idade >= 12:
    print("Você é um adolescente.")
else:
    print("Você é uma criança.")
