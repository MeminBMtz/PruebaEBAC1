import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
import random
import math

def guardar_datos(artist, monthly_listeners):
    with open("Datos_Definitivos_2024.txt", "a") as archivo:
        otro = "###" + str(monthly_listeners)
        archivo.write(artist+otro+"\n")

def crearFestival(fecha1, fecha2, fecha3):
    fechas = ["----- PRIMERA FECHA -----",
              "----- SEGUNDA FECHA -----",
              "----- TERCERA FECHA -----"]
    
    fechas2 = [fecha1, fecha2, fecha3]
    
    with open("Festival 2024.txt", "a") as archivo:
        for i in range(3):
            archivo.write(fechas[i]+"\n"+"\n")
            archivo.write(fechas2[i])

class Artista():
    def __init__(self, name, monthly_listeners):
        self.name = name
        self.monthlyL = monthly_listeners
    
    def getName(self):
        return self.name
    
    def getML(self):
        return self.monthlyL
    
    def toString(self):
        msg = self.name + " | " + "Monthly Listeners: " + str(self.monthlyL)
        print(msg)

datos = open("/Users/memobarbosa/Downloads/MDA/Datos_Definitivos_2024.txt","r")

nDatos = datos.read()
conjunto = nDatos.split("\n")
datos.close()

lista_buena = []
for artist in conjunto:
    if artist not in lista_buena:
        lista_buena.append(artist)

lista_buena.sort()
fest = []

for valores in lista_buena:
    parametros = valores.split("#")
    art = Artista(parametros[0], int(parametros[1]))
    fest.append(art)

fechas = ["6-12-2024", "7-12-2024",
          "8-12-2024"]

escenarios = ["ESCENARIO PRINCIPAL", "SECUNDARIO", "TERCIARIO", "CUARTO", "QUINTO"]

horasE5 = ["12:00 p.m. - 14:00 p.m.",
           "14:30 p.m. - 16:30 p.m.",
           "17:00 p.m. - 19:00 p.m.",
           "19:30 p.m. - 21:30 p.m."]

horasE4 = ["12:10 p.m. - 14:10 p.m.",
           "14:40 p.m. - 16:40 p.m.",
           "17:10 p.m. - 19:10 p.m.",
           "19:40 p.m. - 21:40 p.m."]

horasE3 = ["12:20 p.m. - 14:20 p.m.",
           "14:50 p.m. - 16:50 p.m.",
           "17:20 p.m. - 19:20 p.m.",
           "19:50 p.m. - 21:50 p.m."]

horasE2 = ["12:30 p.m. - 14:30 p.m.",
           "15:00 p.m. - 17:00 p.m.",
           "17:30 p.m. - 19:30 p.m.",
           "20:00 p.m. - 22:00 p.m."]

horasE1 = ["12:40 p.m. - 14:40 p.m.",
           "15:10 p.m. - 17:10 p.m.",
           "17:40 p.m. - 19:40 p.m.",
           "20:10 p.m. - 22:10 p.m."]

### 13 ###
fecha1 = fechas[0] + "\n" + "\n"
fecha2 = fechas[1] + "\n" + "\n"
fecha3 = fechas[2] + "\n" + "\n"
for escenario in escenarios:
    cont = 3
    fecha1 = fecha1 + escenario + "\n" + "\n"
    fecha2 = fecha2 + escenario + "\n" + "\n"
    fecha3 = fecha3 + escenario + "\n" + "\n"
    if escenarios.index(escenario) == 0:
        horas = horasE1
    elif escenarios.index(escenario) == 1:
        horas = horasE2
    elif escenarios.index(escenario) == 2:
        horas = horasE3
    elif escenarios.index(escenario) == 3:
        horas = horasE4
    elif escenarios.index(escenario) == 4:
        horas = horasE5

    for otro in range(0,4):
        hora = horas[cont-otro]
        nueva = []
        for j in fest:
            nueva.append(j.getML())

        nueva.sort()
        hml = nueva[-3:]
        hml.sort()
        heads = []
        maximo = len(fest)
        for k in range(4):
            for a in fest:
                if a.getML() == hml[k]:
                    heads.append(a)
                    for b in fest:
                        if b.getName() == a.getName():
                            fest.remove(b)
                            maximo = len(fest)
        if len(heads) != 0:
            fecha1 = fecha1 + heads[0].getName() + " | Monthly Listeners: " + str(heads[0].getML()) + " | Hora: " + hora + "\n"
            if len(heads) >= 2:
                fecha2 = fecha2 + heads[1].getName() + " | Monthly Listeners: " + str(heads[1].getML()) + " | Hora: " + hora + "\n"
                if len(heads) >= 3:
                    fecha3 = fecha3 + heads[2].getName() + " | Monthly Listeners: " + str(heads[2].getML()) + " | Hora: " + hora + "\n"
    cont -= 1
    
    fecha1 = fecha1 + "\n"
    fecha2 = fecha2 + "\n"
    fecha3 = fecha3 + "\n"

crearFestival(fecha1, fecha2, fecha3)