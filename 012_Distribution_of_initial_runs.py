# Distribución de corridas iniciales (Distribution of Initial Runs)

def generar_corridas_iniciales(lista, tamaño_corrida):
    corridas = []
    for i in range(0, len(lista), tamaño_corrida):
        corrida = sorted(lista[i:i + tamaño_corrida])  # Se ordena cada bloque
        corridas.append(corrida)
    return corridas


def distribuir_corridas(corridas, num_archivos):
    archivos = [[] for _ in range(num_archivos)]
    i = 0
    for corrida in corridas:
        archivos[i % num_archivos].append(corrida)
        i += 1
    return archivos


# Ejemplo de uso:
datos = [20, 5, 8, 15, 2, 17, 12, 9, 30, 25, 1, 18]
tamaño_corrida = 4   # Cada corrida tendrá 4 elementos
num_archivos = 3     # Se distribuyen en 3 archivos simulados

print("Datos originales:", datos)

# Generamos corridas iniciales
corridas = generar_corridas_iniciales(datos, tamaño_corrida)
print("\nCorridas iniciales ordenadas:")
for i, c in enumerate(corridas, 1):
    print(f"Corrida {i}: {c}")

# Distribuimos las corridas entre archivos
archivos = distribuir_corridas(corridas, num_archivos)
print("\nDistribución en archivos:")
for i, archivo in enumerate(archivos, 1):
    print(f"Archivo {i}: {archivo}")
