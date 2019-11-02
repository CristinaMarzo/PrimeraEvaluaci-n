def dia_semana():
    print "Bienvenido al programa para averiguar dia de la semana."
    print "Introduzca un numero del 1 al 7 y obtendra el dia de la semana correspondiente."
    n=input("Introduzca su numero aqui: ")
    while (n!=1 and n!=2 and n!= 3 and n!=4 and n!=5 and n!=6 and n!=7):
        print "Ha ocurrido un error. Su numero no es valido."
        n=input("Introduzca aqui un numero entero del 1 al 7: ")
    else:
        print "Su numero es valido."
    if n==1:
        print "Su dia de la semana es el lunes."
    if n==2:
        print "Su dia de la semana es el martes."
    if n==3:
        print "Su dia de la semana es el miercoles."
    if n==4:
        print "Su dia de la semana es el jueves."
    if n==5:
        print "Su dia de la semana es el viernes."
    if n==6:
        print "Su dia de la semana es el sabado."
    if n==7:
        print "Su dia de la semana es el domingo."
dia_semana()
