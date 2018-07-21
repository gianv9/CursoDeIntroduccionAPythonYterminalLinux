# el slicing nos permite seccionar las listas dado un inicio, un fin y un nro de saltos:
# miLista[inicio:fin:saltos] # esto retorna una nueva lista

# dada la lista
# se puede ver que pueden tener otras listas adentro
lista = ['Pepito', 3 , 'Jose' , True, 'juancito', [1,2,3,4] ]
print("Dada la lista: " + str(lista))
print("quiero guardar en otra lista solo los elementos que sean string/palabras:")
listaStr = lista[0:5:2]
print(listaStr)

lista = [1, True, 'Hola', 'como', 'estas' , 12, 40, False]
print("Dada la lista: " + str(lista))
print("Creamos nueva lista con 'Hola', 'Como', 'Estas'")
nuevaLista = lista[2:4:]
print(nuevaLista)


lista2 = [12, 65, True, "Hola", 30, False, 'False', 23, True]
print ("imprimir todos los booleanos de lista :" + str(lista2))
nuevaLista = lista2[2:len(lista2):3]
print(nuevaLista)

# luego recorrer la palabra 'Keloke' con un for, letra por letra...
# un for recorre conjuntos de elementos como listas y strings...
print("Recorrer el string 'keloke' como una lista:")
for letra in 'Keloke' :
    print(letra)

# esto es un string --> 'hola'
# esto es una variable --> hola

lista3 = [23,676,23,9,87,12,25,67,0,40]
# la funcion .sort() me ayuda a ordenar una lista
# ordene lista3 y muestre los numeros pares
# lista.sort()
# nota: el mod es %
print("De la lista: " + str(lista3))
print("los pares son:")
for elemento in lista3:
    if elemento % 2 == 0:
        print(elemento)