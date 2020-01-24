def programa_numeros():
    print"Bienvendi@ al programa para saber si un numero es:"
    print"par o impar y multiplo de 3 o no."
    n=input("Introduzca su numero aqui: ")
    if n%2==0:
        print"Su numero es par y "
    else:
        print"Su numero es impar y"
    if n%3==0:
        print"tambien es multiplo de 3"
    else:
        print"ademas no es multiplo de 3"
programa_numeros()
