#!/usr/bin/env python

def fibo():
        a, b = 0, 1
        while 1:
                yield a
                a, b = b, a + b

a = fibo()
a.next()
z = int(input("Dame un numero:"))
print "imprimiendo los primeros",z,"de la serie de fibonacci"
for i in range(z):
        print a.next(),

while True:
        n = raw_input("\nQuieres volver a analizar otro numero? Escribe 'SI'. Si deseas terminar escribe 'FIN' ")
        if n.strip() == 'SI':
                a = fibo()
                a.next()
                z = int(input("Dame un numero: "))
                print "imprimiendo los primeros",z,"de la serie de fibonacci"
                for i in range(z):
                        print a.next(),
        elif n.strip() == 'FIN':
                print "Gracias por usar el programa"
                break
