def contar_caracteres(texto):
    return len(texto)
palavra = input("Digite uma palavra: ")
resultado = contar_caracteres(palavra)
print(f"A palavra {palavra} possui {resultado} caracteres")