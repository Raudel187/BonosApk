import requests
import sys
from bs4 import BeautifulSoup


user_code_student = sys.argv[1]

#'Z190202031'
bonos_cobrados = sys.argv[2]


sesion = requests.Session()

sesion_active = sesion.post("http://www.itszas.edu.mx/bonos/login.php",data=dict(user="Manuel",clave="080494"))


data1 = BeautifulSoup(sesion_active.text, "html.parser")
location = data1.find("script").text
translation = location.split("'")
link_bonos = "http://www.itszas.edu.mx/bonos/" + translation[1]

## Seccion Descarga
sesion_active = sesion.get(link_bonos)
data2 = BeautifulSoup(sesion_active.text, "html.parser")
user_main_name = data2.h3
print user_main_name.text, "\n"




## Carga de Informacion del Alumno

url_student_cargo = "http://www.itszas.edu.mx/bonos/carga3.php?control2="+ user_code_student+"&envio=Buscar"


bono_page_user = sesion.get(url_student_cargo)

sopa3 = BeautifulSoup(bono_page_user.text, "html.parser")

info_alumno = sopa3.find_all('h2')

if info_alumno[3].text == "":
    print "Usuario incorrecto"
    sys.exit(1)


print "Codigo: ", info_alumno[0].text
print "Nombre: ", info_alumno[1].text.encode('utf8')
print "Carrera: ", info_alumno[2].text.encode('utf8')
print "Correo: ", info_alumno[3].text

bonos_user = sopa3.find_all("h1")

bonos_actuales = bonos_user[1].text.encode('utf8')


print "\n", "Bonos Cobrados: "
print " -----------"
print "|"," "*9,"|"
print " "*4, bonos_cobrados," "*2
print "|"," "*9,"|"
print " -----------"

print "\n", "Bonos Restantes: "
print " -----------"
print "|"," "*9,"|"
print " "*4, bonos_actuales," "*2
print "|"," "*9,"|"
print " -----------"





#input_bono = sopa3.input(id='#cargabonos1')
#url_cargo_bonos = 'http://www.itszas.edu.mx/bonos/guardar2.php?cargabonos=3&cargabonos1=size%3D"5"&descargar=Descargar+Bonos'



#5
#5
