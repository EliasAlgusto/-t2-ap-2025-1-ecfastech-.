
def simulacao_eleicao():
    candidatos = {
        1: "José",
        2: "João",
        3: "Maria",
        4: "Ana"
    }

    votos = {
        1: 0,  # José
        2: 0,  # João
        3: 0,  # Maria
        4: 0,  # Ana
        5: 0,  # Nulo
        6: 0   # Branco
    }

    print("Códigos de votação:")
    for codigo, nome in candidatos.items():
        print(f"{codigo} - {nome}")
    print("5 - Voto Nulo")
    print("6 - Voto em Branco")
    print("0 - Encerrar votação")

    while True:
        try:
            voto = int(input("\nDigite o código do voto: "))
            if voto == 0:
                break
            elif voto in votos:
                votos[voto] += 1
            else:
                print("Código inválido. Tente novamente.")
        except ValueError:
            print("Digite apenas números inteiros.")

    total_votos = sum(votos.values())
    total_nulos = votos[5]
    total_branco = votos[6]

    print("\nResultado da Eleição:")
    for codigo in range(1, 5):
        print(f"{candidatos[codigo]}: {votos[codigo]} voto(s)")

    print(f"Votos Nulos: {total_nulos}")
    print(f"Votos em Branco: {total_branco}")

    if total_votos > 0:
        perc_nulo = (total_nulos / total_votos) * 100
        perc_branco = (total_branco / total_votos) * 100
        print(f"Percentual de votos nulos: {perc_nulo:.2f}%")
        print(f"Percentual de votos em branco: {perc_branco:.2f}%")
    else:
        print("Nenhum voto registrado.")

# Executar a função
simulacao_eleicao()
