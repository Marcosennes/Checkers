import pygame
from Tabuleiro import Tabuleiro
from constantes import*
class Jogo:
    def __init__(self, janela, tabuleiro):
        self.selecionado = None
        self.tabuleiro = tabuleiro
        self.turno = BRANCO
        self.movimentos_validos = {}
        self.janela = janela
    
    def atualiza(self):
        self.tabuleiro.desenha_tabuleiro(self.janela)
        self.desenha_movimentos_validos(self.movimentos_validos)
        pygame.display.update()

    def reseta(self):        
        self.selecionado = None
        self.tabuleiro = tabuleiro
        self.turno = BRANCO
        self.movimentos_validos = {}

    def muda_turno(self):
        self.movimentos_validos = {}
        if(self.turno == VERMELHO):
            self.turno = BRANCO
        else:
            self.turno = VERMELHO

    def seleciona(self, coluna, linha):
        self.coluna = coluna
        self.linha = linha
        if(self.selecionado):
            resultado = self.movimenta(coluna, linha)
            if(not resultado):
                self.selecionado = None
                self.movimentos_validos = {}
                self.seleciona(coluna, linha)
        
        peca = self.tabuleiro.pega_peca(coluna, linha)
        if(peca and peca.cor == BRANCO):
            self.selecionado = peca
            self.movimentos_validos = self.tabuleiro.pega_movimentos_validos(peca)
            return True
        
        return False


    def movimenta(self, coluna, linha):
        peca = self.tabuleiro.pega_peca(coluna, linha)
        if(self.selecionado and not peca and (coluna, linha) in self.movimentos_validos):
            self.tabuleiro.movimenta(self.selecionado, coluna, linha)
            pulo = self.movimentos_validos[(coluna, linha)]
            if(pulo):
                self.tabuleiro.mata_pecas(pulo)
            self.muda_turno()
        else:
            return False
        
        return True

    def desenha_movimentos_validos(self, movimentos):
        if(movimentos):
            for movimento in movimentos:
                coluna, linha = movimento
                pygame.draw.circle(self.janela, (0, 255, 0), (int(coluna * QUADRADO + QUADRADO/2), int(linha * QUADRADO + QUADRADO/2) ), 25)
        #else:
        #    pygame.draw.polygon(self.janela, (200, 0, 0), [(self.linha + QUADRADO, self.coluna + QUADRADO)])

    def vencedor(self):
        return self.tabuleiro.vencedor()
