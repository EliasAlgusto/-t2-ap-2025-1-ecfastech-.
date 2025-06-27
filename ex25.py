
N=int(input("Quantas pessoas há na turma? "))
idades=[]

for _ in range(N):
    idade = int(input("Digite a idade: "))
    idades.append(idade)
media_idade= sum(idades) / N 
if media_idade <= 25:
    categoria = "jovem"
elif media_idade <= 60:
    categoria = "adulta"
else:
    categoria = "idosa"

print(f"Média de idade da turma: {media_idade:.2f}")
print(f"A turma é considerada {categoria}.")
