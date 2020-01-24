def iva():
    print "Bienvenid@ a la calculadora de IVA."
    precio = input ("Introduzca su precio original (sin IVA) aqui: ")
    print "Hay tres tipos de IVA."
    print "El general es del 16%, el reducido del 7% y el superreducido del 4%"
    print "Para el general, introduzca g"
    print "Para el reducido, introduzca r"
    print "Para el superreducido, introduzca s"
    tasa = raw_input ("Introduzca su tarifa de IVA aqui: ")
    if (tasa=='g'):
        porcentaje = 0.16
    if (tasa=='r'):
        porcentaje = 0.07
    if (tasa=='s'):
        porcentaje = 0.04
    resultado = precio * (1+porcentaje)
    print "Su resultado es: ", resultado
iva()
