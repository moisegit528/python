import random
nome1 = str(input("Aluno 1: "))
nome2 = str(input("Aluno 2: "))
nome3 = str(input("Aluno 3: "))
nome4 = str(input("Aluno 4: "))
nomes = [nome1, nome2, nome3, nome4]
escolhido = random.choice(nomes)
print("O aluno escolhido é {}!".format(escolhido))