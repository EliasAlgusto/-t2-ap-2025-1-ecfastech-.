
temperaturas= []
while True:
    temp=input("Digite uma temperatura (ou 'sair' para finalizar): ")
    if temp.lower()== "sair":
        break
    temperaturas.append(float(temp))
menor_temp= min(temperaturas)
maior_temp= max(temperaturas)
media_temp= sum(temperaturas) / len(temperaturas)


print(f"Menor temperatura: {menor_temp}°C")
print(f"Maior temperatura: {maior_temp}°C")
print(f"Média das temperaturas: {media_temp:.2f}°C")
