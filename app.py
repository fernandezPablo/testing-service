import requests
import time
import threading

#Valores de entrada de usuario
route = input('Url del servicio a ejecutar: ')
time_to_sleep = float(input('Tiempo de espera entre cada petición: '))
num_of_cores = int(input('Cantidad de hilos de ejcución: '))

def req_countries(route,time_to_sleep,number_of_thread):
    i = 1
    while(True):
        print('Procesando peticion: ', i, ' en hilo nº', number_of_thread)
        x = requests.get(route)
        print('Resultado de peticion ',i,' :', x.text, ' en hilo nº: ', number_of_thread)
        time.sleep(time_to_sleep)
        i += 1

threads = []
#Creando hilos de ejecución
for i in range(num_of_cores):
    threads.append(threading.Thread(target=req_countries, args=(route,time_to_sleep,str(i+1))))


#Iniciando hilos de ejecución
for thread in threads:
    thread.start()
