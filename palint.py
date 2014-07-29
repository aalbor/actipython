#!/usr/bin/env python

def palindro(a, b):
        if a == b:
                return True
        else:
                return False

a = raw_input("Dame una palabra: ")
b = a[::-1]
if palindro(a, b) == True:
        print "Esta palabra es palindrome pues alreves se escribe asi:",b,"y se puede leer de ambas maneras"
else:
        print "Esta palabra no es palindrome pues alreves se escribe asi:",b


while True:
        n = raw_input("Quieres volver a analizar otra palabra? Escribe 'SI'. Si deseas terminar escribe 'FIN' ")
        if n.strip() == 'SI':
                a = raw_input("Dame una palabra: ")
                b = a[::-1]
                if palindro(a, b) == True:
                        print "Esta palabra es palindrome pues alreves se escribe asi:",b,"y se puede leer de ambas maneras"
                else:
                        print "Esta palabra no es palindrome pues alreves se escribe asi:",b
        elif n.strip() == 'FIN':
                print "Gracias por usar el programa"
                break 
