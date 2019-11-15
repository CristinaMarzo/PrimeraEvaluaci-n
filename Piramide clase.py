def piramide_clase():
    filas = input ("Dime el numero de filas: ")
    espacios = ' '
    asteriscos = '*'
    for i in range (filas):
        for nespacios in range (1, filas-i):
            espacios = espacios + ' '
        for nasteriscos in range (1, 2*i+1):
            asteriscos = asteriscos + '*'
        print espacios + asteriscos
        espacios = ' '
        asteriscos = '*'
piramide_clase()
