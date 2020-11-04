import pygame
import PPlay
from Tabuleiro import *
from Jogo import *
import sys

pygame.font.init()

try:
    pygame.init()
except:
    print("O módulo não foi inicializado com sucesso.")

WIDTH = 480
HEIGHT = 480

fonte = pygame.font.SysFont(None, 42)

# Define a janela
janela = pygame.display.set_mode((WIDTH, HEIGHT))

# Título
titulo = 'Damas'
pygame.display.set_caption(titulo)

# Cria o objeto Tabuleiro
tabuleiro = Tabuleiro(480, 480)
tabuleiro.atribui_casas()

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)


def main():
    clock = pygame.time.Clock()
    FPS = 60
    click = False
    while True:
        clock.tick(FPS)   
        verde = (0, 200 , 0)
        vermelho = (200, 0, 0)     

        janela.fill((0, 0, 0))
        draw_text(titulo, fonte, (255, 255, 255), janela, WIDTH/2 , (HEIGHT)/4)

        mx, my = pygame.mouse.get_pos()

        botao1 = pygame.Rect(WIDTH/2 - 100, (HEIGHT)/3, 200, 50)
        botao2 = pygame.Rect(WIDTH/2 - 100, (HEIGHT)/3 + 100, 200, 50)

        if (botao1.collidepoint((mx, my))):
            verde = (0, 255 , 0)

            if (click):
                jogo()
                pass
        if (botao2.collidepoint((mx, my))):
            vermelho = (255, 0, 0)

            if (click):
                pygame.quit()
                pass

        pygame.draw.rect(janela, verde, botao1)
        draw_text("COMEÇAR", fonte, (0, 0, 0), janela, WIDTH/2 , (HEIGHT)/3 + 25) #+25 é a metade do tamanho do botão
        pygame.draw.rect(janela, vermelho, botao2)
        draw_text("SAIR", fonte, (0, 0, 0), janela, WIDTH/2, (HEIGHT)/3 + 125) #+125 é a distancia 100 + 25 do tamanho do botão

        click = False
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

            elif event.type == pygame.QUIT:
                pygame.quit()
        
        pygame.display.update()



def jogo():

    LOOP = True
    clock = pygame.time.Clock()
    FPS = 60
    jogo = Jogo(janela, tabuleiro)

    while LOOP:
        clock.tick(FPS)
        if(jogo.vencedor() == None):
            for event in pygame.event.get():
                # tabuleiro.conta_pecas(VERMELHO)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # print(event)
                    posx, posy = pygame.mouse.get_pos()
                    x, y = tabuleiro.pega_casa([posx, posy])

                    jogo.seleciona(x, y)

                elif event.type == pygame.QUIT:
                    LOOP = False

            jogo.atualiza()
        
        else:
            tabuleiro.desenha_tabuleiro(janela)
            pygame.font.init()
            fonte = pygame.font.SysFont('Comic Sans MS', 30)
            if(jogo.vencedor() == VERMELHO):
                texto = fonte.render("O Vermelho venceu!", True, (0,0,0))
                janela.blit(texto, (WIDTH/3.5,HEIGHT/2.5))
            elif(jogo.vencedor() == BRANCO):
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
