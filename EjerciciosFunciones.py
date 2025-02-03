#Ejercicio 1: funcion que muestra saludo
def saludo():
    print("¡hola amiga!")

#Ejercicio 2: funcion que saluda a una persona por su nombre
def saludo_nombre(nombre):
    print(f"¡hola {nombre}!")

#Ejercicio 3: funcion que calcula el factorial de un numero
#solucion usando recursividad
def factorial(numero):
    if numero == 0:
        return 1
    return numero * factorial(numero - 1)
#solucion sin recursividad
def factorial_sin_recursividad(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    
    return resultado

#Ejercicio 4: funcion que calcula el total de una factura con iva
def calcular_factura(base, iva=21):
    return base + (base * iva / 100)

#Ejercicio 5: funciones que calculan area de circulo y volumen de cilindro
def area_circulo(radio):
    import math
    return math.pi * radio ** 2

def volumen_cilindro(radio, altura):
    return area_circulo(radio) * altura

#Ejercicio 6: funcion que calcula la media de una lista de numeros
def calcular_media(numeros):
    return sum(numeros) / len(numeros)

#Ejercicio 7: funcion que devuelve una lista con los numeros cuadrados de una lista de numeros
def calcular_cuadrados(numeros):
    return [num ** 2 for num in numeros]

#Ejercicio 8: funcion que calcula estadisticas basicas de una lista
def calcular_estadisticas(numeros):
    import math
    media = calcular_media(numeros)
    varianza = sum((x - media) ** 2 for x in numeros) / len(numeros)
    desviacion = math.sqrt(varianza)
    return {
        "media": media,
        "varianza": varianza,
        "desviacion": desviacion
    }

#Ejercicio 9: funcion que determina si un numero es primo
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

#Ejercicio 10: funcion que convierte numero decimal a binario
def decimal_a_binario(numero):
    if numero == 0:
        return "0"
    binario = ""
    while numero > 0:
        binario = str(numero % 2) + binario
        numero //= 2
    return binario


