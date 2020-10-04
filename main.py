import pygame
import PPlay
from Tabuleiro import *
from Jogo import *

pygame.font.init()

try:
    pygame.init()
except:
    print("O módulo não foi inicializado com sucesso.")

WIDTH   = 480
HEIGHT  = 480

#Define a janela
janela = pygame.display.set_mode((WIDTH, HEIGHT))

#Título
pygame.display.set_caption("Jogo de Dama")

#Cria o objeto Tabuleiro
tabuleiro = Tabuleiro(480,480)
tabuleiro.atribui_casas()
# tabuleiro.printa_vetor()

jogo = Jogo(janela)

def main():
    
    LOOP    = True
    clock = pygame.time.Clock()
    FPS = 60

    while LOOP:
        clock.tick(FPS)
        
        tabuleiro.desenha_tabuleiro(janela)

        for event in pygame.event.get():
            #print(event)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event)
                posx, posy = pygame.mouse.get_pos()
                x, y = tabuleiro.pega_casa([posx, posy])
                peca = tabuleiro.pega_peca(x, y)
                if(peca.cor == (255,0,0)):
                    tabuleiro.seleciona_local(6, 7, peca)
                
                elif(peca.cor == (255,255,255)):
                    tabuleiro.seleciona_local(1, 0, peca)

                #tabuleiro.verifica_casa(posx, posy)

            elif event.type == pygame.QUIT:
                LOOP = False

        pygame.display.update()

    pygame.quit()

main()