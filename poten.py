#!/usr/bin/env python

def funcion(c, d):
        res = c**d
        return res

c = int(input("Dame la base: "))
d = int(input("Dame el exponente: "))
print c, "elevado a la potencia", d, "es:", funcion(c, d) 
