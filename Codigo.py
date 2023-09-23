# Definir funciones para cada operación
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir por cero"

# Mostrar las opciones disponibles
print("Seleccione la operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

# Obtener la opción del usuario
opcion = input("Ingrese el número de la operación que desea realizar: ")

# Obtener los números de entrada del usuario
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Realizar la operación seleccionada
if opcion == '1':
    resultado = suma(num1, num2)
elif opcion == '2':
    resultado = resta(num1, num2)
elif opcion == '3':
    resultado = multiplicacion(num1, num2)
elif opcion == '4':
    resultado = division(num1, num2)
else:
    resultado = "Opción no válida"

# Mostrar el resultado
print(f"El resultado es: {resultado}")
print("Prueba para los commits")
