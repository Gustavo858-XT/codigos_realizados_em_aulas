def calcular_desconto(valor, desconto = 5):
    if valor < 0 or desconto < 0 or desconto > 100:
        return None
    else:
        valor_final = valor - (valor * desconto/100)
        return valor_final
# Entrada de dados
valor_produto = float(input("Informe o valor do produto R$: "))
desconto = input("Informe o desconto (%) [Enter = 5%]: ")
# Validação
if desconto == "":
    resultado = calcular_desconto(valor_produto)
else:
    resultado = calcular_desconto(valor_produto, float(desconto))
print(resultado)