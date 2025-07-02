
def calcular_serie_harmonica(n):
    h = 0
    for i in range(1, n + 1):
        h += 1 / i
    print(f"Valor de H com {n} termos: {h:.4f}")

N = int(input("Digite o número de termos da série harmônica (N): "))
if N > 0:
    calcular_serie_harmonica(N)
else:
    print(" Por favor, insira um número inteiro positivo.")
