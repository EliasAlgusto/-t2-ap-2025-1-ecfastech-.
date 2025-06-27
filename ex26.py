
eleitores= int(input("Digite o número total de eleitores: "))
votos_candidato1 = 0
votos_candidato2 = 0
votos_candidato3 = 0


for _ in range(eleitores):
    print("\nCandidatos:")
    print("1 - Candidato A")
    print("2 - Candidato B")
    print("3 - Candidato C")
    voto = int(input("Digite o número do candidato em quem deseja votar (1, 2 ou 3): "))


    if voto == 1:
        votos_candidato1 += 1
    elif voto == 2:
        votos_candidato2 += 1
    elif voto == 3:
        votos_candidato3 += 1
    else:
        print("Voto inválido! Não será contabilizado.")


print("\nResultado da eleição:")
print(f"Candidato A: {votos_candidato1} votos")
print(f"Candidato B: {votos_candidato2} votos")
print(f"Candidato C: {votos_candidato3} votos")
