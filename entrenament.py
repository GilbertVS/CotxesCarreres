# importarem llibreries per els objectes de pygame
import pygame
#importarem llibreries per el nombre aleatori
import random
#importarem el mòdul del menú principal del joc de cotxes
from menu import menu_prin
#------------------- definició de funció cotxe
def cotxe(x,y) :
    finestre.blit(figur, (x,y))
    
#------------------- definició del contador de caixes
def contador(caixes) :
    font = pygame.font.SysFont(None, 25)
    text = font.render("Caixes: "+str(caixes), True, roig)
    finestre.blit(text,(0,0))

#------------------- definició de la funció textes objectes
def text_object(text, font) :
    textSurface = font.render(text, True, roig)
    return textSurface, textSurface.get_rect()

#------------------- definició de la funció missatge en pantalla
def message_display(text) :

    largeText = pygame.font.Font("freesansbold.ttf", 110)
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
            if m.key == pygame.K_LEFT or m.key == pygame.K_RIGHT or pygame == pygame.K_UP :
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
        crash, only1, pause = False, True, False
        # bucle infinit mentra el boolean sigui False
        x = finestr_ample * 0.45
        y = finestr_alt * 0.45
        # assignació a la posició central de la pantalla del jugador
        x_canvi = 0
        y_canvi = 0
        caixes_passades = 0
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
                        if moment.key == pygame.K_LEFT or moment.key == pygame.K_RIGHT :
                            x_canvi = 0
                            # inicialització dels incre / decre a zero en cas de deixar la tecla
                #print(moment)
            finestre.fill(blanc)
            # color de fons de la finestre
            x += x_canvi
            y += y_canvi
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
                    caixes_passades += 1
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
            if caixa_Y < y < caixa_Y+caixa_alt and caixa_X < x <caixa_X+caixa_ample :
                crash = True  
            if caixa_Y < y+cotxe_ample < caixa_Y+caixa_alt and caixa_X < x+cotxe_ample <caixa_X+caixa_ample :
                crash = True
                # acabar el joc hi ha una xoc
            if x > finestr_ample - cotxe_ample :
                x = 0
            if  x < 0 :
                x = finestr_ample - cotxe_ample
            if y > finestr_alt - cotxe_ample :
                y =0
            if y < 0 :
                y = finestr_alt - cotxe_ample
            contador(caixes_passades)
            # contador de les caixes esquivades
            if crash == True :
                if only1 == True :
                    only1 = False
                    pygame.mixer.Sound.play(crash_sound)
                    pygame.mixer.music.stop() 
                x_canvi, y_canvi = 0, 0
                message_display("caixes: "+str(caixes_passades))
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
        green, red, orange = (0, 133, 0), (244, 0, 0), (244, 122, 0)
        if click[0] == 1 or keys[pygame.K_RETURN] :
            jugar_partida(False, False)
    elif caixa_ample*4.5 > mouse[0] > caixa_ample*3.5 and cotxe_ample + caixa_alt*4 > mouse[1]>caixa_alt*4 :
        green, red, orange = (0, 244, 0), (244, 0, 0), (182, 61, 0)
        if click[0] == 1 or keys[pygame.K_RETURN] :
            menu_prin()
    elif caixa_ample*6 > mouse[0] > caixa_ample*5 and cotxe_ample + caixa_alt*4 >mouse[1] >caixa_alt*4 :
        red, green, orange = (133, 0, 0), (0, 244, 0), (244, 122, 0)
        if click[0] == 1 or keys[pygame.K_RETURN] :
            sortir_partida()
    else :
        green, red, orange = (0, 244, 0), (244, 0, 0), (244, 122, 0)
    pygame.draw.rect(finestre, green, [caixa_ample*2, caixa_alt*4, caixa_ample, cotxe_ample], 0)
    pygame.draw.rect(finestre, orange, [caixa_ample*3.5, caixa_alt*4, caixa_ample, cotxe_ample], 0)
    pygame.draw.rect(finestre, red, [caixa_ample*5, caixa_alt*4, caixa_ample, cotxe_ample], 0) 
    play = smallText.render("Jugar", 1, (7, 7, 7))
    finestre.blit(play, (caixa_ample*2+10, caixa_alt*4+20))   
    show = smallText.render("Menú", 1, (7, 7, 7))
    finestre.blit(show, (caixa_ample*3.5+10, caixa_alt*4+20))
    quited = smallText.render("Sortir", 1, (7, 7, 7))
    finestre.blit(quited, (caixa_ample*5+10, caixa_alt*4+20))

#---------------- inici del programa
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
caixa_ample, caixa_alt = 100, 80
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
