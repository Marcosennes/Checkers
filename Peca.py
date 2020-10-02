class Peca(pygame.sprite.Sprite):
    def __init__(self, cor, posicao, dama = False):
        self.cor = cor
        self.posicao = posicao
        self.dama = dama