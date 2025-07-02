
def contar_ocorrencias():
    linhas=int(input("Número de linhas da matriz: "))
    colunas=int(input("Número de colunas da matriz: "))
    matriz= []

    for i in range(linhas):
        linha = []
        for j in range(colunas):
            valor = input(f"Elemento [{i+1}][{j+1}]: ")
            linha.append(valor)
        matriz.append(linha)
    elemento = input("\nDigite o elemento a ser buscado: ")
    contagem = 0

    for linha in matriz:
        for item in linha:
            if item == elemento:
                contagem += 1

    print(f"\n📊 O elemento '{elemento}' aparece {contagem} vez(es) na matriz)

contar_ocorrencias()
