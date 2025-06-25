
while True:
    a = int(input("População do país A: "))
    b = int(input("População do país B: "))
    taxa_a = float(input("Taxa de crescimento de A (%): "))
    taxa_b = float(input("Taxa de crescimento de B (%): "))

    if a <= 0 or b <= 0 or taxa_a <= 0 or taxa_b <= 0:
        print("Todos os valores devem ser positivos.")
        continue

    anos = 0
    while a <= b:
        a += a * (taxa_a / 100)
        b += b * (taxa_b / 100)
        anos += 1

    print(f"Serão necessários {anos} anos para que A ultrapasse ou iguale B.")

    repetir = input("Deseja repetir? (s/n): ").lower()
    if repetir != 's':
        break
