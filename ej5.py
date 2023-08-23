# 5. Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una
# cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero
# del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el
# ejercicio tanto de manera iterativa como recursiva

def get_int_iterativa():
    while True:
        try:
            num1 = int(input ("ingrese un valor entero: "))
            return (num1)    
        except ValueError:
            print ("Eso no es un entero. Vuelva a intentar")
        
def get_int_recursiva():
    try:
        num1 = int(input ("ingrese un valor entero: "))
        return num1    
    except ValueError:
        print ("Eso no es un entero. Vuelva a intentarlo.")
        return get_int_recursiva()

numero_entero = get_int_iterativa()
print ("iterativa", numero_entero)

numero_entero= get_int_recursiva()
print ("recursiva", numero_entero)