
def fatorial(n):
    resultado= 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado
while True:
    num = int(input("Digite um numero inteiro positivo menor que 16 (ou -1 para sair): "))
    if num == -1:
        break
    elif 0 < num < 16:
        print(f"Fatorial de {num} é {fatorial(num)}")
    else:
        print("Numero invalido! Digite um numero entre 1 e 15.")

