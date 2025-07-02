
numero=input("Digite um número inteiro positivo: ")

if numero.isdigit():
    invertido = numero[::-1]
    print(f"Número invertido: {invertido}")
else:
    print("Entrada inválida. Digite um número positivo.")
