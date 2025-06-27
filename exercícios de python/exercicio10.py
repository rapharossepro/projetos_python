##  Escopo de variáveis
# Crie um programa que tenha uma variável global x = 10. 
# Faça uma função mostra_local() que crie uma variável x = 20 local e exiba o valor. 
# Depois, fora da função, exiba novamente o valor de x.

x = 10  # Variável global

def mostra_local():
    x = 20  # Variável local
    print("Valor de x dentro da função:", x)

mostra_local()
print("Valor de x fora da função:", x)

# A função mostra_local() exibe o valor da variável local x, que é 20.
# Fora da função, o valor de x é 10, pois a variável global não foi alterada.
# Isso demonstra o escopo de variáveis em Python, onde variáveis locais e globais podem ter o mesmo nome,
# mas são tratadas de forma diferente dependendo do contexto.