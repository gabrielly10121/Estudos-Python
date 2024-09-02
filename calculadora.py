import math

def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Erro: Divisão por zero!"
    return x / y

def potencia(x, y):
    return x ** y

def raiz_quadrada(x):
    if x < 0:
        return "Erro: Raiz quadrada de número negativo!"
    return math.sqrt(x)

def fatorial(x):
    if x < 0:
        return "Erro: Fatorial de número negativo!"
    return math.factorial(x)

def logaritmo(x, base=10):
    if x <= 0:
        return "Erro: Logaritmo de número não positivo!"
    return math.log(x, base)

def calcular():
    print("Escolha a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Potenciação")
    print("6. Raiz Quadrada")
    print("7. Fatorial")
    print("8. Logaritmo")

    escolha = input("Digite o número da operação (1/2/3/4/5/6/7/8): ")

    if escolha in ['1', '2', '3', '4', '5']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            print(f"{num1} + {num2} = {adicionar(num1, num2)}")
        elif escolha == '2':
            print(f"{num1} - {num2} = {subtrair(num1, num2)}")
        elif escolha == '3':
            print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
        elif escolha == '4':
            print(f"{num1} / {num2} = {dividir(num1, num2)}")
        elif escolha == '5':
            print(f"{num1} ** {num2} = {potencia(num1, num2)}")

    elif escolha == '6':
        num = float(input("Digite o número: "))
        print(f"√{num} = {raiz_quadrada(num)}")

    elif escolha == '7':
        num = int(input("Digite um número inteiro: "))
        print(f"{num}! = {fatorial(num)}")

    elif escolha == '8':
        num = float(input("Digite o número: "))
        base = float(input("Digite a base do logaritmo (padrão é 10): ") or 10)
        print(f"log_{base}({num}) = {logaritmo(num, base)}")

    else:
        print("Operação inválida.")

while True:
    calcular()
    continuar = input("Deseja realizar outra operação? (s/n): ")
    if continuar.lower() != 's':
        print("Encerrando a calculadora.")
        break
