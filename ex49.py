
def gerar_serie(n):
    soma = 0
    print("Série gerada:")
    for i in range(1, n+1):
        denominador = 2 * i - 1
        termo = i / denominador
        soma += termo
        print(f"{i}/{denominador}", end="  ")
    print(f"\n\n Soma da série: {soma:.2f}")

n = int(input("Digite o número de termos da série: "))
gerar_serie(n)
