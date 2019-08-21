# -*- coding: utf-8 -*-
"""
Data: 18 d'agost 2019
Fitxer: CotxeCompeticio2.py
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
dt = datetime.now()
random.seed(dt.second*13)
def meta(metaX, metaY, ampleM, altM, color) :
    pygame.draw.rect(finestre, color, [metaX, metaY, ampleM, altM])
    pygame.draw.rect(finestre, color, [metaX+ampleM*2, metaY, ampleM, altM])
    pygame.draw.rect(finestre, color, [metaX+ampleM*4, metaY, ampleM, altM])
    pygame.draw.rect(finestre, color, [metaX+ampleM*6, metaY, ampleM, altM])
    pygame.draw.rect(finestre, color, [metaX+ampleM*8, metaY, ampleM, altM])
    pygame.draw.rect(finestre, color, [metaX+ampleM*10, metaY, ampleM, altM])
    pygame.draw.rect(finestre, color, [metaX+ampleM*12, metaY, ampleM, altM])
    pygame.draw.rect(finestre, color, [metaX+ampleM, metaY+altM, ampleM, altM])
    pygame.draw.rect(finestre, color, [metaX+ampleM*3, metaY+altM, ampleM, altM])
    pygame.draw.rect(finestre, color, [metaX+ampleM*5, metaY+altM, ampleM, altM])
    pygame.draw.rect(finestre, color, [metaX+ampleM*7, metaY+altM, ampleM, altM])
    pygame.draw.rect(finestre, color, [metaX+ampleM*9, metaY+altM, ampleM, altM])
    pygame.draw.rect(finestre, color, [metaX+ampleM*11, metaY+altM, ampleM, altM])
    pygame.draw.rect(finestre, color, [metaX, metaY+altM*2, ampleM, altM])
    pygame.draw.rect(finestre, color, [metaX+ampleM*2, metaY+altM*2, ampleM, altM])
    pygame.draw.rect(finestre, color, [metaX+ampleM*4, metaY+altM*2, ampleM, altM])
    pygame.draw.rect(finestre, color, [metaX+ampleM*6, metaY+altM*2, ampleM, altM])
    pygame.draw.rect(finestre, color, [metaX+ampleM*8, metaY+altM*2, ampleM, altM])
    pygame.draw.rect(finestre, color, [metaX+ampleM*10, metaY+altM*2, ampleM, altM])
    pygame.draw.rect(finestre, color, [metaX+ampleM*12, metaY+altM*2, ampleM, altM])

#------------------- definició de la funció del senyal d'indicació
def senyal(x, y) :
    finestre.blit(seny, (x,y))
    
#------------------- definició de funció cotxe
def cotxe(x,y) :
    finestre.blit(figur, (x,y))

def cotxe2(x, y) :
    finestre.blit(figur2, (x, y))
    
#------------------- definició del contador de caixes
def contador(p, p2) :
    font = pygame.font.SysFont(None, 25)
    text1 = font.render("Jugador 1: "+str(p), True, verd) 
    text2 = font.render("Jugador 2: "+str(p2), True, roig)
    finestre.blit(text1,(0,0))
    finestre.blit(text2,(0,15))

#------------------- definició de la funció textes objectes
def text_object(text, font) :
    textSurface = font.render(text, True, roig)
    return textSurface, textSurface.get_rect()

#------------------- definició de la funció missatge en pantalla
def message_display(text) :

    largeText = pygame.font.Font("freesansbold.ttf", 100)
    TextSurf, TextRect = text_object(text, largeText)
    TextRect.center = ((finestr_ample/2),(finestr_alt/2))
    finestre.blit(TextSurf, TextRect)
           
#-------------------- definifió de la funció caixes
def caixes(caixaX, caixaY, caixaW, caixaH, color) :
    pygame.draw.rect(finestre, color, [caixaX, caixaY, caixaW, caixaH])

#----------------------- definició de sortir partida
def sortir_partida() :
    pygame.quit()
    quit()

#----------------------- definició de la funció pause
def paused(p) :
    for m in pygame.event.get() :
        if m.type == pygame.QUIT :
            sortir_partida()
        elif m.type == pygame.KEYDOWN :
            if m.key == pygame.K_ESCAPE :
                sortir_partida()
            if m.key == pygame.K_LEFT or m.key == pygame.K_RIGHT or m.key == pygame.K_UP :
                p = False
            if m.key == pygame.K_SPACE or m.key == pygame.K_DOWN or m.key == 112 :
                p = False
    message_display("PAUSA")
    pygame.mixer.music.pause()
    pygame.display.flip()
    return p
    
# --------------------- definició dejuigar partida
def jugar_partida(sortir, acabat) :
    while not sortir :
        pygame.mixer.music.load('dance.mp3')
        pygame.mixer.music.play(-1)
        crash, only1, pause, mort1, mort2 = False, True, False, False, False
        # bucle infinit mentra el boolean sigui False
        x, x2 = finestr_ample * 0.65, finestr_ample * 0.35
        y, y2 = finestr_alt * 0.65, finestr_alt * 0.65
        # assignació a la posició central de la pantalla del jugador
        x_canvi, x_canvi2 = 0, 0
        y_canvi, y_canvi2 = 0, 0
        punts, punts2 = 0, 0
        caixes_aleatories = 1
        # inicialització variables de modificació del jugador
        #-------------------- caixes aleatoriament
        caixa_X = random.randrange(0, finestr_ample-100)
        caixa_Y = -finestr_alt
        velocitat = 2
        caixa_ample = 100
        caixa_alt = 100
        # posició aleatòria per la primera caixa de sortida
        while not acabat :
            while pause :
                pause = paused(pause)
                if pause == False :
                    pygame.mixer.music.unpause()
                pygame.display.update()
                segon.tick(60)
            for moment in pygame.event.get() :
                if moment.type == pygame.QUIT :
                    sortir_partida()
                # sortir del bucle si el tipus de 'moment' igual QUIT
                if crash == False:
                    if moment.type == pygame.KEYDOWN : # en cas pulsada una tecla incre o decr
                        if moment.key == pygame.K_ESCAPE :
                            sortir_partida()
                        if moment.key == 112 :
                            pause = True
                        if moment.key == 119 :
                            y_canvi2 = -2.5
                        if moment.key == 115 :
                            y_canvi2 = 2.5
                        if moment.key == 97 :
                            x_canvi2 = -5
                        if moment.key == 100 :
                            x_canvi2 = 5
                        if moment.key == pygame.K_UP :
                            y_canvi = -2.5
                        if moment.key == pygame.K_DOWN:
                            y_canvi = 2.5
                        if moment.key == pygame.K_LEFT :
                            x_canvi = -5
                        elif moment.key == pygame.K_RIGHT :
                            x_canvi = 5
                            # increment o decrement en el cas de pulsar la tecla
                    if moment.type == pygame.KEYUP : # en cas de deixar pulsar la tecla 
                        if moment.key == pygame.K_UP or moment.key == pygame.K_DOWN :
                            y_canvi = 0
                        if moment.key == 119 or moment.key == 115 :
                            y_canvi2 = 0
                        if moment.key == pygame.K_LEFT or moment.key == pygame.K_RIGHT :
                            x_canvi = 0
                        if moment.key == 97 or moment.key == 100 :
                            x_canvi2 = 0
                            # inicialització dels incre / decre a zero en cas de deixar la tecla
                #print(moment)
            finestre.fill(blanc)
            senyal(finestr_ample*0.2, finestr_alt*0.25) #crida la funció del senyal per dibuixar-lo
            senyal(finestr_ample*0.45, finestr_alt*0.25) #crida la funció del senyal per dibuixar-lo
            senyal(finestr_ample*0.7, finestr_alt*0.25)
            meta(120, 0, 40, 20, (0, 0, 0))
            # color de fons de la finestre
            x += x_canvi
            y += y_canvi
            x2 += x_canvi2
            y2 += y_canvi2
            if mort2 == False :
                cotxe2(x2, y2)
            if mort1 == False :
                cotxe(x, y) # crida de la funció cotxe amb nou valor de coordenades
            #crida per la funció caixes per la posició de la caixa en cada moment
            caixes(caixa_X, caixa_Y, caixa_ample, caixa_alt, negre)
            if crash == False :
                if caixes_aleatories == 1 :
                    caixa_Y += velocitat
                elif caixes_aleatories == 2 :
                    caixa_Y -= velocitat
                elif caixes_aleatories == 3 :
                    caixa_X -= velocitat
                else:
                    caixa_X += velocitat
                # per cada possibilitat de sortida de la nova caixa hi ha canvi en posició
                if caixa_Y > finestr_alt or  caixa_X > finestr_ample or caixa_Y < 0 or caixa_X < 0 : # en el cas de la caixa surti dels limits de la pantalla
                    if mort1 == False :
                        punts += 1
                    if mort2 == False :
                        punts2 += 1
                    velocitat +=1
                    caixa_ample += 5
                    caixa_alt += 5
                    caixes_aleatories = random.randint(1,4)
                    if caixes_aleatories == 1 :
                        caixa_Y = 0
                        caixa_X = random.randrange(0, finestr_ample-100)
                    elif caixes_aleatories == 2 :
                        caixa_Y = 0 + finestr_alt
                        caixa_X = random.randrange(0, finestr_ample-100) 
                    elif caixes_aleatories == 3 :
                        caixa_Y = random.randrange(0, finestr_alt-100)
                        caixa_X = 0 + finestr_ample
                    else :
                        caixa_Y = random.randrange(0, finestr_alt-100)
                        caixa_X = 0 
                # A determinar aleatòriament la possició de la nova caixa
            if y < y <y+cotxe_ample and x2<x<x2+cotxe_ample and mort1 == False :
                x = x2+corxe_ample
            if x<x2<x+cotxe_ample and y<y2<y+cotxe_ample and mort2 ==False :
                x2 = x-cotxe_ample

            if caixa_Y < y < caixa_Y+caixa_alt and caixa_X < x <caixa_X+caixa_ample :
                mort1 = True
                if mort2 == True :
                    crash = True  
            if caixa_Y < y+cotxe_ample < caixa_Y+caixa_alt and caixa_X < x+cotxe_ample <caixa_X+caixa_ample :
                mort1 = True
                if mort2 == True :
                    crash = True
            if caixa_Y < y2 < caixa_Y+caixa_alt and caixa_X < x2 <caixa_X+caixa_ample :
                mort2 = True
                if mort1 == True : 
                    crash = True  
            if caixa_Y < y2+cotxe_ample < caixa_Y+caixa_alt and caixa_X < x2+cotxe_ample <caixa_X+caixa_ample :
                mort2 = True
                if mort1 == True :
                    crash = True
                # acabar el joc hi ha una xoc
            if x > finestr_ample - cotxe_ample :
                x = 0
            if  x < 0 :
                x = finestr_ample - cotxe_ample
            if y > finestr_alt - cotxe_ample :
                y =0
                if mort1 == False :
                    punts -= 3
            if y < 0 :
                y = finestr_alt - cotxe_ample
                if mort1 == False :
                    punts += 3
            if x2 > finestr_ample - cotxe_ample :
                x2 = 0
            if  x2 < 0 :
                x2 = finestr_ample - cotxe_ample
            if y2 > finestr_alt - cotxe_ample :
                y2 =0
                if mort2 == False :
                    punts2 -= 3
            if y2 < 0 :
                y2 = finestr_alt - cotxe_ample
                if mort2 == False :
                    punts2 += 3
            contador(punts, punts2)
            # contador de les caixes esquivades
            if crash == True :
                if only1 == True :
                    only1 = False
                    pygame.mixer.Sound.play(crash_sound)
                    pygame.mixer.music.stop() 
                x_canvi, x_canvi2, y_canvi, y_canvi2 = 0, 0, 0, 0
                if punts > punts2 :
                    message_display("VERD: "+str(punts)+" punts")
                if punts == punts2 :
                    message_display("empat: "+str(punts)+" punts")
                if punts < punts2 :
                    message_display("ROIG: "+str(punts2)+" punts")
                butons(finestre, caixa_ample, caixa_alt, cotxe_ample)
            pygame.display.flip()
            pygame.display.update()
            segon.tick(60)
            # són 60 cop per cada segon
            
# --------------------- definició per imprimir el botons
def butons(finestre, caixa_ample, caixa_alt, cotxe_ample) :
    caixa_ample, caixa_alt = 100, 100
    smallText = pygame.font.Font(None, int(40))    
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE] :
        sortir_partida()
    if caixa_ample*3 > mouse[0] > caixa_ample*2 and cotxe_ample + caixa_alt*4 >mouse[1] >caixa_alt*4 :    
        green, red = (0, 133, 0), (244, 0, 0)
        if click[0] == 1 or keys[pygame.K_RETURN] :
            jugar_partida(False, False)
    elif caixa_ample*6 > mouse[0] > caixa_ample*5 and cotxe_ample + caixa_alt*4 >mouse[1] >caixa_alt*4 :
        red, green = (133, 0, 0), (0, 244, 0)
        if click[0] == 1 or keys[pygame.K_RETURN] :
            sortir_partida()
    else :
        green, red = (0, 244, 0), (244, 0, 0)
    pygame.draw.rect(finestre, green, [caixa_ample*2, caixa_alt*4, caixa_ample, cotxe_ample], 0)
    pygame.draw.rect(finestre, red, [caixa_ample*5, caixa_alt*4, caixa_ample, cotxe_ample], 0) 
    play = smallText.render("Jugar", 1, (7, 7, 7))
    finestre.blit(play, (caixa_ample*2+10, caixa_alt*4+20))   
    quited = smallText.render("Sortir", 1, (7, 7, 7))
    finestre.blit(quited, (caixa_ample*5+10, caixa_alt*4+20))
    
#-------------------- inici del programa
pygame.init() # inici del mòdul "pygame"
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
# format dels colors en el joc
cotxe_ample = 75
# amplada del jugador
segon = pygame.time.Clock() # assignació del temps del bucle
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
while True:
    segon.tick()
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            sortir_partida()
        if event.type == pygame.KEYDOWN : 
            if event.key == pygame.K_ESCAPE :
                sortir_partida()
    finestre.fill(blanc)
    message_display("competició 2")
    butons(finestre, 100, 100, cotxe_ample)
    pygame.display.flip()
