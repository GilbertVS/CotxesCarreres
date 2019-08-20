# -*- coding: utf-8 -*-
"""
Data: 20 d'agost 2019
Fitxer: Cotxe.py
Concepte: joc d'habilitat 
Autor: Gilbert Viader
"""
import pygame
import time
import random
from datetime import datetime
"""
importarem les llibreries pygame (controls de comandes i pantalles)
com la llibreria time per temporitzar un temps determinat
"""
from menu import menu_prin
from entrenament import jugar_partida
from competicio import jugar_partida2
from competicio2 import jugar_partida3        
#---------------- inici del programa
#pygame.init() # inici del mòdul "pygame"
dt = datetime.now()
random.seed(dt.second*13)
crash_sound = pygame.mixer.Sound("crash.wav")
finestr_ample = 800
finestr_alt = 600
finestre = pygame.display.set_mode((finestr_ample, finestr_alt))
pygame.display.set_caption("una carrera d'obstacles de competició")
# format de la finestra del joc
negre = (111, 111, 111)
blanc = (255, 255, 255)
roig = (211, 1, 1)
verd = (1, 211, 1)
caixa_ample, caixa_alt = 100, 80
# format dels colors en el joc
cotxe_ample = 75
# amplada del jugador
#segon = pygame.time.Clock() # assignació del temps del bucle
sortir, acabat  = False, False # assignació de la variable boolean
figur = pygame.image.load('racecar.png')
figur2 = pygame.image.load('racecar2.png')
# càrrega un arxiu d'imatge en la variable 'figur'
icona = pygame.image.load('carIcon.png')
pygame.display.set_icon(icona)
seny = pygame.image.load('senyal.png')
# càrrega de la senyal d'indicació del sentit
seny = pygame.transform.scale(seny, (90, 240))
#transformarem la senyal a unes dimensions més petites
#començar el joc crida de la funció joc_cotxe()
menu_prin()
