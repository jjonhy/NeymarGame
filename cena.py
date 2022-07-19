import pygame
from obj import Obj


class Cena:
    def __init__(self):
        self.todas_sprites = self.todas_sprites = pygame.sprite.Group()
        self.fundo = Obj('imagens/ajuda/fundo.png', 0, 0, self.todas_sprites)
        self.exibindo = True

    def desenha(self, janela):
        self.todas_sprites.draw(janela)

    def verifica_eventos(self):
        pass

    def executa_cena(self, janela):
        aux = 0

        self.exibindo = True
        while self.exibindo:
            self.desenha(janela)

            aux = self.verifica_eventos()
            if aux != 0:
                self.exibindo = False

            pygame.display.update()

        return aux
