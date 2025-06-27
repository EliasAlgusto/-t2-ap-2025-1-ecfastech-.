
def contar_primos(n):
    primos= []
    total_divisoes= 0


    for num in range(2, n + 1):
        eh_primo= True
        for i in range(2, int(num ** 0.5) + 1):
            total_divisoes += 1
            if num % i== 0:
                eh_primo= False
                break
        if eh_primo:
            primos.append(num)


    return primos, total_divisoes


N = int(input("Digite um número inteiro N: "))
primos, divisoes = contar_primos(N)
print(f"Números primos entre 1 e {N}: {primos}")
print(f"Total de divisões realizadas: {divisoes}")


