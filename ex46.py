
def calcular_resultado_saltos():
    while True:
        nome = input("Nome do atleta (pressione Enter para encerrar): ").strip()
        if nome == "":
            break

        saltos = []
        ordem = ["Primeiro", "Segundo", "Terceiro", "Quarto", "Quinto"]

        for i in range(5):
            while True:
                try:
                    distancia = float(input(f"{ordem[i]} Salto (em metros): "))
                    saltos.append(distancia)
                    break
                except ValueError:
                    print("Entrada inválida. Digite um número decimal.")

        print(f"\nAtleta: {nome}")
        for i in range(5):
            print(f"{ordem[i]} Salto: {saltos[i]:.1f} m")

        melhor = max(saltos)
        pior = min(saltos)

        saltos_filtrados = saltos.copy()
        saltos_filtrados.remove(melhor)
        saltos_filtrados.remove(pior)

        media = sum(saltos_filtrados) / len(saltos_filtrados)

        print(f"\nMelhor salto: {melhor:.1f} m")
        print(f"Pior salto: {pior:.1f} m")
        print(f"Média dos demais saltos: {media:.1f} m")
        print(f"\nResultado final:\n{nome}: {media:.1f} m\n")

calcular_resultado_saltos()
