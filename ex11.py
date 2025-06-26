
inicio = int(input("Digite o primeiro número: "))
fim = int(input("Digite o segundo número: "))

if inicio > fim:
    inicio, fim = fim, inicio

soma = 0
for i in range(inicio + 1, fim):
    print(i)
    soma += i

print(f"Soma dos números: {soma}")
