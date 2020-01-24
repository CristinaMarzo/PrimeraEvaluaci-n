def piramide_clase():
    filas = input("Dime la altura de la piramide: ")
    espacios = ' '
    asteriscos = '*'
    for i in range (filas):
        #Construimos la secuencia de espacios
        for nespacios in range (1, filas-i):
            espacios = espacios + ' '
        for nasteriscos in range (1, 2*i+1):
            asteriscos = asteriscos + '*'
            #Escribo de golpe toda la fila
        print espacios + asteriscos
        #Limpio las variables acumuladoras
        espacios = ' '
        asteriscos = '*'
        #Paso a la siguiente fila
        
piramide_clase()
