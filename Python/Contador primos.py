def contador():
    print 'Bienvenid@ al contador de numeros primos.'
    print 'Hasta que numero quieres que cuente? Recuerda que tiene que ser positivo.'
    n = int(input('Ponlo aqui: '))
    while n<=0:
        print 'Ha ocurrido un error. Introduzca un numero positivo.'
        n = int(input('Ponlo aqui: '))
    print 'El numero es correcto.'
    for i in range (2, n+1):
        creciente = 2
        esprimo = True
        while esprimo and creciente<i:
            if i % creciente ==0:
                esprimo = False
            else:
                creciente=creciente+1
        if esprimo == True:
            print i, ' es primo'
        else:
            print i, ' no es primo'


contador()
