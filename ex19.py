
9N=int(input("Quantos números deseja inserir? "))
numeros= []

for _ in range(N):
    num = float(input("Digite um número entre 0 e 1000: "))
    while num < 0 or num > 1000: 
        print("Número inválido! Digite um número entre 0 e 1000.")
        num = float(input("Digite um número entre 0 e 1000: "))
    numeros.append(num)


