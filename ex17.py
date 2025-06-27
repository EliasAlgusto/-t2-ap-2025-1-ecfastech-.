
num = int(input("Digite um número inteiro para calcular o fatorial: "))
from math import prod

fatorial = prod(range(1, num + 1))
sequencia = " . ".join(map(str, range(num, 0, -1)))

print(f"{num}! = {sequencia} = {fatorial}")