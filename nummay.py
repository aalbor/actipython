#!/usr/bin/env python

def funcion():
        if a>b:
                return  True
        elif a<b:
                return  False
        else:
                return "Los numeros son iguales"

a = int(input("Escriba un numero: "))
b = int(input("Escriba otro numero: "))
x = funcion()

if x == True:
        print a, "Es mayor que", b
elif x == False:
        print b, "Es mayor que", a
else:
        print x 
