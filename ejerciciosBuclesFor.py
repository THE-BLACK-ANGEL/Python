"""
#Ejercicio 1
#Utilizando cinco bucles tipo for y en cada uno de ellos el tipo range() con tres argumentos,
#escribe el código Python necesario para que se muestre por pantalla la siguiente
#información tabulada con las siguientes cinco series aritméticas:

for i in range(1, 11):
    if(i<10) :
        print(i,end=(" "))
    else :
        print(i)

for i in range (2,21,2) :
    if(i<20) :
        print(i,end=(" "))
    else :
        print(i)

for i in range (20,48,3) :
    if(i<48) :
        print(i,end=(" "))
    else :
        print(i)

for i in range (10,31,4) :
    if(i<30) :
        print(i,end=(" "))
    else :
        print(i)

for i in range (40,0-1,-5) :
    if(i>0) :
        print(i,end=(" "))
    else :
        print(i)



#Ejercicio 2
#Crea un programa que muestre el mismo resultado que en el ejercicio anterior, pero
#utilizando ahora bucles tipo for con tipos range() de dos argumentos.

for x in range(1,11):
    if(x<10) :
        print(x,end=(" "))
    else :
        print(x)

num1 = 2
for x in range (1,11):
    if(num1<20):
        print(num1,end=(" "))
        num1+=2
    else :
        print(num1)

num1 = 20
for x in range (1,11):
    if(num1<47):
        print(num1,end=(" "))
        num1+=3
    else :
        print(num1)

num1=10
for x in range (1,7):
    if(num1<30):
        print(num1,end=(" "))
        num1+=4
    else :
        print(num1)

num1=40
for x in range (1,10):
    if(num1>0):
        print(num1,end=(" "))
        num1-=5
    else :
        print(num1)
        




#Ejercicio 3
#Crea un programa que muestre la tabla del ejercicio número 1, utilizando bucles tipo for
#con tipos range() que tengan solamente un argumento
num1= 1
for x in range(10):
    if(num1<10):
        print(num1,end=(" "))
        num1+=1
    else : 
        print(num1)

num1 = 2
for x in range(10):
    if(num1<20):
        print(num1,end=(" "))
        num1+=2
    else :
        print(num1)

num1 = 20
for x in range(10):
    if(num1<47):
        print(num1,end=(" "))
        num1+=3
    else :
        print(num1)

num1 = 10
for x in range(6):
    if(num1<30):
        print(num1,end=(" "))
        num1+=4
    else :
        print(num1)

num1=40
for x in range (9):
    if(num1>0):
        print(num1,end=(" "))
        num1-=5
    else :
        print(num1)



#Ejercicio 4
#Escribe el código necesario para generar las siguientes siete secuencias de números
#utilizando bucles for.


for i in range(1, 11):
  print(i * i,end=(" "))
print()

for i in range(2, 11):
  print(i * i + 3,end=(" "))
print()

for i in range(3, 8):
  print(i * i * i,end=(" "))
print()

for i in range(2, 8):
  print(i * 4,end=(" "))
print()

for i in range(0, 5):
  print(10 ** i,end=(" "))
print()

for i in range(0, 5):
  print(10 ** (-i),end=(" "))
print()

num1=1
for i in range(1, 9):
    print(num1,end=(" "))
    num1=num1*-1
print()


#Ejercicio 5
#Escribe un programa que pida dos números enteros, el segundo ha de ser mayor o igual
#que el primero. A continuación, se debe mostrar por pantalla una lista con todos los
#números enteros comprendidos entre los números introducidos, indicando en cada caso
#si el número escrito es par o impar.

num1=(int)(input("Introduce un numero : "))
num2=(int)(input("Introduce otro numero mayor o igual al primero : "))
while num1>num2 :
    num2=(int)(input("Introduce un numero mayor o igual que el primero : "))

print("Los numeros entre los dos son : ")
for i in range(num1,num2+1):
    if i%2==0:
        print(f"{i} es par",end="//")
    else:
        print(f"{i} es impar",end="//")
print()

#Ejercicio 6
#Escribe un programa que pida dos números enteros, el segundo ha de ser mayor o igual que el primero. A continuación, se debe mostrar por pantalla una lista con todos
#A continuación, el programa debe mostrar como resultado la suma de todos los enteros comprendidos entre el primero y el segundo incluidos ambos. Observa
#el formato del resultado en el modelo:

num1=(int)(input("Introduce un numero : "))
num2=(int)(input("Introduce otro numero mayor o igual al primero : "))
while num1>num2 :
    num2=(int)(input("Introduce un numero mayor o igual que el primero : "))
total=0
for i in range(num1,num2+1):
    total=total+i

print(f"La suma de los numeros entre {num1} y {num2} es :")
for i in range(num1,num2+1):
    if i == num2:
        print(i ,end=" = ")
    else:    
        print(i,end=" + ")
print(total)
"""
#Ejercicio 7
#Escribe un programa que pida por pantalla un número entero y que a continuación calcule
#su factorial. En número ha de ser mayor que cero.  

num1 = 0 
while num1 <= 0:
    num1 = int(input("Introduce un numero mayor que 0 : "))

factorial = 1
for i in range(1,num1+1):
    factorial = factorial * i

print(f"El factorial de {num1} es : {factorial}")

#Ejercicio 8
#Escribe un programa que permita sumar números, la aplicación debe funcionar de la
#siguiente forma:
#a. En primer lugar, el programa preguntará por la cantidad de números que se van a introducir
#b. A continuación, el programa debe pedir cada uno de esos valores (pueden ser decimales)
#c. Por último el programa calculará la suma de todos ellos y mostrará el resultado por pantalla.



#Ejercicio 9
#Diseña un programa que detecte números negativos, la aplicación debe funcionar de la
#siguiente forma:
#a. En primer lugar, el programa preguntará por la cantidad de números que se van a introducir.
#b. A continuación, el programa ha de pedir cada uno de esos valores (pueden ser decimales)
#c. Por último el programa indicará cuántos de esos números son negativos. 


#Ejercicio 10 
#Diseña un programa que pregunte por la cantidad de números que se van a introducir. A
#continuación, la aplicación debe de mostrar como resultado el mayor, el menor y la media
#aritmética de todos ellos.


#Ejercicio 11
#Crea un programa que pida un valor entero mayor que cero y calcule todos sus divisores,
#mostrando el resultado con el formato indicado en el siguiente ejemplo (necesitarás
#utilizar una variable tipo lista).

#Ejercicio 12
#Tomando como punto de partida el programa anterior, escribe el código necesario para
#que el programa determine si el número es primo o no, el resultado podría ser:

