print ("===== Calculadora Inteligente =====")
num1 = float(input("Digite um valor para o primeiro número:"))
num2 = float(input("Digite um valor para o segundo número:"))

operacao = input("Escolha qual a operação irá fazer: +,-,*,/ :")

if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if num2 != 0:
        resultado = num1/num2
    else:
        print ("Erro: Não é possivel a divisão ser feita por zero!")
        exit ()
else:
    print ("Operação inválida!")
    exit()

    print ("Resultado da operação:",resultado)