
while True:
    numero= input("Qual tabuada você quer (de 1 a 10)? ")
    if numero.isdigit() and 1 <= int(numero) <= 10:
        numero= int(numero)
        break
    print("Digite um número válido, entre 1 e 10.")

print(f"\nTabuada de {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")