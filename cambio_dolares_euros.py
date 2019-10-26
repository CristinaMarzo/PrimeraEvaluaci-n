def dolares_euros():
    print "Bienvenido al convertidor de dolares a euros."
    print "Recuerde que el importe que introduzca DEBE estar en dolares."
    d = input("Introduzca aqui el importe: ")
    while (d<=0):
        print "Ha ocurrido un error"
        print "Su importe debe ser positivo (estrictamente mayor que 0)."
        d = input ("Introduzca su nuervo importe aqui: ")
    print "Su numero es valido."
    resultado = d*0.90
    print "Su importe es igual a ", resultado, " euros."
dolares_euros()
