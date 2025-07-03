
def encontrar_extremos():
    linhas= int(input("Digite o número de linhas da matriz: "))
    colunas= int(input("Digite o número de colunas da matriz: "))
    matriz= []

    for i in range(linhas):
        linha = []
        for j in range(colunas):
            valor=float(input(f"Elemento [{i+1}][{j+1}]: "))
            linha.append(valor)
        matriz.append(linha)

    maior= menor = matriz[0][0]  # Inicializa com o primeiro valor

    for linha in matriz:
        for valor in linha:
            if valor > maior:
                maior = valor
            if valor < menor:
                menor = valor

    print(f"\n Maior elemento da matriz: {maior}")
    print(f" Menor elemento da matriz: {menor}")
