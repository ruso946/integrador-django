class Persona:
    def __init__(self, nombre='', edad=0, dni=''):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_edad(self):
        return self.edad

    def set_edad(self, edad):
        if edad >= 0:
            self.edad = edad
        else:
            print("La edad no puede ser un valor negativo.")

    def get_dni(self):
        return self.dni

    def set_dni(self, dni):
        if len(dni) == 9:
            self.dni = dni
        else:
            print("El DNI debe tener 9 caracteres.")

    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"DNI: {self.dni}")

    def es_mayor_de_edad(self):
        return self.edad >= 18
    
class Cuenta(Persona):
    def __init__(self, titular=None, cantidad=0.0):
        super().__init__(titular.get_nombre(), titular.get_edad(), titular.get_dni())
        self.__cantidad = cantidad

    def get_cantidad(self):
        return self.__cantidad

    def mostrar(self):
        print(f"Titular: {self.get_nombre()}")
        print(f"Edad: {self.get_edad()}")
        print(f"DNI: {self.get_dni()}")
        print(f"Cantidad: {self.__cantidad}")

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad
        else:
            print("La cantidad a ingresar debe ser mayor que cero.")

    def retirar(self, cantidad):
        if cantidad > 0:
            self.__cantidad -= cantidad
        else:
            print("La cantidad a retirar debe ser mayor que cero.")

class CuentaJoven(Cuenta):
    def __init__(self, titular=None, cantidad=0.0, bonificacion=0.0):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion

    def get_bonificacion(self):
        return self.__bonificacion

    def set_bonificacion(self, bonificacion):
        if bonificacion >= 0:
            self.__bonificacion = bonificacion
        else:
            print("La bonificación no puede ser un valor negativo.")

    def es_titular_valido(self):
        edad_titular = self.get_titular().get_edad()
        return edad_titular >= 18 and edad_titular < 25

    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
        else:
            print("No se puede retirar dinero de una cuenta con titular no válido.")

    def mostrar(self):
        print("Cuenta Joven")
        super().mostrar()
        print(f"Bonificación: {self.__bonificacion}%")

titular_joven = Persona("Ana García", 22, "987654321")
cuenta_joven = CuentaJoven(titular_joven, 1000.0, 5.0)
cuenta_joven.mostrar()
cuenta_joven.ingresar(88)
cuenta_joven.mostrar()
titular_joven.nombre="Pedro"
titular_joven.mostrar
cuenta_joven.nombre="Pepe"
cuenta_joven.mostrar()
