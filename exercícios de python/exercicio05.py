## Laço com for e lista
# Crie uma lista com quatro nomes. Use um for com enumerate para exibir:
# 1 - Nome1
# 2 - Nome2

nomes = ['João', 'Maria', 'Pedro', 'Ana']

for indice, nome in enumerate(nomes, start=1):
    print(f'{indice} - {nome}')

