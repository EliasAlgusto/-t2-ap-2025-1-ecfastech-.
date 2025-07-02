
def avaliar_ginasta():
    while True:
        nome = input("Atleta (pressione Enter para encerrar): ").strip()
        if nome == "":
            break

        notas = []
        for i in range(1, 8):
            while True:
                try:
                    nota = float(input(f"Nota {i}: "))
                    if 0 <= nota <= 10:
                        notas.append(nota)
                        break
                    else:
                        print("A nota deve estar entre 0 e 10.")
                except ValueError:
                    print("Entrada inválida. Digite um número decimal.")

        print(f"\nAtleta: {nome}")
        for nota in notas:
            print(f"Nota: {nota:.1f}")

        melhor = max(notas)
        pior = min(notas)

        notas_filtradas = notas.copy()
        notas_filtradas.remove(melhor)
        notas_filtradas.remove(pior)

        media = sum(notas_filtradas) / len(notas_filtradas)

        print("\nResultado final:")
        print(f"Atleta: {nome}")
        print(f"Melhor nota: {melhor:.1f}")
        print(f"Pior nota: {pior:.1f}")
        print(f"Média: {media:.2f}\n")

avaliar_ginasta()
