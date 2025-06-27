
# 🐍 Exercícios de Python — Estruturas e Funções

Este projeto contém uma coleção de exercícios didáticos resolvidos em Python, voltados ao estudo de estruturas de dados e funções. O objetivo é treinar conceitos fundamentais da linguagem de forma prática, com exemplos que simulam contextos reais de uso em provas, projetos e aplicações simples.

---

## 📘 Descrição dos Exercícios

### 1️⃣ Listas
Criação de uma lista com 5 números informados pelo usuário. Em seguida:
- Exibe a **soma** dos números usando `sum()`
- Mostra o **maior** valor com `max()`
- Mostra o **menor** valor com `min()`

### 2️⃣ Tuplas
Recebe 3 valores representando as coordenadas **(x, y, z)**:
- Armazena em uma tupla
- Imprime cada valor em uma linha
- Mostra apenas a coordenada `y` (índice 1)

### 3️⃣ Conjuntos
Recebe dois grupos de nomes informados pelo usuário:
- Armazena como `set()`
- Exibe nomes em **comum** (interseção com `&`)
- Exibe nomes presentes em **pelo menos um** grupo (união com `|`)

### 4️⃣ Dicionário
Cria um dicionário com dados de um produto:
- Nome, preço e quantidade
- Calcula o **valor total em estoque**
- Imprime os dados formatados

### 5️⃣ Laço com `for` e `enumerate`
Lê 4 nomes e os imprime numerados:
- Usa `enumerate(lista, start=1)` para indexação personalizada

### 6️⃣ Função simples (sem parâmetro, sem retorno)
Define a função `linha()` que imprime uma linha de 40 traços:
- Usada antes e depois de imprimir a palavra **"Relatório"**

### 7️⃣ Função com parâmetro
Cria a função `tabuada(numero)` que:
- Recebe um número e exibe sua tabuada de 1 a 10

### 8️⃣ Função com retorno
Define a função `media3(n1, n2, n3)` que:
- Calcula a média de três notas
- Retorna o resultado
- Mostra se o aluno está **aprovado** ou **reprovado**

### 9️⃣ Função com conjunto
Define a função `disciplinas_comuns(d1, d2)` que:
- Recebe dois conjuntos
- Retorna as disciplinas em comum entre dois alunos

### 🔟 Escopo de variáveis
Trabalha com variáveis **local** e **global**:
- Cria uma variável global `x = 10`
- Dentro da função `mostra_local()`, cria um `x = 20` (local)
- Mostra os dois valores para comparar escopo

---

## 🎯 Desafio Bônus — Cadastro de Alunos

- Pede os dados de **2 alunos**: nome, idade, curso e disciplinas (como conjunto)
- Armazena os dados em dicionários e adiciona numa lista
- Exibe os dados de cada aluno
- Mostra as disciplinas em comum entre eles (interseção)

---

## ▶️ Como Executar o Menu Geral

1. Abra o terminal na pasta do projeto
2. Execute o arquivo principal:

```bash
python Acessogeral.py
```

3. Escolha o número do exercício que deseja rodar no menu interativo.

---

## 🧠 Habilidades Envolvidas

- Uso de estruturas: **listas, tuplas, dicionários, conjuntos**
- Manipulação de dados com **input()**, **print()**, **format()**
- Criação de funções com ou sem parâmetros/retorno
- Laços de repetição e escopo de variáveis
- Modularização e organização de código Python

---

## 👨‍💻 Autor

[Raphael Del Rosse](https://github.com/rapharossepro)  
Estudante de Análise e Desenvolvimento de Sistemas  
Foco em Cloud, DevOps, Python e automação.

---
