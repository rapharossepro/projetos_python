## Função com conjunto
# Crie uma função disciplinas_comuns(d1, d2) que receba dois conjuntos de disciplinas e retorne o conjunto com as disciplinas em comum. Mostre o resultado no programa principal.

def disciplinas_comuns(d1, d2):
    return d1.intersection(d2)
d1 = {"Matemática", "Português", "História"}
d2 = {"Biologia", "História", "Química"}
print("Disciplinas em comum:", disciplinas_comuns(d1, d2))