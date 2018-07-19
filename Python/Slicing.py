# el slicing nos permite seccionar las listas dado un inicio, un fin y un nro de saltos:
# miLista[inicio:fin:saltos] # esto retorna una nueva lista

# dada la lista
# se puede ver que pueden tener otras listas adentro
lista = ['Pepito', 3 , 'Jose' , True, 'juancito', [1,2,3,4] ]
# quiero guardar en otra lista solo los elementos que sean string/palabras:
listaStr = lista[0:5:2]
print(listaStr)