# 🧮 Calculadora Linux e Python

## 📋 Descrição

Este projeto foi desenvolvido como atividade acadêmica com o objetivo de praticar conceitos de programação em **Shell Script (Linux)** e **Python**.

O projeto consiste em uma calculadora simples capaz de realizar as quatro operações matemáticas básicas:

* ➕ Soma
* ➖ Subtração
* ✖️ Multiplicação
* ➗ Divisão

Foram desenvolvidas duas versões da calculadora:

1. **Versão Shell Script (.sh)** para execução em ambiente Linux.
2. **Versão Python (.py)** para execução utilizando o interpretador Python.


# 📁 Estrutura do Projeto

```text
calculadora/
│
├── calculadora.sh
├── calculadora.py
└── README.md
```


# 🛠 Tecnologias Utilizadas

* Linux Ubuntu
* Bash (Shell Script)
* Python 3
* Git
* GitHub
* Visual Studio Code


# 📜 Código Shell Script

Arquivo:

```text
calculadora.sh
```

Funções implementadas:

* Leitura de dados pelo usuário;
* Estruturas condicionais utilizando `case`;
* Operações matemáticas básicas;
* Exibição do resultado na tela.


# 🐍 Código Python

Arquivo:

```text
calculadora.py
```

Funções implementadas:

* Entrada de dados com `input()`;
* Estruturas condicionais (`if`, `elif`, `else`);
* Operações matemáticas básicas;
* Tratamento de divisão por zero;
* Exibição do resultado na tela.


# ▶️ Como Executar o Script Shell (.sh)

## 1. Dar permissão de execução

```bash
chmod +x calculadora.sh
```

## 2. Executar o programa

```bash
./calculadora.sh
```

### Exemplo de execução

```text
===== Calculadora Linux =====

Digite o primeiro número:
10

Digite o segundo número:
5

Escolha a operação (+, -, *, /):
+

Resultado: 15
```


# ▶️ Como Executar o Programa Python

## 1. Verificar se o Python está instalado

```bash
python3 --version
```

## 2. Executar o programa

```bash
python3 calculadora.py
```

### Exemplo de execução

```text
===== Calculadora Python =====

Digite o primeiro número: 20
Digite o segundo número: 4
Escolha a operação (+, -, *, /): /

Resultado: 5.0
```


# 💡 Explicação do Código Python

O programa segue os seguintes passos:

1. Solicita ao usuário dois números.
2. Solicita a operação matemática desejada.
3. Verifica qual operação foi escolhida através de estruturas condicionais.
4. Realiza o cálculo correspondente.
5. Exibe o resultado na tela.
6. Caso o usuário tente dividir por zero, o programa apresenta uma mensagem de erro.

# 🎯 Objetivos de Aprendizagem

Durante o desenvolvimento deste projeto foram praticados os seguintes conceitos:

* Variáveis;
* Entrada e saída de dados;
* Estruturas condicionais;
* Operadores matemáticos;
* Scripts Linux;
* Programação em Python;
* Controle de versão com Git;
* Hospedagem de projetos no GitHub.


# 👩‍💻 Autora

**Laura Joanna**

Projeto desenvolvido para fins acadêmicos e de aprendizagem em programação.

