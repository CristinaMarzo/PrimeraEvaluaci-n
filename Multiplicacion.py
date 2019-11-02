def multiplicacion():
    print "Bienvenid@ al programa para multiplicar cuatro numeros."
    print "Recuerde que tienen que ser reales y distintos de 0."
    n_1 = input("Introduzca su primer numero aqui: ")
    if (n_1==0):
        while (n_1==0):
            print "Ha ocurrido un error."
            print "Su primer numero es igual a 0."
            n_1 = input ("Por favor, introduzca un numero real distinto de 0 aqui: ")
    else:
        print "Su numero es valido."
    n_2 = input("Introduzca su segundo numero aqui: ")
    if (n_2==0):
        while (n_2==0):
            print "Ha ocurrido un error."
            print "Su segundo numero es igual a 0."
            n_2 = input ("Por favor, introduzca un numero real distinto de 0 aqui: ")
    else:
        print "Su numero es valido."
    n_3 = input ("Introduzca su tercer numero aqui: ")
    if (n_3==0):
        while (n_3==0):
            print "Ha ocurrido un error."
            print "Su tercer numero es igual a 0."
            n_3 = input ("Por favor, introduzca un numero real distinto de 0 aqui: ")
    else:
        print "Su numero es valido."
    n_4 = input ("Introduzca su cuarto numero aqui: ")
    if (n_4==0):
        while (n_4==0):
            print "Ha ocurrido un error."
            print "Su cuarto numero es igual a 0."
            n_4 = input ("Por favor, introduzca un numero real distinto de 0 aqui: ")
    else:
        print "Su numero es valido."
    resultado = n_1*n_2*n_3*n_4
    print "Su resultado es: ", resultado
multiplicacion()
