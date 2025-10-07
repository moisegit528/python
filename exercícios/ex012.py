preco = float(input("Qual é o preço do produto? R$"))
calculo = (preco * 5)/100 # or soma = preco - (preco * 5/100)
soma = preco - calculo
print("O produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}".format(preco, soma))