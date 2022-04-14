#introducion del programa (inicio de sesion, parametros, variables)

name = input ("Inicia sesion: ")
print ("Bienvenido " + name + " a Un Dia como Hoy en la Historia")
print("")
tema = input ("Sobre que tema te gustaria tratar hoy?")


#importo la biblioteca time para usar la funcion sleep y hacer como que carga el programa (tambien importo sys para despue spoder cerrar el programa)

import sys

from time import perf_counter, sleep
n = 3
start = perf_counter()

print ("aguarde un momento...lo estamos redirigiendo a nuestra pagina principal")

for r in range(n):
    sleep(2)   
end = perf_counter()


#Hago la cuenta en de los segundos

hora = 11 * 3600
minutos = 6 * 60
segundos = 23 * 1    
total_sec = hora + minutos + segundos
    
    
#usando un if, revelo el dato del partido
#para que de bien el if escriba en minuscula y con un espacio

if tema == " tenis":
    
    print("")
    print ("Un dia como hoy, 24 de Junio, termino el partido de tenis más largo de la historia.")
    print("")
    sleep(5)
    
    print("Tuvo lugar entre el 22 y el 24 de junio de 2010, en la primera ronda del campeonato de Wimbledon 2010 de individuales masculino, entre el tenista estadounidense John Isner y el francés Nicolas Mahut.")
    print("")
    sleep(5)
    
    print("Con un tiempo de 11 horas, 6 minutos y 23 segundos; John Isner se impuso con un marcador de 6–4, 3–6, 6–7(7), 7–6(3), total: 70–68.") 
    print("")
    print("Duracion del partido en segundos:")
    print(total_sec)
    print("")
    
else:
    print("error #404")


#la conclusion, un comando paraterminar el script de ejecucion (copiar el input tal cual se muestra)

salir = input ("Para apagar el programa escriba '.Close' ")
if salir == ".Close":
    sys.exit()
else:
    print ("Error #404")