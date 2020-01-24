def fecha():
    print "Bienvenido al programa para transformar una fecha en formato dd, mm, aaaa,"
    print "siendo d el dia, m el mes y a el año."
    
    d = int(input ("Introduzca el dia: "))
    while (d<1) or (d>31):
        print "Ha ocurrido un error. El numero del dia debe estar entre 1 y 31."
        d = input ("Introduzca de nuevo su numero de dia aqui: ")

    m = int(input ("Introduzca el mes: "))
    while (m<1) or (m>12):
        print "Ha ocurrido un error. El numero del mes debe estar entre 1 y 12."
        m = input ("Introduzca de nuevo su numero de mes aqui: ")

    a = int(input ("Introudzca el año: "))
    
    if m==1:
        resultado = "enero"
    if m==2:
        resultado = "febrero"
    if m==3:
        resultado = "marzo"
    if m==4:
        resultado = "abril"
    if m==5:
        resultado = "mayo"
    if m==6:
        resultado = "junio"
    if m==7:
        resultado = "julio"
    if m==8:
        resultado = "agosto"
    if m==9:
        resultado = "septiembre"
    if m==10:
        resultado = "octubre"
    if m==11:
        resultado = "noviembre"
    if m==12:
        resultado = "diciembre"
    print "Su resultado es: ", d, " de " , resultado, " de " , a

fecha()
