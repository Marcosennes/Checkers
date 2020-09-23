import pygame
pygame.font.init()

try:
    pygame.init()
except:
    print("O módulo não foi inicializado com sucesso.")

WIDTH   = 800
HEIGHT  = 800
LOOP    = True

#Define a janela
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#Título
pygame.display.set_caption("Jogo de Dama")

background = pygame.image.load("assets/images/background.jpg")


while LOOP:
    screen.blit(background)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            LOOP = False

    pygame.display.update()