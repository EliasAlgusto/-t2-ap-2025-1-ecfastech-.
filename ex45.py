
def aplicar_prova():
    print(" Gabarito da Prova (digite A, B, C, D ou E para cada questão)")
    gabarito = []
    for i in range(1, 11):
        while True:
            resposta = input(f"Gabarito da questão {i:02d}: ").strip().upper()
            if resposta in ['A', 'B', 'C', 'D', 'E']:
                gabarito.append(resposta)
                break
            else:
                print("Resposta inválida. Tente novamente.")

    notas = []
    continuar = 'S'

    while continuar == 'S':
        print("\n Respostas do aluno:")
        acertos = 0
        for i in range(1, 11):
            while True:
                resposta = input(f"Questão {i:02d}: ").strip().upper()
                if resposta in ['A', 'B', 'C', 'D', 'E']:
                    if resposta == gabarito[i-1]:
                        acertos += 1
                    break
                else:
                    print("Resposta inválida. Tente novamente.")
        print(f"Total de acertos: {acertos}")
        notas.append(acertos)

        continuar = input("Outro aluno vai utilizar o sistema? (S/N): ").strip().upper()

    if notas:
        print("\n Resultado final da turma:")
        print(f"Maior acerto: {max(notas)}")
        print(f"Menor acerto: {min(notas)}")
        print(f"Total de alunos: {len(notas)}")
        media = sum(notas) / len(notas)
        print(f"Média da turma: {media:.2f}")
    else:
        print("Nenhum aluno respondeu à prova.")

aplicar_prova()
