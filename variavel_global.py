variavel_global = "Essa é uma varoável global"
def imprimir_variavel():
    variavel_local = "Essa é uma variável local"
    print(variavel_global)
    print(variavel_local)
imprimir_variavel()
print(variavel_global)
# print(variavel_local) #Erro variável local, não definido

n3 = 7 #variavel global
def soma(n1, n2):
    n2 = 9
    print("Função soma n1", n1)
    print("Função soma n2", n2)
    print("Função soma n2", n3)
