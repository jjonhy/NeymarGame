import pygame
from obj import Obj
from cena import Cena


class MenuInicial(Cena):
    def __init__(self):
        super().__init__()
        self.titulo = Obj('imagens/creditos/titulo.png', 211, 150, self.todas_sprites)
        self.jogar_botao = Obj('imagens/menu_inicial/jogar.png', 368, 400, self.todas_sprites)
        self.ajuda_botao = Obj('imagens/menu_inicial/ajuda.png', 368, 483, self.todas_sprites)
        self.creditos_botao = Obj('imagens/menu_inicial/creditos.png', 368, 566, self.todas_sprites)
        self.sair_botao = Obj('imagens/menu_inicial/sair.png', 368, 649, self.todas_sprites)

    def verifica_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return 4

            if evento.type == pygame.MOUSEMOTION:
                if self.jogar_botao.rect.collidepoint(pygame.mouse.get_pos()):
                    self.jogar_botao.image = pygame.image.load('imagens/menu_inicial/jogar2.png')

                elif self.ajuda_botao.rect.collidepoint(pygame.mouse.get_pos()):
                    self.ajuda_botao.image = pygame.image.load('imagens/menu_inicial/ajuda2.png')

                elif self.creditos_botao.rect.collidepoint(pygame.mouse.get_pos()):
                    self.creditos_botao.image = pygame.image.load('imagens/menu_inicial/creditos2.png')

                elif self.sair_botao.rect.collidepoint(pygame.mouse.get_pos()):
                    self.sair_botao.image = pygame.image.load('imagens/menu_inicial/sair2.png')

                else:
                    self.jogar_botao.image = pygame.image.load('imagens/menu_inicial/jogar.png')
                    self.ajuda_botao.image = pygame.image.load('imagens/menu_inicial/ajuda.png')
                    self.creditos_botao.image = pygame.image.load('imagens/menu_inicial/creditos.png')
                    self.sair_botao.image = pygame.image.load('imagens/menu_inicial/sair.png')

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
