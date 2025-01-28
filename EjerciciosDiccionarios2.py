#Ejercicio 1: diccionario de cuadrados
numero = int(input("Introduce un número: "))
cuadrados = {n: n**2 for n in range(1, numero + 1)}
print(cuadrados)



#Ejercicio 2: conteo de caracteres
cadena = input("Introduce una cadena: ")
frecuencia = {}
for caracter in cadena:
    frecuencia[caracter] = frecuencia.get(caracter, 0) + 1
print(frecuencia)



#Ejercicio 3: notas de alumnos (lo he hecho con fin porque me ha parecido más fácil)
numero_alumnos = int(input("Número de alumnos: "))
notas_alumnos = {}

for i in range(numero_alumnos):
    nombre = input("Nombre del alumno: ")
    
    if nombre in notas_alumnos:
        print(f"Error: El alumno {nombre} ya existe")
        raise ValueError(f"Alumno {nombre} esta duplicado")
    
    notas = []
    
    while not (nota := input("Introduce una nota (o 'fin' para terminar): ")).lower() == 'fin':
        notas.append(float(nota))
    
    notas_alumnos[nombre] = notas

print("\nNotas de alumnos:")
for nombre, notas in notas_alumnos.items():
    if notas:
        promedio = sum(notas) / len(notas)
    else:
        promedio = 0
    print(f"{nombre}: {notas}, Promedio: {promedio:.2f}")

# Ejercicio 4: Agenda telefónica
agenda = {}

while True:
    print("\nMenú de Agenda:")
    print("1. Añadir/modificar")
    print("2. Buscar")
    print("3. Borrar")
    print("4. Listar")
    print("5. Salir")
    
    opcion = input("Elige una opción: ")
    
    if opcion == '1':
        n = input("Nombre del contacto: ")
        if n in agenda:
            print(f"Teléfono actual: {agenda[n]}")
            modificar = input("¿Modificar? (s/n): ")
            if modificar.lower() == 's':
                agenda[n] = input("Nuevo teléfono: ")
        else:
            agenda[n] = input("Teléfono: ")
    
    elif opcion == '2':
        busqueda = input("Introduce texto a buscar: ")
        resultados = {k: v for k, v in agenda.items() if k.startswith(busqueda) or k.lower().strartswith(busqueda)}
        print(resultados)
    
    elif opcion == '3':
        n = input("Nombre a borrar: ")
        if n in agenda:
            confirmacion = input(f"¿Borrar {nombre}? (s/n): ")
            if confirmacion.lower() == 's':
                del agenda[n]
        else:
            print("Contacto no encontrado")
    
    elif opcion == '4':
        print(agenda)
    
    elif opcion == '5':
        break

    else:
        print("\nOpción no válida. Por favor, elige una opción del menu.")
