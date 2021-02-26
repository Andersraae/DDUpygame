import pygame, sys

def DrawFloor():
    screen.blit(floorSurface,(floor_x_pos,900))
    screen.blit(floorSurface,(floor_x_pos+576,900))

def CreatePipe(): #Laver rektangler til nye pipes
    randomPipePos = random.choice(pipeHeight)
    newPipe = pipeSurface.get_rect(midtop = (700,randomPipePos))
    return newPipe

def MovePipes(pipes): #Denne funktion flytter alle pipies til venstre med 5 pr tick
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes

def DrawPipes(pipes):
    for pipe in pipes:
        screen.blit(pipeSurface, pipe)

pygame.init()

screen = pygame.display.set_mode((576,1024)) #Opretter et display surface med given størrelse
clock = pygame.time.Clock() #Styrer refreshrate/tickrate af spillet

#Spil variable
gravity = 0.25
birdMovement = 0

#Find billeder og lyde og læg dem i hver deres mapper
bgSurface = pygame.image.load('assets/background-day.png').convert()
bgSurface = pygame.transform.scale2x(bgSurface) #Opskalerer billedet

#Gulv
floorSurface = pygame.image.load('assets/base.png').convert()
floorSurface = pygame.transform.scale2x(floorSurface) #Opskalerer billedet
floor_x_pos = 0

#Sprite
birdSurface = pygame.image.load('assets/bluebird-midflap.png').convert()
birdSurface = pygame.transform.scale2x(birdSurface)
birdRect = birdSurface.get_rect(center = (100,512))

#Pipes
pipeSurface = pygame.image.load('assets/pipe-green.png')
pipeSurface = pygame.transform.scale2x(pipeSurface)
pipeList = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200) #Spawner ny pipe hver 1200 millisekund.
pipeHeight = [400,600,800]

while True: #Gameloop så spillet bliver ved med at være åbent
    for event in pygame.event.get(): #Tjekker alle events i spillet
        if event.type == pygame.QUIT: #Hvis eventet er at gå ud så skal den lukke spillet.
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                birdMovement = 0
                birdMovement -= 12
        if event.type == SPAWNPIPE:
            pipeList.append(CreatePipe())

    screen.blit(bgSurface,(0,0)) #Indsæt bgSurface med koordinaterne 0,0 på display sruface

    #Sprite
    birdMovement += gravity #Gør birdMovement gravity større pr tick
    birdRect.centery += birdMovement #Bevæger sig med birdMovement farten i y retningen
    screen.blit(birdSurface, birdRect) #Indsætter rektanglen så man kan tjekke efter kollision

    #pipeSurface
    pipeList = MovePipes(pipeList)
    DrawPipes(pipeList)

    #Gulv
    floor_x_pos -= 1
    DrawFloor()
    if floor_x_pos <= -576:
        floor_x_pos = 0

    pygame.display.update() #Opdaterer display surface
    clock.tick(144) #Sætter tickrate
