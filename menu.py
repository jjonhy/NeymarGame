import pygame
from obj import Obj


class Menu:
    def __init__(self):
        self.todas_sprites = pygame.sprite.Group()
        self.fundo = Obj('imagens/menu/fundo.png', 0, 0, self.todas_sprites)
        self.retomar_botao = Obj('imagens/menu/retomar.png', 368, 400, self.todas_sprites)
        self.reiniciar_botao = Obj('imagens/menu/reiniciar.png', 368, 483, self.todas_sprites)
        self.inicio_botao = Obj('imagens/menu/inicio.png', 368, 566, self.todas_sprites)
        self.exibindo = True

    def desenha(self, janela):
        self.todas_sprites.draw(janela)

    def verifica_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return 4

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    return 7

            if evento.type == pygame.MOUSEBUTTONUP:
                if self.retomar_botao.rect.collidepoint(pygame.mouse.get_pos()):
                    return 7

                elif self.reiniciar_botao.rect.collidepoint(pygame.mouse.get_pos()):
                    return 8

                elif self.inicio_botao.rect.collidepoint(pygame.mouse.get_pos()):
                    return 6

        return 0

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
