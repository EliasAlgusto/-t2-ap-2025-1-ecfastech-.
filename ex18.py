
N=int(input("Quantos números deseja inserir? "))
numeros = []  # Lista para armazenar os números
for _ in range(N):
    num=float(input("Digite um número: "))
    numeros.append(num)

menor_valor = min(numeros)
maior_valor = max(numeros)
soma_valores = sum(numeros)

print(f"Menor valor: {menor_valor}")
print(f"Maior valor: {maior_valor}")
print(f"Soma dos valores: {soma_valores}")

