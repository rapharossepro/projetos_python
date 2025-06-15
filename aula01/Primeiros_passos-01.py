nome = 'Fulano de Tal'
idade = 20
peso = 94.0
print(f'{nome} tem {idade} anos e pesa {peso} Kg')

nome2 = input('Qual é o seu nome? ')
idade2 = int(input('Qual é a sua idade? '))
peso2 = float(input('Qual é o seu peso? '))
print(f"{nome2} tem {idade2} anos e pesa {peso2} kg")

if peso2 >= 100:
    print("Voce esta obeso, seu leitao!")
elif peso2 <= 99:
    print("Voce esta quase gordo, sua baleia!")
elif peso2 <= 70:
    print("Voce esta no peso ideal, depende do seu tamanho!")
else:
    print("voce tem que se alimentar direito, seu chassi de grilo!")


    ## Nesse projeto, aprendi como utilizar o print, input, declarar variaveis, atribuir valores a variaveis utilizando o recebe, como mostrar essas variaveis na tela com o print
    ## e como utilizar a estrutura condicional if, elif e else para verificar as condicoes solicitadas pelo usuario.
    ## Tambem aprendi a utilizar o f-string para formatar strings com variaveis dentro delas.
    ## Tambem aprendi a utilizar o int e float para converter os valores de entrada do usuario para numeros inteiros e flutuantes.
    ## Tambem aprendi a utilizar o operador de comparacao >=, <= e == para comaparar os valores das variaveis.
    ## Tambem aprendi a utilizar o operador de atribuicao = para atribuir valores as variaveis.

# int (número inteiro)
idade = 33

# float (número decimal)
peso = 87.5

# str (texto)
nome = "Raphael"

# bool (lógico)
tem_certificacao = True

# Exibindo os valores com print
print("Nome:", nome)
print("Idade:", idade)
print("Peso:", peso)
print("Tem certificação?", tem_certificacao)
