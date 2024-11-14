#Ejercicio1
print("¡HOLA MUNDO!")
#Ejercicio2
saludo= "¡IES Murgi!"
print(saludo)
#Ejercicio3
nombre = input("Ingrese su nombre : ")
print("Hola, "+nombre)
#Ejercicio4
calculo = ((3+2)/2*5)**2
print(calculo)
#Ejercicio5
horas= int(input("¿Cuantas horas has trabajado?"))
paga= int(input("¿A cuanto se paga la hora?"))
total=str(horas*paga)
print("El total cobrado es "+total)
print("El total cobrado es",horas*paga)
#Ejercicio6
numeroI = 1
numeroF = int(input("Introduce el numero con el que quieres terminar : "))
calculo = 0 
for i in range (numeroI,numeroF+1):
    calculo = calculo+i

print("La suma de los numeros del 1 al",numeroF,"es:",calculo)
#Ejercicio7
peso = float(input("Introduzca el peso en  kg: "))
estatura = float(input("Introduzca su estatura en metros: "))
imc=round((peso/estatura**2),1)
print("El IMC en este caso es de",imc)
#Ejercicio8
numero1= int (input("Introduce el primer numero : "))
numero2= int (input("Introduce el segundo numero : "))
resultado = numero1/numero2
resto = numero1%numero2
print(" El resultado de la division entre ",numero1,"y",numero2,"es :",resultado,"y su resto es :",resto)
#Ejercicio9
cantidadInversion = float(input("Introduce la cantidad a invertir : "))
interesAnual = int(input("Introduce el interes anual : "))
CantidadFinal=cantidadInversion*(1+(interesAnual/100))
print("La  cantidad final(al final del año) es : ", CantidadFinal)
#Ejercicio10
pesoPayaso = 112 
pesoMuñeca = 75
cantidadPayasosVendidos = int(input("Cuantos payasos quieres : "))
cantidadMuñecasVendidas = int(input("Cuantos muñecos quieres : "))
peso_total = (pesoPayaso*cantidadPayasosVendidos)+(pesoMuñeca*cantidadMuñecasVendidas)
print("El pedido tiene en total un peso de : ",peso_total)
#Ejercicio11
cantidadInversion = float(input("Introduce la cantidad a invertir : "))
interesAnual = 4
for num in range (1, 3+1):
    resultado=cantidadInversion*(1+(interesAnual/100))
    print("La cantidad total al final  del año", num, "es:", round(resultado,2))
    cantidadInversion=resultado
#Ejercicio12
precioNormal=3.50
precioNoDelDia=3.50-(3.50*0.6)
barrasBendidas = int(input("Cuantas barras se han vendido que no son del dia : "))
print("Precio de la barra normal: ", precioNormal,"\nPrecio de la barra que no es del dia : ", precioNoDelDia,"\nPrecio total de las barras vendidas que no son del dia :",round((barrasBendidas*precioNoDelDia),2))