def primo():
    numero=input"Say me your number"
    primo = True
    for i in range (2, numero):
        if (numero%i==0):
            primo = False
    if (primo==True):
        print "Es primo"
    else:
        print "No es primo"
primo ()
