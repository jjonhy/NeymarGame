import pygame


class Obj(pygame.sprite.Sprite):
    def __init__(self, caminho_imagem, x, y, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load(caminho_imagem)
        self.rect = self.image.get_rect()
        self.rect[0] = x
        self.rect[1] = y

    def desenha(self, janela):
        self.group.draw(janela)
