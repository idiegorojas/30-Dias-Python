def analizar_texto(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        contenido = archivo.read()
    
    palabras = contenido.split()
    total_palabras = len(palabras)
    
    frecuencia_palabras = {}
    for palabra in palabras:
        if palabra in frecuencia_palabras:
            frecuencia_palabras[palabra] += 1
        else:
            frecuencia_palabras[palabra] = 1
    
    palabra_mas_frecuente = max(frecuencia_palabras, key=frecuencia_palabras.get)
    
    longitud_total_palabras = sum(len(palabra) for palabra in palabras)
    longitud_promedio_palabras = longitud_total_palabras / total_palabras
    
    resultados = {
        'total_palabras': total_palabras,
        'frecuencia_palabras': frecuencia_palabras,
        'palabra_mas_frecuente': palabra_mas_frecuente,
        'longitud_promedio_palabras': longitud_promedio_palabras
    }
    
    return resultados

# Ejemplo de uso
ruta_archivo = 'ruta/al/archivo.txt'
resultados = analizar_texto(ruta_archivo)
print(resultados)