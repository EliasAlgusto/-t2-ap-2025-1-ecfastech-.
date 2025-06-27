
cidades = []
for _ in range(5):
    codigo = int(input("Digite o código da cidade: "))
    veiculos = int(input("Digite o número de veículos de passeio (1999): "))
    acidentes = int(input("Digite o número de acidentes com vítimas (1999): "))
    cidades.append((codigo, veiculos, acidentes))

maior_indice = max(cidades, key=lambda x: x[2])
menor_indice = min(cidades, key=lambda x: x[2])

media_veiculos = sum(c[1] for c in cidades) / len(cidades)

cidades_menos_2000 = [c[2] for c in cidades if c[1] < 2000]
media_acidentes = sum(cidades_menos_2000) / len(cidades_menos_2000) if cidades_menos_2000 else 0

print(f"Maior índice de acidentes: Cidade {maior_indice[0]}, {maior_indice[2]} acidentes")
print(f"Menor índice de acidentes: Cidade {menor_indice[0]}, {menor_indice[2]} acidentes")
print(f"Média de veículos nas cinco cidades: {media_veiculos:.2f}")
print(f"Média de acidentes nas cidades com menos de 2.000 veículos: {media_acidentes:.2f}")


