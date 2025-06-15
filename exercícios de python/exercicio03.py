## Crie dois conjuntos de nomes (com pelo menos 3 nomes cada), digitados pelo usuário. Depois:

# Mostre os nomes que aparecem nos dois conjuntos.

# Mostre os nomes que aparecem em pelo menos um dos conjuntos (união).
print("Digite os 3 nomes do primeiro conjunto:\n")
nome1 = (input("Digite o primeiro nome: "))
nome2 = (input("Digite o segundo nome: "))
nome3 = (input("Digite o terceiro nome: "))

print("Digite os 3 nomes do segundo conjunto:\n")
nome4 = (input("Digite o quarto nome: "))
nome5 = (input("Digite o quinto nome: "))
nome6 = (input("Digite o sexto nome: "))

conjunto1 = {nome1 , nome2 , nome3}
conjunto2 = {nome4 , nome5 , nome6}

uniao = conjunto1 | conjunto2

print(f'{nome1}, {nome2}, {nome3}, {nome4}, {nome5}, {nome6}\n')
for nome in uniao:
    print(nome)

