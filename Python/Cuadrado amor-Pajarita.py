def pajarita_tumbada():
    filas = 2*(input ("Dime cuantas filas quieres que tenga: "))
    espacios = ' '
    asteriscos = '*'
    columnas = (((filas/2)-1)*2)+1
    for i in range (filas):
        while (i%2!=0):
            nespacios = columnas-2
            for a in range (2, columnas):
                inter = ' '
                for e in range (2, nespacios-2):
                    espacios = espacios + ' '
                    e = e+1
                    inter = inter + ' *'
                if inter==0:
                    inter = ' '
                print asteriscos + inter + espacios + inter + asteriscos
                espacios = ' '
                asteriscos = '*'
            nespacios = nespacios-1
            i = i+1
           
pajarita_tumbada()
