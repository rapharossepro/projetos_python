#Funções em Python

"""
É um bloco de codigos reutilizável que executa uma tarefa específica
"""
"""
lista = [1,2,3]
lista.append(4) #função = método
print(lista)
"""
"""
1- Organização do código
2- Reutilização de código
3- Facilidade de manutenção
4- Legibilidade
"""
"""
#Prontas x Criadas manualmente
#Criar ==  Declarar uma função
def nome_da_função():
    """ 
    #Bloco de código
"""

def saudação():
    print("Olá, seja bem vindo ao sistema!")

#como eu chamo uma função == invocar 
saudação() #Executa a função
#declaração de função com parâmetro
def boas_vindas(nome):
    print(f"Olá, {nome}! Seja bem-vindo.")

boas_vindas("Fabrício")
boas_vindas("Raphael")
"""
"""

def soma(a,b):
    return a + b

#print(soma(2,2))
resultado = soma(2,3)
print("O resultado é: ", resultado)
"""
"""
def mensagem(texto="Olá, mundo!"):
    print(texto)

mensagem() #Olá, mundo!
mensagem("Bom dia!")
"""

#Escopo de variáveis
#Variável local -> Escopo Local -> existe apenas dentro da função
#Variável Global -> Escopo Global -> definida fora de qualquer função

def teste():
    x = 10 #Local
    print(x)

x = 5 #Global
teste()
print(x)
print(x)
print(x)
print(x)
print(x)