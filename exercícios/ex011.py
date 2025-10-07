l = float(input("Largura da parede: "))
a = float(input("Altura da parede: "))
soma = l * a
print("Sua parede tem a dimensão de {}x{} e sua área é de {:.1f}m².".format(l, a, soma))
print("Para pintar essa parede, você precisará de {:.1f} litros de tinta.".format(soma/2))