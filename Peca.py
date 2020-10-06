import pygame
from constantes import *


class Peca(pygame.sprite.Sprite):
    def __init__(self, cor, posicao, linha_transforma_dama, direcao):
        self.cor = cor
        if(self.cor == VERMELHO):
            self.cor_peca       = pygame.image.load("assets/images/peca_vermelha.png")
            self.cor_dama       = pygame.image.load("assets/images/dama_vermelha.png")
            self.morte_sprite   = [pygame.image.load("assets/images/morte_vermelha_1.png"), pygame.image.load("assets/images/morte_vermelha_2.png"), pygame.image.load("assets/images/morte_vermelha_3.png")]
        elif(self.cor == BRANCO):
            self.cor_peca       = pygame.image.load("assets/images/peca_branca.png")        
            self.cor_dama       = pygame.image.load("assets/images/dama_branca.png")        
            self.morte_sprite   = [pygame.image.load("assets/images/morte_branca_1.png"), pygame.image.load("assets/images/morte_branca_2.png"), pygame.image.load("assets/images/morte_branca_3.png")]
        self.posicao = posicao
        self.dama = False
        self.linha_transforma_dama = linha_transforma_dama
        self.x = self.y = 0
        self.direcao = direcao
        self.calcula_pos()
        self.morte = False

    # Calcula a posição em que cada peça vai ficar no tabuleiro
    def calcula_pos(self):
        self.x_inicial = self.posicao[0]*LARGURA/8
        self.y_inicial = self.posicao[1]*ALTURA/8

        self.x = int((self.x_inicial) + QUADRADO/2)
        # +30 vem da metade do tamanho do quadrado em px
        self.y = int((self.y_inicial) + QUADRADO/2)

    def transforma_dama(self, x):
        if(x == self.linha_transforma_dama):
            self.dama = True

    def mata_peca(self):
        self.morte = True

    def desenha_peca(self, janela):
        if(self.morte):
            janela.blit(self.morte_sprite[0], (self.x - 27, self.y - 27))
        else:
            # pygame.draw.circle(janela, (0, 0, 0), (self.x, self.y), 25)
            janela.blit(self.cor_peca, (self.x - 27, self.y - 27))
            #pygame.draw.circle(janela, self.cor, (self.x, self.y), 20)
            if(self.dama):
                janela.blit(self.cor_dama, (self.x - 27, self.y - 27))
                # pygame.draw.circle(janela, (128, 128, 128), (self.x, self.y), 10)

    def movimenta_peca(self, nova_posicao):
        if(self.posicao != nova_posicao):
            self.posicao = nova_posicao
            self.calcula_pos()
            return True

        return False


