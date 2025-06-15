## Pede o nome e a nota final de um aluno (entre 0 e 10)

# Imprime se ele está:

# Reprovado se a nota for < 5

# Em recuperação se for >= 5 e < 7

# Aprovado se for >= 7

nota_final = float(input("Digite a nota final do aluno: "))

if nota_final < 5:
    print("Reprovado")
elif nota_final < 7:
    print("Em recuperação")
else:
    print("Aprovado")