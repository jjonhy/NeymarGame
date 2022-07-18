import pygame
from obj import Obj


class Menu:
    def __init__(self):
        self.todas_sprites = pygame.sprite.Group()

        self.fundo = Obj('imagens/menu/fundo.png', 0, 0, self.todas_sprites)
        self.jogar_botao = Obj('imagens/menu/jogar.png', 368, 400, self.todas_sprites)
        self.creditos_botao = Obj('imagens/menu/creditos.png', 368, 483, self.todas_sprites)
        self.sair_botao = Obj('imagens/menu/sair.png', 368, 566, self.todas_sprites)

        self.exibindo = True

    def desenha(self, janela):
        self.todas_sprites.draw(janela)
