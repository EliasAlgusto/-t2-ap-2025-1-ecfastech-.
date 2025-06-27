
def divisores(n):
    return [i for i in range(1, n + 1) if n % i == 0]

num=int(input("Digite um número inteiro: "))
if eh_primo(num):
    print(f"{num} é um número primo.")
else:
    print(f"{num} não é um número primo. Ele é divisível por {divisores(num)}.")


