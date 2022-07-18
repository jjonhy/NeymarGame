import pygame
from obj import Obj


class MenuInicial:
    def __init__(self):
        self.todas_sprites = pygame.sprite.Group()
        self.fundo = Obj('imagens/menu_inicial/fundo.png', 0, 0, self.todas_sprites)
        self.jogar_botao = Obj('imagens/menu_inicial/jogar.png', 368, 400, self.todas_sprites)
        self.ajuda_botao = Obj('imagens/menu_inicial/ajuda.png', 368, 483, self.todas_sprites)
        self.creditos_botao = Obj('imagens/menu_inicial/creditos.png', 368, 566, self.todas_sprites)
        self.sair_botao = Obj('imagens/menu_inicial/sair.png', 368, 649, self.todas_sprites)
        self.exibindo = True

    def desenha(self, janela):
        self.todas_sprites.draw(janela)

    def verifica_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return 4

            if evento.type == pygame.MOUSEBUTTONUP:
                if self.jogar_botao.rect.collidepoint(pygame.mouse.get_pos()):
                    return 1

                elif self.ajuda_botao.rect.collidepoint(pygame.mouse.get_pos()):
                    return 2

                elif self.creditos_botao.rect.collidepoint(pygame.mouse.get_pos()):
                    return 3

                elif self.sair_botao.rect.collidepoint(pygame.mouse.get_pos()):
                    return 4

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
