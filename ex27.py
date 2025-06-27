num_turmas= int(input("Digite a quantidade de turmas: "))
total_alunos= 0

for i in range(num_turmas):
    while True:
        alunos = int(input(f"Digite a quantidade de alunos na turma {i+1} (máximo 40): "))
        if 1 <= alunos <= 40:
            total_alunos += alunos
            break
        else:
            print("Número inválido! A turma deve ter entre 1 e 40 alunos.")

media_alunos = total_alunos / num_turmas
print(f"O número médio de alunos por turma é: {media_alunos:.2f}")
