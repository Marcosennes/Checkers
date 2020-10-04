import pygame
from Tabuleiro import Tabuleiro
from constantes import*

class Jogo:
    def __init__(self, janela):
        self.selecionado = None
        self.tabuleiro = Tabuleiro()
        self.turno = (255, 0, 0)
        self.valida_movimento = {}
        self.janela = janela
    
    def atualiza(self):
        self.desenha_tabuleiro(self.janela)
        pygame.display.update()

    
    def reseta(self):        
        self.selecionado = None
        self.tabuleiro = Tabuleiro()
        self.turno = (255, 0, 0)
        self.valida_movimento = {}

    def muda_turno(self):
        self.valida_movimento = {}
        if(self.turno == (255, 0, 0)):
            self.turno = (0, 0, 0)
        else:
            self.turno = (255, 0, 0)

    def seleciona(self, coluna, linha):
        if(self.selecionado):
            resultado = self.movimenta(coluna, linha)
            if(not resultado):
                self.selecionado = None
                self.seleciona(coluna, linha)
        
        peca = self.tabuleiro.pega_peca(coluna, linha)
        if(peca and peca.cor == self.turno):
            self.selecionado = peca
            self.valida_movimento = self.tabuleiro.pega_movimentos_validos(peca)
            return True
        
        return False


    def movimenta(self, coluna, linha):
        peca = self.tabuleiro.pega_peca(coluna, linha)
        if(self.selecionado and not peca and (coluna, linha) in self.valida_movimento):
            self.tabuleiro.movimenta(peca, [coluna, linha])
            self.muda_turno()
        else:
            return False
        
        return True
    
    def desenha_movimentos_validos(self, movimentos):
        for movimento in movimentos:
            coluna, linha = movimento
            pygame.draw.circle(self.win, (0, 255, 0), (coluna * QUADRADO + QUADRADO//2, linha * QUADRADO + QUADRADO//2), 15)
    
    def vencedor(self):
        return self.tabuleiro.vencedor()