
def substituir_caractere(mensagem, caractere_antigo, caractere_novo):
    nova_mensagem=mensagem.replace(caractere_antigo, caractere_novo)
    print(f" Nova mensagem: \"{nova_mensagem}\"")

# Teste com os dados do exercício
mensagem= "Hello World!"
caractere_antigo = "o"
caractere_novo= "@"
substituir_caractere(mensagem, caractere_antigo, caractere_novo)
