
def contar_palavras(texto):
    palavras=texto.strip().split()
    total=len(palavras)
    print(f" Total de palavras: {total}")

entrada = input("Digite uma frase: ")
contar_palavras(entrada)
