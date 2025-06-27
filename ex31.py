
while True:  # Loop infinito para processar múltiplas compras
    print("\nLojas Tabajara")
    
    total = 0
    contador = 1


    while True:
        preco= float(input(f"Produto {contador}: R$ "))
        if preco == 0:
            break 
        total += preco
        contador += 1


    print(f"Total: R$ {total:.2f}")


    dinheiro= float(input("Dinheiro: R$ "))
    troco= dinheiro - total


    print(f"Troco: R$ {troco:.2f}")


    continuar= input("\nRegistrar nova compra? (s/n): ").strip().lower()
    if continuar != "s":
        break 
