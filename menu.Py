# Lista global para almacenar listas ingresadas por el usuario
listas_guardadas = []

# Función para verificar si dos palabras son anagramas
def es_anagrama(palabra1, palabra2):
    return sorted(palabra1.lower()) == sorted(palabra2.lower())

# Función para invertir una cadena
def invertir_cadena(cadena):
    return cadena[::-1]

# Función para calcular el término n de la secuencia de Fibonacci
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Función para eliminar duplicados en una lista
def eliminar_duplicados(lista):
    return list(set(lista))

# Función para verificar si una cadena es un palíndromo
def es_palindromo(cadena):
    cadena = cadena.lower().replace(" ", "")
    return cadena == cadena[::-1]

# Función para contar la frecuencia de palabras en un texto
def contar_palabras(texto):
    palabras = texto.lower().split()
    return {palabra: palabras.count(palabra) for palabra in set(palabras)}

# Función para encontrar el mayor número en una lista
def encontrar_mayor(lista):
    return max(lista)

# Función para invertir una lista
def invertir_lista(lista):
    return lista[::-1]

# Función para filtrar solo los números pares de una lista
def filtrar_pares(lista):
    return [num for num in lista if num % 2 == 0]

# Función para encontrar el segundo mayor número en una lista
def encontrar_segundo_mayor(lista):
    return sorted(set(lista), reverse=True)[1] if len(set(lista)) > 1 else None

# Función para contar el número de vocales en un texto
def contar_vocales(texto):
    return sum(1 for letra in texto.lower() if letra in "aeiou")

# Función para ordenar una lista de tuplas por el segundo elemento
def ordenar_tuplas(lista_tuplas):
    return sorted(lista_tuplas, key=lambda x: x[1])

# Función para contar caracteres únicos en una cadena
def contar_unicos(cadena):
    return len(set(cadena))

# Función para encontrar las N palabras más largas en un texto
def palabras_mas_largas(texto, n):
    return sorted(texto.split(), key=len, reverse=True)[:n]

# Función para verificar si un número es primo
def es_primo(n):
    if n < 2:
        return False
    return all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

# Función para generar los primeros N números primos
def primos_hasta(n):
    primos, i = [], 2
    while len(primos) < n:
        if es_primo(i):
            primos.append(i)
        i += 1
    return primos

# Función para agregar una nueva lista
def agregar_lista():
    nueva_lista = input("Ingrese una lista de elementos separados por espacio: ").split()
    listas_guardadas.append(nueva_lista)
    print("Lista agregada con éxito:", nueva_lista)

# Función para ver las listas guardadas
def ver_listas():
    if not listas_guardadas:
        print("No hay listas guardadas.")
    else:
        for i, lista in enumerate(listas_guardadas, 1):
            print(f"Lista {i}: {lista}")

# Función para mostrar el menú de opciones
def menu():
    opciones = ["Anagrama", "Invertir cadena", "Fibonacci", "Eliminar duplicados", "Palíndromo", "Contar palabras", "Encontrar el mayor", "Invertir lista", "Filtrar pares", "Segundo mayor", "Contar vocales", "Ordenar tuplas", "Contar caracteres únicos", "Palabras más largas", "Números primos", "Agregar una nueva lista", "Ver listas guardadas"]
    while True:
        print("\nMenú de opciones:")
        for i, opcion in enumerate(opciones, 1):
            print(f"{i}. {opcion}")
        print("0. Salir")
        
        try:
            eleccion = int(input("Seleccione una opción: "))
            if eleccion == 0:
                break
            elif 1 <= eleccion <= 17:
                ejecutar_funcion(eleccion)
            else:
                print("Opción no válida.")
        except ValueError:
            print("Ingrese un número válido.")

# Función para ejecutar la opción seleccionada
def ejecutar_funcion(opcion):
    if opcion == 1:
        print(es_anagrama(input("Palabra 1: "), input("Palabra 2: ")))
    elif opcion == 2:
        print(invertir_cadena(input("Ingrese una cadena: ")))
    elif opcion == 3:
        print(fibonacci(int(input("Ingrese n: "))))
    elif opcion == 4:
        print(eliminar_duplicados(input("Ingrese lista de números separados por espacio: ").split()))
    elif opcion == 5:
        print(es_palindromo(input("Ingrese una cadena: ")))
    elif opcion == 6:
        print(contar_palabras(input("Ingrese un texto: ")))
    elif opcion == 7:
        print(encontrar_mayor(list(map(int, input("Ingrese una lista de números separados por espacio: ").split()))))
    elif opcion == 8:
        print(invertir_lista(input("Ingrese lista separada por espacio: ").split()))
    elif opcion == 9:
        print(filtrar_pares(list(map(int, input("Ingrese lista de números separados por espacio: ").split()))))
    elif opcion == 10:
        print(encontrar_segundo_mayor(list(map(int, input("Ingrese lista de números separados por espacio: ").split()))))
    elif opcion == 11:
        print(contar_vocales(input("Ingrese una cadena: ")))
    elif opcion == 12:
        print(ordenar_tuplas(eval(input("Ingrese lista de tuplas: "))))
    elif opcion == 13:
        print(contar_unicos(input("Ingrese una cadena: ")))
    elif opcion == 14:
        print(palabras_mas_largas(input("Ingrese un texto: "), int(input("Número de palabras: "))))
    elif opcion == 15:
        print(primos_hasta(int(input("Ingrese n: "))))
    elif opcion == 16:
        agregar_lista()
    elif opcion == 17:
        ver_listas()

if __name__ == "__main__":
    menu()