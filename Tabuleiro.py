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
    
    #Verifica qual casa foi clicada pelo mouse (Talvez apagar)
    def verifica_casa(self, posicao_x, posicao_y):
        
        print(posicao_x, posicao_y)
        for i in range(len(self.tabuleiro)):
            for j in range(len(self.tabuleiro[i])):
                if(posicao_x > self.tabuleiro[i][j][0] and posicao_x < self.tabuleiro[i][j][1] and  posicao_y > self.tabuleiro[i][j][2] and posicao_y < self.tabuleiro[i][j][3]):
                    if(self.tabuleiro[i][j][4]):
                        #self.tabuleiro[i][j][4].transforma_dama()#Somente para teste


                        local_selecionado = self.seleciona_local(i+1, j+1, self.tabuleiro[i][j][4])
                        if(local_selecionado):
                            self.tabuleiro[i+1][j+1][4] = self.tabuleiro[i][j][4]

                            self.tabuleiro[i][j][4] = None


                    
                    return self.tabuleiro[i][j]

    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


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
        
        for i in range(self.linhas):
            for j in range(self.colunas):
                peca = self.tabuleiro[i][j][4]

                if(peca != None):
                    peca.desenha_peca(janela)

    #Verifica o vencedor
    def vencedor(self):
        if(self.peca1 <= 0):
            return (255, 0, 0)
        
        elif(self.peca2 <=0):
            return (0, 0, 0)
        
        elif(self.peca1 == 1 and self.peca2 == 1):
            return (128,128,128) #Empate

    
    def valida_movimento(self, peca):
        movimentos = peca.movimentos_valido()

        for i in range(len(movimentos)):
            if(self.tabuleiro[movimentos[i]][4]):
                if(self.tabuleiro[movimentos[i]][4].cor != peca.cor):
                    movimentos[i] = [movimentos[i][0]+1, movimentos[i][1] + 1]
                else:
                    movimentos[i].remove()
            
        return movimentos
