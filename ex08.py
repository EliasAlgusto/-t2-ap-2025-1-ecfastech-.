soma = 0

for i in range(5):
    while True:
        try:
            numero = float(input(f"Número {i+1}: "))
            soma += numero
            break
        except ValueError:
            print("Inválido. Digite um número.")

media = soma / 5

print(f"Soma: {soma}")
print(f"Média: {media:.2f}")


