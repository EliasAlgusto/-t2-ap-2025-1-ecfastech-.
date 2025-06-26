
n=int(input("Digite o número de termos da série de Fibonacci: "))
fibonacci= [1, 1]  # Inicia com os dois primeiros termos
for _ in range(n - 2):  # Gera os termos restantes
    fibonacci.append(fibonacci[-1] + fibonacci[-2])
print("Série de Fibonacci:", fibonacci)
