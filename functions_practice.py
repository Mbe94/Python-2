# Ejercicio 1: Saludo Personalizado
# Crea una función llamada saludar que tome un parámetro nombre y luego imprima un saludo personalizado, como por ejemplo: "¡Hola, [nombre]!".

def saludar(nombre):
    print(f"Hola, {nombre}!")

saludar("Juan")

#----------------------------------------------------------------

# Ejercicio 2: Multiplicación
# Crea una función llamada multiplicar que tome dos parámetros a y b, y luego imprima el resultado de la multiplicación de esos dos números.

def multiplicar(a,b):
    print(a * b)

multiplicar(2,3)
#----------------------------------------------------------------

# Ejercicio 3: Calculadora Básica
# Crea una función llamada calcular que tome tres parámetros: a, b y operacion. Si la operación es "suma", la función debe devolver la suma de a y b; si es "resta", debe devolver la resta. Si no es ninguna de esas, imprime un mensaje diciendo que la operación no es válida.

def calcular(a,b, operacion):
    if operacion == "suma":
        print(a + b)
    elif operacion == "resta":
        print(a - b)
    else:
        print("La operación no es válida")

calcular(34,45,"suma")
calcular(100,50,"resta")
calcular(150,580,"multiplicación")
#----------------------------------------------------------------