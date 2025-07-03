
def limpar_espacos(texto):
    texto_corrigido = ' '.join(texto.split())
    print(f" Texto corrigido: \"{texto_corrigido}\"")

# Executar com o exemplo
texto_com_espacos = "   Olá   mundo   Python   "
limpar_espacos(texto_com_espacos)
