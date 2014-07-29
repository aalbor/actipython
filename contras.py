#!/usr/bin/env python
import re
def cont():
        pat = "^.*(?=.[^\s]{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!.@?#$%^&+=,:;]).*$"
        resul = re.findall(pat, contra)
                if (resul):
                        return "contrasena valida"
                else:
                        return "contrasena no valida"

contra = raw_input("Dame la contrasena que deseas tener: ")
while True:
        print contra
        n = raw_input("Deseas que esta sea tu contrasena, escribe 'SI'. Si deseas cambiarla, escribe 'NO' ")
        if n.strip() == 'SI':
                print contra,'*',cont(),'*'
                break
        if n.strip() == 'NO':
                contra = raw_input("Dame la contrasena que deseas tener: ") 
