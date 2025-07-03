

def inverter_linhas():
    linhas=int(input("Digite o número de linhas da matriz: "))
    colunas=int(input("Digite o número de colunas da matriz: "))
    
    matriz = []

    for i in range(linhas):
        linha = []
        for j in range(colunas):
            valor = input(f"Elemento [{i+1}][{j+1}]: ")
            linha.append(valor)
        matriz.append(linha)

    matriz_invertida = matriz[::-1]

    print("\n Matriz com linhas invertidas:")
    for linha in matriz_invertida:
        print(" ".join(str(item) for item in linha))

inverter_linhas()
