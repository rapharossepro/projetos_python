## Crie uma Tupla com três coordenadas (x, y, z) informadas pelo usuário. Depois:

# Exiba as coordenadas separadamente (uma por linha).

# Mostre o valor da coordenada y.

x = float(input("Digite a primeira coordenada: "))
y = float(input("Digite a segunda coordenada: "))
z = float(input("Digite a terceira coordenada: "))

coordenadas = (x ,y ,z)

print(f"As coordenadas são: x={x}, y={y} e z={z}")
print(coordenadas[1]) #Coordenada 'y'

# declare as variaveis x,y,z recebendo valores pelo teclado(Funcao Input)
# Float pois sao valores com ponto flutuante
# A tupla coordenadas recebe as 3 variaveis
# No final sao mostradas as 3 variaveis e tambem a variavel y