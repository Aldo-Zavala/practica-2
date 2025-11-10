# Método de ordenamiento Natural Merging (Mezcla Natural)

def merge(lista_izq, lista_der):
    resultado = []
    i = j = 0
    
    # Combinamos las dos listas ordenadas
    while i < len(lista_izq) and j < len(lista_der):
        if lista_izq[i] <= lista_der[j]:
            resultado.append(lista_izq[i])
            i += 1
        else:
            resultado.append(lista_der[j])
            j += 1
    
    # Agregamos los elementos restantes
    resultado.extend(lista_izq[i:])
    resultado.extend(lista_der[j:])
    
    return resultado


def natural_merging_sort(lista):
    if len(lista) <= 1:
        return lista

    # Repetimos hasta que solo quede una secuencia ordenada
    while True:
        sublistas = []
        i = 0

        # Identificamos las secuencias naturalmente ordenadas
        while i < len(lista):
            secuencia = [lista[i]]
            i += 1
            while i < len(lista) and lista[i] >= lista[i - 1]:
                secuencia.append(lista[i])
                i += 1
            sublistas.append(secuencia)
        
        # Si solo hay una secuencia, ya está ordenada
        if len(sublistas) == 1:
            return sublistas[0]
        
        # Mezclamos las sublistas de dos en dos
        nueva_lista = []
        for i in range(0, len(sublistas), 2):
            if i + 1 < len(sublistas):
                nueva_lista.append(merge(sublistas[i], sublistas[i + 1]))
            else:
                nueva_lista.append(sublistas[i])
        
        # Actualizamos la lista con las mezclas realizadas
        lista = [x for sublista in nueva_lista for x in sublista]


# Ejemplo de uso
numeros = [8, 3, 5, 1, 9, 2, 7, 4]
print("Lista original:", numeros)
ordenada = natural_merging_sort(numeros)
print("Lista ordenada:", ordenada)
