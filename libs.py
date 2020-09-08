# -*- coding: utf-8 -*-
import os
import psutil as p
import urllib
#import httplib 
import requests
import time as t

# Obtiene la velocidad y la utilización del objeto CPU
class cpu():
    def __init__(self):
        self.utilizacion= p.cpu_percent(interval=0.1)
        self.velocidad= int(p.cpu_freq()[0])

    def utilities(self):
        u = {'u':round(self.utilizacion,3),'v':round(self.velocidad,3)}
        return u

#Se crea el objeto Soc, obteniendose la temperatura del cpu y del gpu
class Soc():
    #Valido para arquitecturas de Gpu integradas al Cpu(temperature zone)
    def __init__(self,dispositivo):
        self.dispositivo = dispositivo
    def temperature(self):
         temp = p.sensors_temperatures()[self.dispositivo][0][1]
         return round(temp,3)

#Objeto memory, se obtiene la utilización de la memoria fisica y swap
class memory():
    def __init__(self):
        self.fm = p.virtual_memory()
        self.sm = p.swap_memory()
    def percentual(self):
        p = {'f':round(self.fm[2],3),'s':round(self.sm[3],3)}
        return p

#Establece una conexión http y escribe en la API
class write_api():
    wrcount = 0
    def __init__(self,parameters):
        self.parameters = parameters
        self.key = str(open(os.getcwd()+"/keys.txt","r").read()).strip()
        self.header = {"Content-typZZe":"application/x-www-form-urlencoded","Accept":"text/plain"}
        write_api.wrcount += 1

    def write(self):
        self.parameters['key'] = self.key
        print(self.parameters)
        #conexion = httplib2.HTTPConnection("api.thingspeak.com:80")
        conexion = requests.get("api.thingspeak.com:80")
        conexion.request("POST","/update",urllib.parse.urlencode(self.parameters),self.header)
        conexion.getresponse()# se no se trae la respuesta no se envian los datos
        





