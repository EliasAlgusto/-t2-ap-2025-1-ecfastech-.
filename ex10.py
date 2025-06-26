
soma= 0
for i in range(5):
    while True:
        try:
            soma+= float(input(f"Número {i+1}: "))
            break
        except ValueError:
            print("Inválido. Digite um número.")
print(f"Soma: {soma}\nMédia: {soma / 5:.2f}")
