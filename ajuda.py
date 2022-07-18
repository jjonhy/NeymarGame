import pygame
from obj import Obj


class Ajuda:
    def __init__(self):
        self.todas_sprites = pygame.sprite.Group()
        self.fundo = Obj('imagens/ajuda/fundo.png', 0, 0, self.todas_sprites)
        self.voltar_botao = Obj('imagens/ajuda/voltar.png', 368, 700, self.todas_sprites)
        self.exibindo = True

    def desenha(self, janela):
        self.todas_sprites.draw(janela)

    def verifica_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return 4

            if evento.type == pygame.MOUSEBUTTONUP:
                if self.voltar_botao.rect.collidepoint(pygame.mouse.get_pos()):
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
