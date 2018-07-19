# procedimiento (no retorna valores)
def saludar():
    print('Hola muchachos!')

# procedimiento con parámetros (no retorna valores)
def saludar2(nombre):
    print('Hola ' + nombre)

# funcion que retorna un valor
def obtenerPalabra():
    return 'cadena'

# funcion que suma dos numeros
# luego retorna el resultado
def sumador(n1, n2):
    suma = int(n1) + int(n2)
    return suma

# funcion que suma dos numeros y retorna directamente el resultado
def sumador2(n1, n2):
    return int(n1) + int(n2)


# llamada de una funcion:
saludar()
saludar2('Gian')
obtenerPalabra()
# guardando los valores retornados por las funciones
resultado1 = sumador(132,24)
resultado2 = sumador2(44,55)
# puedo imprimir varias variable en el print!
print(resultado1, resultado2)