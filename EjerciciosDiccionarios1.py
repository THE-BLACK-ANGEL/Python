
#Ejercicio 1: simbolos de moneda
monedas = {'euro': '€', 'dolar': '$', 'Yen': '¥'}
moneda = input("Introduce una moneda: ")
print(monedas.get(moneda, "Moneda no encontrada en el diccionario"))



#Ejercicio 2: informacion personal
persona = {}
persona['nombre'] = input("Introduce tu nombre: ")
persona['edad'] = input("Introduce tu edad: ")
persona['dirección'] = input("Introduce tu dirección: ")
persona['teléfono'] = input("Introduce tu número de teléfono: ")

print(f"{persona['nombre']} tiene {persona['edad']} años, vive en {persona['dirección']} y su número de teléfono es {persona['teléfono']}")



#Ejercicio 3: precio de las frutas
precios_frutas = {
    'platano': 1.35,
    'manzana': 0.80,
    'pera': 0.85,
    'naranja': 0.70
}

fruta = input("Introduce la fruta que desees comprar: ")
kilos = float(input("Introduce el número de kilos: "))

if fruta in precios_frutas:
    precio_total = precios_frutas[fruta] * kilos
    print(f"El precio de {kilos} kilos de {fruta} es de {precio_total:.2f}€")
else:
    print("La fruta no está en el diccionario")



#Ejercicio 4: formato de fecha
meses = {
    1: 'enero', 2: 'febrero', 3: 'marzo', 4: 'abril', 
    5: 'mayo', 6: 'junio', 7: 'julio', 8: 'agosto', 
    9: 'septiembre', 10: 'octubre', 11: 'noviembre', 12: 'diciembre'
}

fecha = input("Introduce una fecha (dd/mm/aaaa): ")
día, mes, año = fecha.split('/')

fecha_formateada = f"{día} de {meses[int(mes)]} de {año}"
print(fecha_formateada)



#Ejercicio 5: creditos del curso
creditos_curso = {'Matemáticas': 6, 'Física': 4, 'Química': 5}

total_creditos = 0
for asignatura, creditos in creditos_curso.items():
    print(f"{asignatura} tiene {creditos} créditos")
    total_creditos += creditos

print(f"Total de créditos del curso: {total_creditos}")



#Ejercicio 6: construir un diccionario de una persona
persona = {}

while not (clave:=input("Introduce un tipo de información (o 'listo' para terminar): ")).lower() == 'listo':
    valor = input(f"Introduce {clave}: ")
    persona[clave] = valor
    print("Diccionario actual:", persona)



#Ejercicio 7: carrito de la compra
carrito = {}
coste_total = 0

while not (articulo := input("Introduce nombre del artículo (o 'listo' para terminar): ")).lower() == 'listo':
    precio = float(input("Introduce precio del artículo: "))
    carrito[articulo] = precio
    coste_total += precio

print("\nLista de la compra")
for articulo, precio in carrito.items():
    print(f"{articulo} {precio}")
print(f"Total {coste_total}")



#Ejercicio 8: diccionario de traduccion de español-ingles
diccionario_traduccion = {}

#introducir traducciones del español a ingles
traducciones = input("Introduce traducciones (palabra1:traducción1, palabra2:traducción2): ")
for par in traducciones.split(", "):
    español, ingles = par.split(":")
    diccionario_traduccion[español] = ingles

#traducir una frase (se traducen solo las palabras que están en el diccionario las demas se dejan como están)
frase = input("Introduce una frase en español para traducir: ")
palabras_traducidas = []

for palabra in frase.split():
    palabras_traducidas.append(diccionario_traduccion.get(palabra, palabra))

print(" ".join(palabras_traducidas))
