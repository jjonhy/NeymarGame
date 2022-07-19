import pygame
from obj import Obj
from cena import Cena


class Menu(Cena):
    def __init__(self):
        super().__init__()
        self.retomar_botao = Obj('imagens/menu/retomar.png', 368, 400, self.todas_sprites)
        self.reiniciar_botao = Obj('imagens/menu/reiniciar.png', 368, 483, self.todas_sprites)
        self.inicio_botao = Obj('imagens/menu/inicio.png', 368, 566, self.todas_sprites)

    def verifica_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return 4

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    return 7

            if evento.type == pygame.MOUSEMOTION:
                if self.retomar_botao.rect.collidepoint(pygame.mouse.get_pos()):
                    self.retomar_botao.image = pygame.image.load('imagens/menu/retomar2.png')

                elif self.reiniciar_botao.rect.collidepoint(pygame.mouse.get_pos()):
                    self.reiniciar_botao.image = pygame.image.load('imagens/menu/reiniciar2.png')

                elif self.inicio_botao.rect.collidepoint(pygame.mouse.get_pos()):
                    self.inicio_botao.image = pygame.image.load('imagens/menu/inicio2.png')

                else:
                    self.retomar_botao.image = pygame.image.load('imagens/menu/retomar.png')
                    self.reiniciar_botao.image = pygame.image.load('imagens/menu/reiniciar.png')
                    self.inicio_botao.image = pygame.image.load('imagens/menu/inicio.png')

            if evento.type == pygame.MOUSEBUTTONUP:
                if self.retomar_botao.rect.collidepoint(pygame.mouse.get_pos()):
                    return 7

                elif self.reiniciar_botao.rect.collidepoint(pygame.mouse.get_pos()):
                    return 8

                elif self.inicio_botao.rect.collidepoint(pygame.mouse.get_pos()):
                    return 6

        return 0
