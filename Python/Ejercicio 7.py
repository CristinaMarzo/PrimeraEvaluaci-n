def operaciones():
    print "Bienvenid@ al programa calculadora de operaciones."
    print "Puede sumar, restar, multiplicar o dividir."
    print "Recuerde que para sumas tendra que introducir 'S',"
    print "'R' para restas, 'M' para multiplicaciones y 'D' para divisiones."
    operacion = raw_input("Introduzca aqui la operacion deseada: ")
    n_1 = input ("Introduzca su primer numero aqui: ")
    n_2 = input ("Introduzca su segundo numero aqui: ")
    if (operacion == 'S'):
        resultado = n_1 + n_2
    if (operacion == 'R'):
        resultado = n_1 - n_2
    if (operacion == 'M'):
        resultado = n_1 * n_2
    if (operacion == 'D'):
        while (n_2==0):
            print "Ha ocurrido un error. Su segundo numero es 0."
            n_2=input("Introduzca aqui un numero distinto de 0: ")
        resultado = n_1 / n_2
        print "Su resultado es: ", resultado
operaciones()
