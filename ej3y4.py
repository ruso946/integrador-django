##################################################
#### ejercicio 3 #################################
##################################################

def contar_palabras(cadena):
    # Dividir la cadena en palabras
    palabras = cadena.split()
    
    # Inicializar un diccionario para almacenar la frecuencia de cada palabra
    frecuencia = {}
    
    # Contar la frecuencia de cada palabra
    for palabra in palabras:
        # Limpiar la palabra de signos de puntuación y convertirla a minúsculas
        palabra = palabra.strip('.,!?()[]{}"\'').lower()
        
        # Si la palabra no está en el diccionario, agregarla con una frecuencia de 1
        if palabra not in frecuencia:
            frecuencia[palabra] = 1
        # Si la palabra ya está en el diccionario, incrementar su frecuencia en 1
        else:
            frecuencia[palabra] += 1
    
    return frecuencia

# Solicitar una cadena de entrada al usuario
cadena = input("Ingrese una cadena de caracteres: ")

# Obtener el diccionario de frecuencia de palabras
resultado = contar_palabras(cadena)

# Imprimir el diccionario de frecuencia
print("Frecuencia de palabras:")
for palabra, frec in resultado.items():
    print(f"{palabra}: {frec}")

#######################################
## ejercicio 4 ########################
#######################################

def palabra_mas_repetida(frecuencia_dict):
    # Inicializar variables para la palabra y su frecuencia máxima
    palabra_max = None
    frecuencia_max = 0
    
    # Iterar a través del diccionario de frecuencia
    for palabra, frecuencia in frecuencia_dict.items():
        if frecuencia > frecuencia_max:
            palabra_max = palabra
            frecuencia_max = frecuencia
    
    # Devolver una tupla con la palabra más repetida y su frecuencia
    return (palabra_max, frecuencia_max)

print(palabra_mas_repetida(contar_palabras(cadena)))


