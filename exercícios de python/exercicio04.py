## Monte um dicionário para armazenar os dados de um produto:
# Nome do produto
# Preço
# Quantidade em estoque
# Depois, exiba os dados formatados e calcule o valor total do estoque do produto.

produto = {}
produto['nome'] = input("Digite o nome do produto: ")
produto['preco'] = float(input("Digite o preço do produto: "))
produto['quantidade'] = int(input("Digite a quantidade em estoque: "))
valor_total = produto['preco'] * produto['quantidade']
print("\nDados do produto:")
print(f"Nome: {produto['nome']}")
print(f"Preço: R$ {produto['preco']:.2f}")
print(f"Quantidade em estoque: {produto['quantidade']}")
print(f"Valor total em estoque: R$ {valor_total:.2f}")

# O código acima cria um dicionário para armazenar os dados de um produto, incluindo nome, preço e quantidade em estoque.
# Em seguida, solicita ao usuário que insira essas informações.
# Após coletar os dados, o programa calcula o valor total do estoque multiplicando o preço pela quantidade.
# Por fim, exibe os dados formatados, incluindo o valor total do estoque com duas casas decimais.
# O dicionário 'produto' é usado para armazenar as informações do produto de forma organizada.
# O uso de dicionários permite fácil acesso e manipulação dos dados do produto.
# O código é útil para gerenciar informações de produtos em um sistema de estoque ou vendas.

