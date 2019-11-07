def nomina():
    print "Bienvenid@ a la calculadora de nominas semanales."
    ordinarias = input ("Introduzca su numero de horas ordinarias: ")
    siguientes = input ("Introduzca su numero de horas no ordinarias: ")
    d_ordinarias = 30
    d_siguientes = (d_ordinarias*1.5)
    t_ordinarias = ordinarias * d_ordinarias
    t_siguientes = siguientes * d_siguientes
    resultado = t_ordinarias + t_siguientes
    print "Su resultado es: ", resultado, "euros"
nomina()
