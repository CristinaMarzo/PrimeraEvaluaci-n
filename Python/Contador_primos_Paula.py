def contador_primos():
    print "Este programa se encarga de contar los numeros primos."
    print "Para ello necesita conocer el numero mas alto deseado."
    n = input ("Cual sera el numero mas alto?: ")
    primo = True
    for i in range (1, n+1):
        for p in range (2, i-1):
            if (i%p==0):
                primo = False
        if (primo==False):
            print i, "No primo"
        else:
            print i, "Primo"
        primo=True
contador_primos()
