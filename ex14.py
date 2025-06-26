
pares = 0
impares = 0


for _ in range(10):  # Loop para solicitar 10 números
    num = int(input("Digite um número inteiro: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1


print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
