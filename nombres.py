#!/usr/bin/env python

import re
def usu(usuario):
        if usuario == 0 or len(usuario) < 6:
                return "El nombre de usuario debe contener al menos 6 caracteres"
        elif len(usuario) > 12:
                return "El nombre de usuario no puede contener mas de 12 caracteres"
        elif re.match('^[a-z\d_]{6,12}$',usuario.lower()):
                return "El nombre de usuario es valido"
        else:
                return "El nombre de usuario puede contener solo letras y numeros"
usuario = raw_input("Dame un nombre de usuario: ")
while True:
        print usuario
        n = raw_input("Deseas que este sea su nombre de usuario escribe 'SI'. Escribe 'NO' si deseas cambiarlo ")
        if n.strip() == 'SI':
                print usuario,'*',usu(usuario),'*'
                break
        if n.strip() == 'NO':
                usuario = raw_input("Dame un nombre de usuario: ")
