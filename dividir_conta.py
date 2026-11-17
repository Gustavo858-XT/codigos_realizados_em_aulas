def dividir_conta(valor_total, pessoas):
    if pessoas <= 0:
        return None
    return valor_total / pessoas
valor_total = float(input("\033[35mValor total da conta(R$)\033[0m"))
pessoas = int(input("\033[36mQuantidade de pessoas:\033[36m"))

valor_individual = dividir_conta(valor_total, pessoas)
if valor_individual is None:
    print("\033[31mErro: a quantidade de pessoas deve ser maior que zero.\033[0m")
else:
    print(f"\033[32mCada pessoa deve pagar: R${valor_individual:.2f}\033[0m")

