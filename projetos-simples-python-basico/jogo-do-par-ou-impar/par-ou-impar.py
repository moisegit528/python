import random
print("-"*20)
print("Jogo do Par ou Ímpar")
usuario = int(input("Digite um número: "))
computador = random.randint(0, 10)
total = usuario + computador
print("Você jogou {} e computador {}  total = {}".format(usuario, computador, total))
if total % 2 == 0:
    resultado = "PAR"
else:
    resultado = "ÍMPAR"

escolha = input("Você escolhe PAR ou ÍMPAR? ").strip().lower().upper()
if (resultado == "PAR" and escolha == "PAR") or (resultado == "ÍMPAR" and escolha == "ÍMPAR"):
    print("Você VENCEU!")
else:
    print("Você PERDEU")