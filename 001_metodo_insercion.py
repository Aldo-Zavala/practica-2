def insertion_sort(lista):
    # Recorremos desde el segundo elemento hasta el final
    for i in range(1, len(lista)):
        actual = lista[i]  # Elemento que vamos a insertar
        j = i - 1
        
        # Desplazamos los elementos mayores hacia la derecha
        while j >= 0 and lista[j] > actual:
            lista[j + 1] = lista[j]
            j -= 1
        
        # Insertamos el elemento en su posición correcta
        lista[j + 1] = actual
    
    return lista


# Ejemplo de uso
numeros = [8, 3, 5, 1, 9, 2]
print("Lista original:", numeros)
ordenada = insertion_sort(numeros)
print("Lista ordenada:", ordenada)