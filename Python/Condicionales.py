# estructuras básicas condicionales

nro = 2

# condicional simple
if nro == 2:
    print('nro es 2!')

# condicional if else
if nro == 5:
    print('nro es 5!')
else:
    print('nro ' + nro + ' NO es 5!')


var = 5


# condicional if elif elif ... else
if nro == var:
    print('nro es igual a var')
elif nro < var:
    print('nro es menor que var')
elif nro > var:
    print('nro es mayor que var')
else:
    # para ejecutar este else comentar algun elif
    print('Este else nunca se ejecuta!!')