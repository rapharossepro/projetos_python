## Função com retorno
# Crie uma função media3(n1, n2, n3) que calcule e retorne a média de três notas. O programa deve exibir se o aluno está aprovado (média ≥ 7) ou reprovado.

def media3(n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    return media    
n1 = float(input("Informe a primeira nota: "))
n2 = float(input("Informe a segunda nota: "))
n3 = float(input("Informe a terceira nota: "))
media = media3(n1, n2, n3)
if media >= 7:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")