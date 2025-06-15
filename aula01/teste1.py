## Desafio prático nº 1
# Crie um programa que:

# Pede o nome do usuário

# Pede a idade

# Pede a altura

# Exibe tudo com um print estilizado


nome = input("Qual seu nome? ")
idade = int(input("Qual sua idade? "))
altura = float(input("Qual sua altura? "))
print("\n----- Dados do Usuário -----")
print(f"Nome   : {nome}")
print(f"Idade  : {idade} anos")
print(f"Altura : {altura:.2f} m")
print("----------------------------")