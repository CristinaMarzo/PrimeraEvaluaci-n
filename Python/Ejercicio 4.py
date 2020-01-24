def mes():
    print "Bienvenid@ al programa para obtener un mes a partir de numeros del 1 al 12."
    mes=input("Introduzca su numero aqui: ")
    while (mes<1) or (mes>12):
        print "Ha ocurrido un error. Su numero no es valido."
        mes = input("Introduzca de nuevo un numero valido aqui: ")
    if mes==1:
        print "El mes es enero."
    else:
        if mes==2:
            print "El mes es febrero."
        else:
            if mes==3:
                print "El mes es marzo."
            else:
                if mes==4:
                    print "El mes es abril."
                else:
                    if mes==5:
                        print "El mes es mayo."
                    else:
                        if mes==6:
                            print "El mes es junio."
                        else:
                            if mes==7:
                                print "El mes es julio."
                            else:
                                if mes==8:
                                    print "El mes es agosto."
                                else:
                                    if mes==9:
                                        print "El mes es septiembre."
                                    else:
                                        if mes==10:
                                            print "El mes es octubre."
                                        else:
                                            if mes==11:
                                                print "El mes es noviembre."
                                            else:
                                                if mes==12:
                                                    print "El mes es diciembre."
mes()
