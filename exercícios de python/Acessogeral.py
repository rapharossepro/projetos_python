# Funções dos exercícios

def exercicio_1():
    numeros = []
    for i in range(5):
        n = int(input(f"Digite o {i+1}º número: "))
        numeros.append(n)
    print(f"Soma: {sum(numeros)}")
    print(f"Maior: {max(numeros)}")
    print(f"Menor: {min(numeros)}")

def exercicio_2():
    x = float(input("Digite o valor de x: "))
    y = float(input("Digite o valor de y: "))
    z = float(input("Digite o valor de z: "))
    coordenadas = (x, y, z)
    print("Coordenadas:")
    for c in coordenadas:
        print(c)
    print(f"Coordenada y: {coordenadas[1]}")

def exercicio_3():
    nomes1 = set(input("Digite 3 nomes (1º grupo), separados por espaço: ").split())
    nomes2 = set(input("Digite 3 nomes (2º grupo), separados por espaço: ").split())
    print(f"Nomes em comum: {nomes1 & nomes2}")
    print(f"Nomes em pelo menos um: {nomes1 | nomes2}")

def exercicio_4():
    produto = {}
    produto['nome'] = input("Nome do produto: ")
    produto['preco'] = float(input("Preço: "))
    produto['quantidade'] = int(input("Quantidade em estoque: "))
    total = produto['preco'] * produto['quantidade']
    print(f"Produto: {produto['nome']}")
    print(f"Preço: R${produto['preco']:.2f}")
    print(f"Quantidade: {produto['quantidade']}")
    print(f"Valor total em estoque: R${total:.2f}")

def exercicio_5():
    nomes = []
    for i in range(4):
        nomes.append(input(f"Digite o {i+1}º nome: "))
    for i, nome in enumerate(nomes, start=1):
        print(f"{i} - {nome}")

def linha():
    print("-" * 40)

def exercicio_6():
    linha()
    print("Relatório")
    linha()

def tabuada(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

def exercicio_8():
    def media3(n1, n2, n3):
        return (n1 + n2 + n3) / 3

    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    n3 = float(input("Nota 3: "))
    media = media3(n1, n2, n3)
    print(f"Média: {media:.2f}")
    print("Aprovado!" if media >= 7 else "Reprovado!")

def exercicio_9():
    def disciplinas_comuns(d1, d2):
        return d1 & d2

    d1 = set(input("Disciplinas do aluno 1: ").split())
    d2 = set(input("Disciplinas do aluno 2: ").split())
    comuns = disciplinas_comuns(d1, d2)
    print(f"Disciplinas em comum: {comuns}")

x = 10
def mostra_local():
    x = 20
    print(f"Valor local de x: {x}")

def exercicio_10():
    mostra_local()
    print(f"Valor global de x: {x}")

def desafio_bonus():
    alunos = []
    for i in range(2):
        print(f"\nCadastro do aluno {i+1}")
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        curso = input("Curso: ")
        disciplinas = set(input("Disciplinas (separadas por espaço): ").split())
        aluno = {
            'nome': nome,
            'idade': idade,
            'curso': curso,
            'disciplinas': disciplinas
        }
        alunos.append(aluno)

    for a in alunos:
        print(f"\nAluno: {a['nome']}, Idade: {a['idade']}, Curso: {a['curso']}")
        print(f"Disciplinas: {a['disciplinas']}")

    comuns = alunos[0]['disciplinas'] & alunos[1]['disciplinas']
    print(f"\nDisciplinas em comum: {comuns}")

# Menu de seleção
def menu_exercicios():
    print("\nEscolha um exercício para executar:")
    print("1 - Listas")
    print("2 - Tuplas")
    print("3 - Conjuntos")
    print("4 - Dicionário")
    print("5 - For com Lista")
    print("6 - Função simples (linha)")
    print("7 - Função com parâmetro (tabuada)")
    print("8 - Função com retorno (média)")
    print("9 - Função com conjunto (disciplinas comuns)")
    print("10 - Escopo de variáveis")
    print("11 - Desafio bônus (cadastro de alunos)")
    print("0 - Sair")

    while True:
        opcao = input("\nDigite o número do exercício que deseja rodar: ")
        if opcao == "1":
            exercicio_1()
        elif opcao == "2":
            exercicio_2()
        elif opcao == "3":
            exercicio_3()
        elif opcao == "4":
            exercicio_4()
        elif opcao == "5":
            exercicio_5()
        elif opcao == "6":
            exercicio_6()
        elif opcao == "7":
            num = int(input("Digite um número para ver a tabuada: "))
            tabuada(num)
        elif opcao == "8":
            exercicio_8()
        elif opcao == "9":
            exercicio_9()
        elif opcao == "10":
            exercicio_10()
        elif opcao == "11":
            desafio_bonus()
        elif opcao == "0":
            print("Fechando... Boa prova, campeão! 🍀")
            break
        else:
            print("Opção inválida. Tenta de novo, fera!")

# Chamada final
menu_exercicios()
