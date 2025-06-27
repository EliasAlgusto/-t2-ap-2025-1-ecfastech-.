def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def lista_primos(limite):
    return [num for num in range(1, limite + 1) if eh_primo(num)]
n= int(input("Digite um número inteiro: "))
print("Números primos entre 1 e", n, ":", lista_primos(n))
