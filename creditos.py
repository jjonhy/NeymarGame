import pygame
from obj import Obj


class Creditos:
    def __init__(self):
        self.todas_sprites = pygame.sprite.Group()

        self.fundo = Obj('imagens/creditos/fundo.png', 0, 0, self.todas_sprites)
        self.voltar_botao = Obj('imagens/creditos/voltar.png', 368, 700, self.todas_sprites)
        self.exibindo = True

    def desenha(self, janela):
        self.todas_sprites.draw(janela)
