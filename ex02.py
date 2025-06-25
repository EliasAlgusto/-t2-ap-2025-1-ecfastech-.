
while True:
    usuario = input("Qual o seu nome? ")
    senha = input("Crie uma senha: ")


    if senha == usuario:
        print("A senha não pode ser igual ao nome de usuário. Tente de novo!")
    else:
        print("Cadastro feito! Seja bem-vindo(a)!")
        break
