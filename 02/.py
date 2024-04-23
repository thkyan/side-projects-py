
def media_dos_elementos_unicos(lista):
    elementos_unicos = []
    for elemento in lista:
     if elemento not in elementos_unicos:
        elementos_unicos.append(elemento)

    media = sum(elementos_unicos) / len(elementos_unicos)
    return media

lista_ex = [1, 2, 3, 4, 5, 6]
resultado = media_dos_elementos_unicos(lista_ex)
print(resultado)