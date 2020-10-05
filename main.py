import pygame
import PPlay
from Tabuleiro import *
from Jogo import *

pygame.font.init()

try:
    pygame.init()
except:
    print("O módulo não foi inicializado com sucesso.")

WIDTH = 480
HEIGHT = 480

# Define a janela
janela = pygame.display.set_mode((WIDTH, HEIGHT))

# Título
pygame.display.set_caption("Jogo de Dama")

# Cria o objeto Tabuleiro
tabuleiro = Tabuleiro(480, 480)
tabuleiro.atribui_casas()

jogo = Jogo(janela, tabuleiro)


def main():

    LOOP = True
    clock = pygame.time.Clock()
    FPS = 60

    while LOOP:
        clock.tick(FPS)

        if(jogo.vencedor() == None):
            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(event)
                    posx, posy = pygame.mouse.get_pos()
                    x, y = tabuleiro.pega_casa([posx, posy])

                    jogo.seleciona(x, y)

                elif event.type == pygame.QUIT:
                    LOOP = False

            jogo.atualiza()
        
        else:
            tabuleiro.desenha_tabuleiro(janela)
            pygame.font.init()
            print("asf")
            fonte = pygame.font.SysFont('Comic Sans MS', 30)
            if(jogo.vencedor() == (255, 0, 0)):
                texto = fonte.render("O Vermelho venceu!", True, (0,0,0))
                janela.blit(texto, (WIDTH/3.5,HEIGHT/2.5))
            elif(jogo.vencedor() == (0, 0, 0)):
                texto = fonte.render("O Branco venceu!", True, (0,0,0))
                janela.blit(texto, (WIDTH/3.5,HEIGHT/2.5))
            else:
                texto = fonte.render("Empate!", True, (0,0,0))
                janela.blit(texto, (WIDTH/3.5,HEIGHT/2.5))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    LOOP = False

            pygame.display.update()

    pygame.quit()


main()
