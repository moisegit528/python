def somar(a,b):
    return a + b
def subtrair(a,b):
    return a - b
def multiplicar(a, b):
    return a * b
def dividir(a, b):
    if b == 0:
        return "Erro: Não pode ser feita a divisão por zero"
    return a / b

print("Calculadora simples")
print("Escolha a operação que deseja:")
print("1 - Soma")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Divisão")

usuario = input("Digite a operação desejada: ")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if usuario == "1":
    print("Resultado:", somar(num1, num2))
elif usuario == "2":
    print("Resultado:", subtrair(num1, num2))
elif usuario == "3":
    print("Resultado:", multiplicar(num1, num2))
elif usuario == "4":
    print("Resultado:", dividir(num1, num2))
else:
    print("Opção inválida.")