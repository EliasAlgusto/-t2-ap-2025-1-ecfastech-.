 
while True:
    try:
        nota = float(input("Digite uma nota de 0 e 10:"))


        if 0 <= nota <= 10:
            print(f"Nota válida: {nota}")
            break
        else:
            print("Erro: Nota fora do limite (0 a 10).")
    except ValueError:
        print("Erro: Digite um número.")
