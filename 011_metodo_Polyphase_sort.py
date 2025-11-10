# Simulación de Polyphase Sort (mezcla polifásica)

import heapq

def polyphase_merge_sort(lista, num_archivos=3):
    # Paso 1: Dividir la lista en sublistas (runs) ordenadas
    runs = []
    tam_run = max(1, len(lista) // (num_archivos * 2))
    
    for i in range(0, len(lista), tam_run):
        sublista = sorted(lista[i:i + tam_run])
        runs.append(sublista)
    
    # Distribuir los runs entre los archivos simulados
    archivos = [[] for _ in range(num_archivos)]
    for i, run in enumerate(runs):
        archivos[i % num_archivos].append(run)
    
    print("Distribución inicial de sublistas (archivos):")
    for i, arch in enumerate(archivos):
        print(f"Archivo {i+1}: {arch}")
    
    # Paso 2: Mezcla polifásica simulada
    while sum(len(arch) for arch in archivos) > 1:
        # Seleccionamos los primeros archivos con datos
        activos = [i for i, arch in enumerate(archivos) if arch]
        if len(activos) < 2:
            break
        
        # Tomamos las primeras sublistas de los dos primeros archivos activos
        i1, i2 = activos[:2]
        run1 = archivos[i1].pop(0)
        run2 = archivos[i2].pop(0)
        
        # Mezclamos las dos sublistas
        mezcla = list(heapq.merge(run1, run2))
        
        # Guardamos la mezcla en el siguiente archivo disponible
        destino = [i for i in range(num_archivos) if i not in (i1, i2)]
        if destino:
            archivos[destino[0]].append(mezcla)
        else:
            archivos[i1].append(mezcla)
        
        print("\n--- Nueva fase de mezcla ---")
        for i, arch in enumerate(archivos):
            print(f"Archivo {i+1}: {arch}")
    
    # La lista final ordenada estará en el primer archivo no vacío
    for arch in archivos:
        if arch:
            return arch[0]


# Ejemplo de uso
numeros = [15, 3, 8, 12, 5, 1, 9, 7, 2, 10, 6, 4, 11, 13, 14]
print("Lista original:", numeros)
ordenada = polyphase_merge_sort(numeros, num_archivos=3)
print("\nLista ordenada:", ordenada)
