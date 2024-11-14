"""
Ejercicio 1
Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e 
imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número 
introducido.
"""

nombre = input("Cual es tu nombre de usuario : ")
numeroVeces = (int)(input("Numero de veces que quieres que se imprima el nombre : "))
for i in range(numeroVeces):
    print(nombre)  # Imprime el nombre del usuario tantas veces como el número introducido


"""
Ejercicio 2
Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre 
por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con
todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en 
mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como 
quiera.
"""

nombreCompleto= input("Introduzca su nombre  completo : ")
nombreCompletoMinusculas = nombreCompleto.lower()
nombreCompletoMayusculas = nombreCompleto.upper()
nombreCompletoMayusPrin = nombreCompleto.title()

print(nombreCompletoMinusculas)
print(nombreCompletoMayusculas)
print(nombreCompletoMayusPrin)


"""
Ejercicio 3
Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario 
lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el 
nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.
"""

nombreCompleto= input("Introduzca su nombre  completo : ")
nombreCompleto=nombreCompleto.upper()
numeroLetras=len(nombreCompleto.replace(" ", ""))
print(f"SU NOMBRE COMPLETO ES : {nombreCompleto} ,Y  TIENE {numeroLetras} LETRAS")


"""
Ejercicio 4
Los teléfonos de una empresa tienen el siguiente formato prefijo-númeroextension donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por 
ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono 
con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.
"""
prefijo = input("Dime el prefijo del pais de  tu telefono : ")
numero= input("Dime el numero de telefono : ")
sufifijo = input("Dime el sufijo de tu telefono : ")
numerocompleto = prefijo+"-"+numero+"-"+sufifijo
print(f"Tu numero de telefono es : {numerocompleto} ")
print(f"Tu numero de telefono sin prefijo y sufijo es : {numero} ")

print ("Ahora haremos que el numero de telefono lo introduzcamos entero y que de hay solo saquemoos el numero de telefono. ")
numerocompleto = input("Dime el numero de telefono completo, es decir, con prefijos y sufijos: ")
division=numerocompleto.split("-")
print(f"Tu numero de telefono sin prefijo y sufijo es : {division[1]}")

"""
Ejercicio 5
Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por 
pantalla la frase invertida.
"""
frase = input("Introduzca la frase a invertir :")
fraseInvertida = frase[::-1]
print(fraseInvertida)


"""
Ejercicio 6
Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y 
después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
"""

frase = input("Introduzca frase : ")
vocal = input("Introduzca vocal : ")
frase = frase.replace(vocal, vocal.upper())
print(frase)


"""
Ejercicio 7
Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por 
pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con 
dominio : murgi.org 
"""
correo= input("Inreoduzca su correo electrónico : ")
nombre = correo.split("@")[0]
dominio = "murgi.org"
correoNuevo = nombre + "@" + dominio
print(f"Tu nuevo correo electrónico es : {correoNuevo}")

"""
Ejercicio 8
Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales
y muestre por pantalla el número de euros y el número de céntimos del precio introducido.
"""

Precio =  input("Introduzca el precio del producto en euros con dos decimales : ")
eurosCentimos =  Precio.split(".")
print(f"El precio del producto es : {eurosCentimos[0]} euros y {eurosCentimos[1]} centimos")

"""
Ejercicio 9
Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa 
y muestra por pantalla, el día, el mes y el año. Suponemos que siempre nos meten el dia y el mes 
con dos dígitos y el año con 4 digitos.
"""
fecha = input("Introduzca el año que  naciste (DD/MM/YYYY): ")
dia = fecha.split("/")[0]
mes = fecha.split("/")[1]
año = fecha.split("/")[2]
print(f"Has nacido el {dia} de {mes} de {año}")

"""
Ejercicio 10
Escribir un programa que pregunte por consola por los productos de una cesta de la compra, 
separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.
"""
productos = input("Introduzca los productos de la cesta de la compra separados por comas ")
productos = productos.split(",")
print("La lista  de productos de la cesta de la compra son : ")
for producto in productos:
    print(producto)

"""
Ejercicio 11
Escribir un programa que pregunte el nombre de un producto, su precio y un número de unidades y 
muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 
dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos 
enteros y 2 decimales
"""
producto=input("Escribe un producto : ")
precio =(float)(input("Escribe el precio del producto : "))
unidades =(int)(input("Escribe el número de unidades del producto : "))
precio=str(round(precio,2))
precio=precio.zfill(6)
unidades=str(unidades)
unidades=unidades.zfill(6)
costeTotal = float(precio) * int(unidades)
costeTotal = str(round(costeTotal,2))
costeTotal = costeTotal.zfill(8)
print(f"Producto : {producto}, precio unitario : {precio}, unidades : {unidades}, Coste total : {costeTotal}")





