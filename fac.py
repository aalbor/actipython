#!/usr/bin/env python

def factorial(x):
    num = 1
    while x >= 1:
        num = num * x
        x = x - 1
    return num

x = int(input("Dame el numero del que deseas su factorial: "))
print "El factorial de", x ,"es:",factorial(x)
