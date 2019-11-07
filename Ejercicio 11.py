def cantidad():
    print "Bienvenid@ al programa para comprobar si su palabra tiene"
    print "un numero de letras u otro."
    palabra = raw_input ("Introduzca aqui su palabra: ")
    numero = input ("Introduzca aqui su numero: ")
    lista = {}
    for letra in palabra:
        if letra in lista:
            lista[letra] = lista[letra]+1
        else:
            lista[letra]=0
    print ("%s se repite %s veces." % (letra, lista))
cantidad()
