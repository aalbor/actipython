#!/usr/bin/env python
def agend():
        var = []
        var2 = ["Nombre:","Telefono:","Correo:"]
        for l in range(3):
                var.append(raw_input(var2[l]))
        return var

def expxml(listado):
        file = open("agenda.xml","w")
        file.write("<?xml version='1.0' encoding='iso-8859-1'?>\n")
        file.write("<agenda>\n")
        for i in listado:
                file.write("\t<contacto>\n")
                for j in range(0,3):
                        if j==0:
                                file.write("\t\t<nombre>%s</nombre>\n" % i[j])
                        elif j==1:
                                file.write("\t\t<telefono>%s</telefono>\n" % i[j])
                        elif j==2:
                                file.write("\t\t<correo>%s</correo>\n" % i[j])
                file.write("\t</contacto>\n")
	file.write("</agenda>")
        file.close()

def expcsv(listado):
        file = open("agenda.csv","w")
        file.write("Nombre, telefono, correo\n")
        for i in listado:
                for j in i:
                        file.write(j+",")
                file.write("\n")
        file.close()

listado=[]
listado.append(agend())
while True:
        n = raw_input("Deseas agregar mas contactos? Escribe 'SI' o 'NO' ")
        if n.strip() == 'SI':
                listado.append(agend())
        if n.strip() == 'NO':
                print "A que extension deseas exportar tu agenda"
                opc = input("Selecciona 1 para xlm o 2 para csv: ")
                if opc == 1:
                        expxml(listado)
                if opc == 2:
                        expcsv(listado)
                break
