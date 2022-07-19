import pygame
from obj import Obj
from cena import Cena


class Ajuda(Cena):
    def __init__(self):
        super().__init__()
        self.titulo = Obj('imagens/ajuda/titulo.png', 211, 50, self.todas_sprites)
        self.conteudo = Obj('imagens/ajuda/conteudo_ajuda.png', 41.5, 175, self.todas_sprites)
        self.inicio_botao = Obj('imagens/ajuda/inicio.png', 368, 700, self.todas_sprites)

    def verifica_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return 4

            if evento.type == pygame.MOUSEMOTION:
                if self.inicio_botao.rect.collidepoint(pygame.mouse.get_pos()):
                    self.inicio_botao.image = pygame.image.load('imagens/ajuda/inicio2.png')

                else:
                    self.inicio_botao.image = pygame.image.load('imagens/ajuda/inicio.png')

            if evento.type == pygame.MOUSEBUTTONUP:
                if self.inicio_botao.rect.collidepoint(pygame.mouse.get_pos()):
                    return 6

        return 0
