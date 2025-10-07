print("-"*20)
senha = input("Digite sua senha: ")

if len(senha) < 8:
    print("Senha muito curta! Use pelo menos 8 caracteres.")
elif senha.isalpha():
    print("Adicione números à sua senha.")
elif senha.isdigit():
    print("Adicione letras à sua senha.")
else:
    print("Senha aceita!")