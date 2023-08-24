import math
# ejercicio 1
num1 = int(input("ingrese un numero"))
num2 = int(input("ingrese otro numero"))
def calcular_maxcd(num1, num2):
    return math.gcd(num1, num2)

# ejercicio 2

def calcular_mincm(num1, num2):
    mincd = calcular_maxcd(num1, num2)    
    return (num1 * num2) // mincd

print ("el maximo comun divisor es", calcular_maxcd(num1, num2))
print ("el minimo comun multiplo es", calcular_mincm(num1, num2))


