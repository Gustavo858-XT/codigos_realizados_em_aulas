def calcular_consumo(distancia, litros):
    if litros <= 0:
        return None
    return distancia/ litros
distancia = float(input("Distãncia percorrida(km):"))
litros = float(input("Combustivel consumido(litros):"))

consumo = calcular_consumo(distancia, litros)

if consumo is None:
    print("Erro: a quantidade de litros deve ser maior que zero.")
else:
    print(f"Consumo médio:{consumo:.2f}km/L")