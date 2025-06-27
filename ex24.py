
notas= []
N=int(input("Quantas notas deseja inserir? "))


for _ in range(N):
    nota = float(input("Digite uma nota: "))
    notas.append(nota)
media = sum(notas) / N
print(f"A média aritmética das notas é: {media:.2f}")

menor_valor = min(numeros)
maior_valor = max(numeros)
soma_valores = sum(numeros)

print(f"Menor valor: {menor_valor}")
print(f"Maior valor: {maior_valor}")
print(f"Soma dos valores: {soma_valores}")
