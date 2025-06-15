## Laços de repetição servem pra executar um bloco de código várias vezes. Você pode repetir:
#Um número fixo de vezes (for)

#nquanto uma condição for verdadeira (while)

for i in range(6):
    print(i)
# A função range() gera uma sequência de números. O for percorre essa sequência.
# O range(6) gera os números de 0 a 5 (6 não é incluído).
# Você pode especificar o início e o fim da sequência:

for i in range(2, 6):
    print(i)

    contador = 1
while contador <= 5:
    print("Contando:", contador)
    contador += 1
