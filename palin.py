#!/usr/bin/env python

def palindro():
        if a == b:
                return True
        else:
                return False

a = raw_input("Dame una cadena: ")
b = a[::-1]

if palindro() == True:
        print "Esta palabra es palindrome pues alreves se escribe asi: ",b," y se puede leer de ambas maneras"
else:
        print "Esta palabra no es palindrome pues alreves se escribe asi:",b
