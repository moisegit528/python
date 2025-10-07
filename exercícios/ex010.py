real = float(input("Quanto dinheiro você tem na carteira? R$"))
dolar = real / 6.15
euro = real / 6.39
print("Com R${} reais você pode comprar US${:.2f} doláres".format(real, dolar))
print("Com R${} reais você pode comprar US${:.2f} euros".format(real, euro))