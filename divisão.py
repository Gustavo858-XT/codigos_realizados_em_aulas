def dividir(a, b):
    if b == 0:
        return "Erro divisão pro 0 não é permitido."
    resultado = a / b
    return resultado
# Chamadas da função
print(dividir(10, 2)) # saida 5.0
print(dividir(10, 0)) # saida: Erro: divisão pr 0 não é permitida