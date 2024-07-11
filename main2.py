import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
import random
import math

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

datos = open("/Users/memobarbosa/Downloads/MDA/Datos_Definitivos_2023.txt","r")

nDatos = datos.read()
conjunto = nDatos.split("\n")
datos.close()

artists_list = []
for line in conjunto:
    if line:
        name, listeners = line.split("#")
        artist = Artista(name, int(listeners))
        artists_list.append(artist)

# Sort the list of artists by monthly listeners in descending order
artists_list.sort(key=lambda x: x.monthlyL, reverse=True)

# Print the sorted list
for artist in artists_list:
    msg = "\n" + str(artists_list.index(artist) + 1) + " | "
    print(msg, end=""); artist.toString()