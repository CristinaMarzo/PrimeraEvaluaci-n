def contador():
    print 'Bienvenid@ al contador de numeros pares e impares.'
    print 'Hasta que numero quieres que cuente?'
    n = input('Ponlo aqui: ')
    m = 0
    while m<n:
        m=m+1
        print(m)
        if m % 2 ==0:
            print 'Par'
        else:
            print 'Impar'

contador()
