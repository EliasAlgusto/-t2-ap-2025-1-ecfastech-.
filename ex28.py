num_cds= int(input("Digite a quantidade de CDs na coleção: "))
total_investido = 0

for i in range(num_cds):
    valor = float(input(f"Digite o valor do CD {i+1}: R$ "))
    total_investido += valor

media_gasto = total_investido / num_cds
print(f"Valor total investido: R$ {total_investido:.2f}")
print(f"Valor médio gasto por CD: R$ {media_gasto:.2f}")
