import pygame
pygame.font.init()

try:
    pygame.init()
except:
    print("O módulo não foi inicializado com sucesso.")

WIDTH   = 600
HEIGHT  = 600
LOOP    = True

#Define a janela
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#Título
pygame.display.set_caption("Jogo de Dama")

#Carregamento do background
background = pygame.image.load("assets/images/background.jpg")


while LOOP:

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    pygame.draw.rect(screen, (0, 0, 0), [40, 40, 60, 60])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            LOOP = False

    pygame.display.update()