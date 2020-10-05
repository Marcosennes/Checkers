import pygame
from Peca import *
from constantes import *

class Tabuleiro:
    def __init__(self, altura = ALTURA, largura = LARGURA):
        self.altura = altura
        self.largura = largura
        self.tabuleiro = []
        
        self.linhas = LINHA 
        self.colunas = COLUNA

        self.peca1 = self.peca2 = 12
        self.dama1 = self.dama2 = 0


    #Atribui a cada sua posição em px
    def atribui_casas(self):
        for i in range(self.colunas):
            linha=[]
            if((i+1)%2 == 0):
                coloca_peca = True
            else:
                coloca_peca = False

            for j in range(self.linhas):
                x_inicial   = i*self.largura/8
                x_final     = self.largura/8    + (i*self.largura/8)
                y_inicial   = j*self.altura/8
                y_final     = self.altura/8     + (j*self.altura/8)

                if(j < 3 and coloca_peca):               
                    linha.append([x_inicial, x_final, y_inicial, y_final, Peca( (255, 0, 0), [i, j], LINHA-1, 1)])
                    coloca_peca = not(coloca_peca)
                elif(j > 4 and coloca_peca):
                    linha.append([x_inicial, x_final, y_inicial, y_final, Peca( (255, 255, 255), [i, j], 0, -1) ])
                    coloca_peca = not(coloca_peca)
                else:
                    linha.append([x_inicial, x_final, y_inicial, y_final, None])
                    coloca_peca = not(coloca_peca)

            self.tabuleiro.append(linha)

    def printa_vetor(self):
        cont = 1
        for i in range(len(self.tabuleiro)):
            for j in range(len(self.tabuleiro[i])):
                print(cont)
                print(self.tabuleiro[i][j])
                cont += 1

    #Movimenta a peca no tabuleiro
    def movimenta(self, peca, x, y):
        self.tabuleiro[peca.posicao[0]][peca.posicao[1]], self.tabuleiro[x][y] = self.tabuleiro[x][y], self.tabuleiro[peca.posicao[0]][peca.posicao[1]]
        peca.movimenta_peca([x, y])
        peca.transforma_dama(y)

    #Retorna a peça
    def pega_peca(self, coluna, linha):
        return self.tabuleiro[coluna][linha][4]        

    #Retorna em qual casa foi clicada
    def pega_casa(self, pos):
        x, y = pos
        linha = int(y // (QUADRADO))
        coluna = int(x // (QUADRADO))

        return coluna, linha

    #Verifica se o local selecionado é diferente do que a peça já está
    def seleciona_local(self, x, y, peca):
        if(peca):
            if(x != peca.posicao[0] or y != peca.posicao[1]):
                self.movimenta(peca, x, y)
                return True
        
        return False

    #Desenha um tabuleiro na tela
    def desenha_tabuleiro(self, janela):
        
        #Carregamento do background
        janela.fill((0, 0, 0))
        background = pygame.image.load("assets/images/background.png")
        janela.blit(background, (0, 0))
        
        for i in range(self.colunas):
            for j in range(self.linhas):
                peca = self.pega_peca(i, j)

                if(peca != None):
                    peca.desenha_peca(janela)

    #Verifica o vencedor
    def vencedor(self):
        if(self.peca1 <= 0):
            return (0, 0, 0)
        
        elif(self.peca2 <=0):
            return (255, 0, 0)
        
        elif(self.peca1 == 1 and self.peca2 == 1):
            return (128,128,128) #Empate

        return None


    def remove(self, pecas):
        for peca in pecas:
            self.tabuleiro[peca.posicao[0]][peca.posicao[1]][4] = None
            if(peca):
                if(peca.cor == (255,0,0)):
                    self.peca1 -= 1
                else:
                    self.peca2 -= 1

    def pega_movimentos_validos(self, peca):
        movimentos = {}
        esquerda = peca.posicao[0] - 1
        direita = peca.posicao[0] + 1
        linha = peca.posicao[1]

        if(peca.cor == (255,0,0) or peca.dama):
            movimentos.update(self._diagonal_esquerda(linha + 1, min(linha + 3, LINHA), 1, peca.cor, esquerda))
            movimentos.update(self._diagonal_direita(linha + 1, min(linha + 3, LINHA), 1, peca.cor, direita))
        if(peca.cor == (255,255,255) or peca.dama):
            movimentos.update(self._diagonal_esquerda(linha - 1, max(linha - 3, -1), -1, peca.cor, esquerda))
            movimentos.update(self._diagonal_direita(linha - 1, max(linha - 3, -1), -1, peca.cor, direita))
        
        return movimentos

    def _diagonal_esquerda(self, inicio, parada, passo, cor, esquerda, pulo=[]):
        movimentos = {}
        ultimo = []
        for r in range(inicio, parada, passo):
            if esquerda < 0:
                break
            
            atual = self.pega_peca(esquerda, r)
            if not atual:
                if pulo and not ultimo:
                    break
                elif pulo:
                    movimentos[(esquerda, r)] = ultimo + pulo
                else:
                    movimentos[(esquerda, r)] = ultimo
                
                if ultimo:
                    if passo == -1:
                        linha = max(r-3, 0)
                    else:
                        linha = min(r+r, LINHA)
                    movimentos.update(self._diagonal_esquerda(r+passo, linha, passo, cor, esquerda-1, pulo=ultimo))
                    movimentos.update(self._diagonal_direita(r+passo, linha, passo, cor, esquerda+1, pulo=ultimo))
                break
            elif atual.cor == cor:
                break
            else:
                ultimo = [atual]

            esquerda -= 1
        
        return movimentos

    def _diagonal_direita(self, inicio, parada, passo, cor, direita, pulo=[]):
        movimentos = {}
        ultimo = []
        for r in range(inicio, parada, passo):
            if direita >= COLUNA:
                break
            
            atual = self.pega_peca(direita, r)
            if not atual:
                if pulo and not ultimo:
                    break
                elif pulo:
                    movimentos[(direita, r)] = ultimo + pulo
                else:
                    movimentos[(direita, r)] = ultimo
                
                if ultimo:
                    if passo == -1:
                        linha = max(r-3, 0)
                    else:
                        linha = min(r+r, LINHA)
                    movimentos.update(self._diagonal_esquerda(r+passo, linha, passo, cor, direita-1,pulo=ultimo))
                    movimentos.update(self._diagonal_direita(r+passo, linha, passo, cor, direita+1,pulo=ultimo))
                break
            elif atual.cor == cor:
                break
            else:
                ultimo = [atual]

            direita += 1
        
        return movimentos