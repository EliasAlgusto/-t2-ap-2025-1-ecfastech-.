
def eh_palindromo(texto):
    texto_normalizado = texto.lower().replace(" ", "")
    return texto_normalizado == texto_normalizado[::-1]

print(eh_palindromo("arara"))        # True
print(eh_palindromo("Ame a ema"))    # True
print(eh_palindromo("Python"))       # False
