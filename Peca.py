import pygame
from constantes import *


class Peca(pygame.sprite.Sprite):
    def __init__(self, cor, posicao, linha_transforma_dama, direcao):
        self.cor = cor
        self.posicao = posicao
        self.dama = False
        self.linha_transforma_dama = linha_transforma_dama
        self.x = self.y = 0
        self.direcao = direcao
        self.calcula_pos()

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

    def desenha_peca(self, janela):

        pygame.draw.circle(janela, (0, 0, 0), (self.x, self.y), 25)
        pygame.draw.circle(janela, self.cor, (self.x, self.y), 20)
        if(self.dama):
            pygame.draw.circle(janela, (128, 128, 128), (self.x, self.y), 10)

    def movimenta_peca(self, nova_posicao):
        if(self.posicao != nova_posicao):
            self.posicao = nova_posicao
            self.calcula_pos()
            return True

        return False

    def movimentos_validos(self):
        if(not self.dama):
            return [[self.x + direcao, self.y - direcao], 
                    [self.x + direcao, self.y + direcao]]
        else:
            return [[self.x + direcao, self.y - direcao], 
                    [self.x + direcao, self.y + direcao]] #Modificar


    def __repr__(self):
        return str(self.cor)
