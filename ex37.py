
clientes= []
while True:
    codigo = int(input("Digite o código do cliente (0 para sair): "))
    if codigo == 0:
        break
    altura = float(input("Digite a altura do cliente (em metros): "))
    peso = float(input("Digite o peso do cliente (em kg): "))
    clientes.append((codigo, altura, peso))

if clientes:
    mais_alto = max(clientes, key=lambda x: x[1])
    mais_baixo = min(clientes, key=lambda x: x[1])
    mais_gordo = max(clientes, key=lambda x: x[2])
    mais_magro = min(clientes, key=lambda x: x[2])

    media_altura = sum(x[1] for x in clientes) / len(clientes)
    media_peso = sum(x[2] for x in clientes) / len(clientes)

    print(f"Cliente mais alto: Código {mais_alto[0]}, Altura: {mais_alto[1]:.2f}m")
    print(f"Cliente mais baixo: Código {mais_baixo[0]}, Altura: {mais_baixo[1]:.2f}m")
    print(f"Cliente mais gordo: Código {mais_gordo[0]}, Peso: {mais_gordo[2]:.2f}kg")
    print(f"Cliente mais magro: Código {mais_magro[0]}, Peso: {mais_magro[2]:.2f}kg")
    print(f"Média de altura dos clientes: {media_altura:.2f}m")
    print(f"Média de peso dos clientes: {media_peso:.2f}kg")
else:
    print("Nenhum cliente registrado.")
