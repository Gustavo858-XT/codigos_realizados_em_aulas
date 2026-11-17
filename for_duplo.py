def percorrer_matriz(matriz):
 for linha in matriz:
     for elemento in linha:
        print(elemento, end= " ")
     print()
# Matriz

matriz = (
    [30, 90, 46],
    [25, 32, 14],
    [35, 10, 55]
)
#Chamada função
percorrer_matriz(matriz)
