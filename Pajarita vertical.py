def pajarita_2():
    filas = input ("Dime el numero de filas: ")
    espacios = ' '
    asteriscos = '*'
    for i in range ((filas/2)):
        nrep = ((filas/2)+1)
        asteriscos = asteriscos * nrep
        for nespacios in range (1, filas-1):
            espacios = espacios + ' '
        for nasteriscos in range (1, 2*i+1):
            asteriscos = asteriscos + ' '
        print espacios + asteriscos
        nrep = nrep-1
        espacios = ' '
        asteriscos = '*'
    for i in range ((filas/2)):
        for nespacios in range (1, filas-i):
            espacios = espacios + ' '
        for nasteriscos in range (1, 2*i+1):
            asteriscos = asteriscos + '*'
        print espacios + asteriscos
        espacios = ' '
        asteriscos = '*'
pajarita_2()
