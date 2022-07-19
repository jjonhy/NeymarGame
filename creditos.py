import pygame
from obj import Obj
from cena import Cena


class Creditos(Cena):
    def __init__(self):
        super().__init__()
        self.titulo = Obj('imagens/creditos/titulo.png', 224.5, 50, self.todas_sprites)
        self.descricao = Obj('imagens/creditos/descricao.png', 41.5, 150, self.todas_sprites)
        self.integrantes = Obj('imagens/creditos/integrantes.png', 326.5, 350, self.todas_sprites)
        self.inicio_botao = Obj('imagens/creditos/inicio.png', 368, 700, self.todas_sprites)

    def verifica_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return 4

            if evento.type == pygame.MOUSEMOTION:
                if self.inicio_botao.rect.collidepoint(pygame.mouse.get_pos()):
                    self.inicio_botao.image = pygame.image.load('imagens/creditos/inicio2.png')

                else:
                    self.inicio_botao.image = pygame.image.load('imagens/creditos/inicio.png')

            if evento.type == pygame.MOUSEBUTTONUP:
                if self.inicio_botao.rect.collidepoint(pygame.mouse.get_pos()):
                    return 6

        return 0
