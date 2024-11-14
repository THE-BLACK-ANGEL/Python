#Ejercicio 1
#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

palabra=input("Introduzca la palabra que quiera mostrar 10 veces : ")
for x in range(10) :
    print(palabra)



#Ejercicio 2
#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha
#cumplido (desde 1 hasta su edad).
edad = input("Introduzca su edad : ")
edad = int(edad)
for x in range(1,edad+1) :
    print(x)


#Ejercicio 3
#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los
#números impares desde 1 hasta ese número separados por comas.
n = 0
while n <= 0 :
    n = int(input("Introduzca un número entero positivo : "))

for x in range(1,n+1,2) :
    if (x < n and x < n-1):
        print(x,end=",") #end=", " para que no salte de línea al final
    else :
        print(x) #imprime el último número sin comas en caso de que el ultimo numero sea impar


#Ejercicio 4
#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta
#atrás desde ese número hasta cero separados por comas.
n = 0 
while n <= 0 :
    n = int(input("Introduzca un número entero positivo : "))
    
for x in range(n,0-1,-1) :
    if (x>=1) :
        print(x,end=",")
    else :
        print(x) #imprime el último número sin comas en caso de que el ultimo numero


#Ejercicio 5
#Calculadora Financiera.
#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de
#años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
cantidadInversion = float(input("Introduce la cantidad a invertir : "))
interesAnual = float(input("Introduzca el interes anual : "))
años = int(input("Introduzca el número de años : "))
for num in range (1, años+1):
    resultado=cantidadInversion*(1+(interesAnual/100))
    print("La cantidad total al final  del año", num, "es:", round(resultado,2))
    cantidadInversion=resultado



#Ejercicio 6
#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo
#rectángulo como el de más abajo, de altura el número introducido.

numero = 0
while numero <= 0 :
    numero = int(input("Introduzca un número entero positivo : "))
    for i in range(1,numero+1):
        for j in range(1,i+1):
            print("*",end="")
            
        print()#imprime el salto de línea para cada fila del triángulo



#Ejercicio 7
#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

for i in range(1,11):
    for j in range(1,11) :
        print(i,"*",j,"=",i*j)
    print()


#Ejercicio 8
#Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las
#letras de la palabra introducida empezando por la última.
palabra = input("Introduzca una palabra : ")
for i in range(len(palabra)-1,-1,-1): #empieza desde el ultimo caracter y va hacia atrás hasta la posicion 0 (primera posicion)
    print(palabra[i],end=" ")
print()



#Ejercicio 9
#Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
#pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
#El programa debe mostrar el numero de intentos que ha necesitado el usuario, hasta acertar la
#contraseña.

contraseña = input("introduzca la contraseña a intentar descifrar : ")
palabra = ""
intentos = 0
while palabra != contraseña :
    palabra = input("introduzca la contraseña : ")
    intentos += 1

print("Contraseña acertada era y ha necesitado",intentos,"intentos para descubrirla")



#Ejercicio 10
#Escribir un programa que pida al usuario un número entero, y el programa muestre si el número es
#Primo ó no. Un número es primo cuando solo se puede dividir entre 1 y él mismo.

num = 0
while num <= 1 :
    num = int(input("introduzca un número entero : "))

primo = True
for i in range(2,num):
    if (num % i) == 0:
        primo=False
if(primo==True):
    print("el numero",num,"es primo")
else :
    print("el numero",num,"no es primo")


#Ejercicio 11
#Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por
#pantalla el número de veces que aparece la letra en la frase.

frase = input("Introduzca una frase :")
letra = input("Introduzca una letra :")
frase = frase.lower()
numVeces=0
for i in range(len(frase)):
    if(frase[i] == letra):
        numVeces=numVeces+1
print("la letra",letra,"aparece",numVeces,"veces en la frase")


#Ejercicio 12
#Escriba un programa que simule una hucha. El programa solicitará primero una cantidad, que será
#la cantidad de dinero que queremos ahorrar. A continuación, el programa solicitará una y otra vez
#las cantidades que se irán ahorrando, hasta que el total ahorrado iguale o supere al objetivo. El
#programa no comprobará que las cantidades sean positivas.

print("--->Bienvenido a la hucha<---")
objetivo = int(input("introduzca la cantidad que quiere ahorrar :"))
total = 0
while total < objetivo :
    cantidad = int(input("introduzca la cantidad que quiere ahorrar :"))
    total = total + cantidad

print("ha alcanzado su objetivo")



#Ejercicio 13.
#Escriba un programa que mejore la simulación de la hucha del ejercicio anterior, no permitiendo
#que se escriban cantidades negativas.
print("--->Bienvenido a la hucha<---")
objetivo = 0
while objetivo <=0 :
    objetivo = int(input("introduzca la cantidad que quiere ahorrar :"))

total = 0

while total < objetivo :
    cantidad = 0 
    while cantidad <= 0 :
        cantidad = int(input("introduzca la cantidad que quiere hechar a la hucha :"))
    
    total = total + cantidad

print("ha alcanzado su objetivo consiguiendo ahorrar la cantidad de",total,"euros")


