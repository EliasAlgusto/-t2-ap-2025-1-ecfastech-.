
def calcular_serie(n):
    soma = 0
    print("Termos da série:")

    for i in range(1, n + 1):
        denominador = 2 * i - 1
        termo = i / denominador
        soma += termo
        print(f"{i}/{denominador}", end="  ")

    print(f"\n\n Soma da série com {n} termos: {soma:.4f}")

# Executar o programa
n = int(input("Digite a quantidade de termos da série: "))
if n > 0:
    calcular_serie(n)
else:
    print("O valor precisa ser um número inteiro positivo.")
