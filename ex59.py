
def contar_vogais_consoantes():
    texto=input("Digite uma frase ou palavra: ").lower()
    vogais= 'aeiou'
    consoantes = 'bcdfghjklmnpqrstvwxyz'

    total_vogais = 0
    total_consoantes = 0

    for char in texto:
        if char in vogais:
            total_vogais += 1
        elif char in consoantes:
            total_consoantes += 1

    print(f"\n Total de vogais: {total_vogais}")
    print(f" Total de consoantes: {total_consoantes}")
