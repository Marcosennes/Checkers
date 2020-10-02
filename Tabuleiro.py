class Tabuleiro:
    def __init__(self, altura=480, largura=480):
        self.altura = altura
        self.largura = largura
        self.tabuleiro = []


    def atribui_casas(self):
        for i in range(8):
            linha=[]
            for j in range(8):
                x_inicial   = i*self.largura/8
                x_final     = self.largura/8    + (i*self.largura/8)
                y_inicial   = j*self.altura/8
                y_final     = self.altura/8     + (j*self.altura/8)
                linha.append((x_inicial, x_final, y_inicial, y_final))
            self.tabuleiro.append(linha)

    def printa_vetor(self):
        cont = 1
        for i in range(len(self.tabuleiro)):
            for j in range(len(self.tabuleiro[i])):
                print(cont)
                print(self.tabuleiro[i][j])
                cont += 1
    
    def verifica_casa(self, posicao_x, posicao_y):
        for i in range(len(self.tabuleiro)):
            for j in range(len(self.tabuleiro[i])):
                if(posicao_x > self.tabuleiro[i][j][0] and posicao_x < self.tabuleiro[i][j][1] and  posicao_y > self.tabuleiro[i][j][2] and posicao_y < self.tabuleiro[i][j][3]):
                    print(self.tabuleiro[i][j])
                    return self.tabuleiro[i][j]