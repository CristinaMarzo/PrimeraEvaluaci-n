def ajedrez():
   print "Bienvenid@ al programa para impirimir en pantalla una tabla de ajedrez."
   print "Recuerde que el dibujo resultante va a ser cuadrado."
   h = int(input("Introduzca aqui el numero de filas deseadas: "))
   for columnas in range (1, h+1):
      if (columnas%2!=0):
         for filas in range (1, h+1):
            if (filas%2!=0):
               print "*"
               filas = filas +1
            if (filas%2==0):
               print " "
               filas = filas +1
         columnas = columnas +1
      if (columnas%2==0):
         for filas in range (1, h+1):
            if (filas%2!=0):
               print " "
               filas = filas +1
            if (filas%2==0):
               print "*"
               filas = filas +1
         columnas = columnas +1
ajedrez()
