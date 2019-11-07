def numeros_cercanos():
    print "Binevenid@ al programa para calcular los 3 numeros anteriores y los"
    print "3 siguientes a otro."
    n = input ("Introduzca aqui su numero: ")
    print "Los anteriores son:"
    for a in range (n-3, n):
        print a
        a = a+1
    print "Los siguientes son:"
    for s in range (n+1,n+4):
        print s
        s = s+1
numeros_cercanos()
