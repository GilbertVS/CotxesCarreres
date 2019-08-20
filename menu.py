import pygame
#-----------------  definició de la func joc_cotxe
def menu_prin() :
    while True :
        segon.tick(10)
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN : 
                if event.key == pygame.K_ESCAPE :
                    pygame.quit()
                    quit()
        finestre.fill((254, 254, 111))
        tipograf = pygame.font.Font("freesansbold.ttf", 40)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE] :
            pygame.quit()
            quit()
        if caixa_ample*7 > mouse[0] > caixa_ample and  caixa_alt*2 >mouse[1] >caixa_alt :    
            orange1, orange2, orange3 = (124, 67, 1), (254, 127, 1), (254, 127, 1)
            if click[0] == 1 or keys[pygame.K_RETURN] :
                from entrenament import jugar_partida
                jugar_partida(False, False)
        elif caixa_ample*7 > mouse[0] > caixa_ample and caixa_alt*3+40 >mouse[1] >caixa_alt*2+40 :
            orange1, orange2, orange3 = (254, 127, 1), (124, 67, 1), (254, 127, 1)
            if click[0] == 1 or keys[pygame.K_RETURN] :
                from competicio import jugar_partida2
                jugar_partida2(False, False)
        elif caixa_ample*7 > mouse[0] > caixa_ample and caixa_alt*5 >mouse[1] >caixa_alt*4 :
            orange1, orange2, orange3 = (254, 127, 1), (254, 127, 1), (124, 67, 1)
            if click[0] == 1 or keys[pygame.K_RETURN] :
                from competicio2 import jugar_partida3
                jugar_partida3(False, False)
        else :
            orange1, orange2, orange3 = (254, 127, 1), (254, 127, 1), (254, 127, 1)
        pygame.draw.rect(finestre, orange1, [caixa_ample, caixa_alt, caixa_ample*6, caixa_alt], 0)
        pygame.draw.rect(finestre, orange2, [caixa_ample, caixa_alt*2+40, caixa_ample*6, caixa_alt], 0)
        pygame.draw.rect(finestre, orange3, [caixa_ample, caixa_alt*4, caixa_ample*6, caixa_alt], 0) 
        entre = tipograf.render("Sala d'entrenaments", 1, (177, 7, 7))
        finestre.blit(entre, (caixa_ample+60, caixa_alt+25))   
        one = tipograf.render("1 jugador competició", 1, (177, 7, 7))
        finestre.blit(one, (caixa_ample+60, caixa_alt*2+25+40))
        two = tipograf.render("2 jugadodors competició", 1, (177, 7, 7))
        finestre.blit(two, (caixa_ample+60, caixa_alt*4+25))
        pygame.display.flip()
        tipograf2 = pygame.font.Font("freesansbold.ttf", 60)
        retol = tipograf2.render("Carrera d'obstacle !", 1, (244, 1, 1))
        finestre.blit(retol, (caixa_ample, caixa_alt*5+30))
        pygame.display.flip()
        
#---------------- inici del programa
pygame.init() # inici del mòdul "pygame"
segon = pygame.time.Clock() # assignació del temps del bucle
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
