print("-"*20)
print("Tabuada Interativa")
numero = int(input("Digite um número e veja a sua tabuada: "))
for i in range(1, 11):
    print("{} X {:2} = {}".format(numero, i, numero*i))