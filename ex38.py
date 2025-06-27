
ano_contratacao= 1995
salario= float(input("Digite o salário inicial do funcionário: "))

percentual = 1.5 / 100

for ano in range(1996, 2025):
    aumento = salario * percentual
    salario += aumento
    percentual *= 2  # Dobro do percentual anterior
print(f"Salário atual em 2025: R$ {salario:.2f}")
