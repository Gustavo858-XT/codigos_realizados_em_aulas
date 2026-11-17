def dividir (n1, n2):
    resultado = n1 / n2
    return resultado
# Armazenando o retorno de uma várialvel
divisao = dividir(80, 5)
print("O resultadfo da divisao é:", divisao)
# Chamando a função diretamente do print
print("Resultado:", dividir(20, 4))
#Utilizando o retorno em outro ciclo
resultado = dividir(3, 5)
soma = 20 + resultado
print("A soma é:", soma)
# Utilizando valores informados pelo usuário
a = int(input("Informe o dividendo"))
b = int(input("Informe o divisor"))
print("Resultado:", dividir(a, b))
