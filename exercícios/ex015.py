dias = int(input("Quantos dias alugados? "))
km = float(input("Quantos Km rodados? "))
soma = (dias * 60) + (km * 0.15) # por km rodados
print("O total a pagar é de R${:.2f}".format(soma))