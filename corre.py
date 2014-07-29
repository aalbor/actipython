import re

def correo():
        f = open('correos.txt','r')
        str = f.readlines()
        for l in str:
                if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,4}$',str.lower()):
                        return "Correo correcto"
                else:
                        return "Correo incorrecto"
        f.close()
        return str

print correo() 
