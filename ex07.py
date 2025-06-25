
maior = None

for i in range(5):
    numero = float(input(f"Digite o {i + 1}º número: "))
    if maior is None or numero > maior:
        maior = numero

print(f"\nO maior número informado foi: {maior}")
