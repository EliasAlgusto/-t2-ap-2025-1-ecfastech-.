
num = int(input("Digite um número inteiro: "))
fatorial = 1
print(f"ENGENHARIA DE COMPUTAÇÃO\nFatorial de: {num}")

for i in range(num, 0, -1):
    fatorial *= i
print(f"{num}! = {' . '.join(map(str, range(num, 0, -1)))} = {fatorial}")
