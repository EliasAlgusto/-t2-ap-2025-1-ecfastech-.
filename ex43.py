
def lanchonete():
    cardapio = {
        100: ("Cachorro Quente", 1.20),
        101: ("Bauru Simples", 1.30),
        102: ("Bauru com ovo", 1.50),
        103: ("Hambúrguer", 1.20),
        104: ("Cheeseburguer", 1.30),
        105: ("Refrigerante", 1.00)
    }

    print("Cardápio da Lanchonete:")
    for codigo, (item, preco) in cardapio.items():
        print(f"{codigo} - {item:<15} R$ {preco:.2f}")

    total_geral = 0.0

    while True:
        try:
            codigo = int(input("\nDigite o código do item (ou 0 para encerrar o pedido): "))
            if codigo == 0:
                break
            if codigo not in cardapio:
                print("Código inválido. Tente novamente.")
                continue

            quantidade = int(input(f"Digite a quantidade de '{cardapio[codigo][0]}': "))
            if quantidade <= 0:
                print("Quantidade inválida. Deve ser maior que zero.")
                continue

            nome_item, preco = cardapio[codigo]
            subtotal = preco * quantidade
            total_geral += subtotal

            print(f" {quantidade} x {nome_item} = R$ {subtotal:.2f}")
        except ValueError:
            print("Entrada inválida. Use apenas números inteiros.")

    print(f"\n Total geral do pedido: R$ {total_geral:.2f}")
    print("Obrigado por comprar conosco!")

lanchonete()
