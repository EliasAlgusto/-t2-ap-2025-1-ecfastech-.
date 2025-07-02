
def calcular_divida(valor_original):
    print(f"{'Valor da Dívida':<20} {'Valor dos Juros':<20} {'Quantidade de Parcelas':<25} {'Valor da Parcela'}")
    
    opcoes_juros = {
        1: 0,
        3: 10,
        6: 15,
        9: 20,
        12: 25
    }

    for parcelas, percentual_juros in opcoes_juros.items():
        valor_juros = valor_original * (percentual_juros / 100)
        valor_total = valor_original + valor_juros
        valor_parcela = valor_total / parcelas
        print(f"R$ {valor_total:10.2f}     R$ {valor_juros:10.2f}       {parcelas:^21}       R$ {valor_parcela:10.2f}")

valor = float(input("Digite o valor da dívida: R$ "))
calcular_divida(valor)
