def operaciones():
    print "Bienvenid@ al programa calculadora de operaciones."
    print "Puede sumar, restar, multiplicar o dividir."
    print "Recuerde que para sumas tendra que introducir 's',"
    print "'r' para restas, 'm' para multiplicaciones y 'd' para divisiones."
    operacion = raw_input("Introduzca aqui la operacion deseada: ")
    n_1 = input ("Introduzca su primer numero aqui: ")
    n_2 = input ("Introduzca su segundo numero aqui: ")
    if (operacion == "s"):
        resultado = n_1 + n_2
    if (operacion == "r"):
        resultado = n_1 - n_2
    if (operacion == "m"):
        resultado = n_1 * n_2
    if (operacion == "d"):
        resultado = n_1 / n_2
    print "Su resultado es: ", resultado
operaciones()
