import pygame
from fase import Fase
from menu import Menu
from creditos import Creditos


class Principal:
    def __init__(self, dimensoes_janela, titulo):
        pygame.display.set_caption(titulo)
        self.janela = pygame.display.set_mode(dimensoes_janela)
        self.menu = Menu()
        self.creditos = Creditos()
        self.imagem_fundo_jogo = pygame.image.load('imagens/campo.png')
        self.rodando = True

    def menu_inicial(self):
        while self.menu.exibindo:
            self.menu.desenha(self.janela)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.menu.exibindo = False
                    self.rodando = False
                    return 3

                if evento.type == pygame.MOUSEBUTTONUP:
                    if self.menu.jogar_botao.rect.collidepoint(pygame.mouse.get_pos()):
                        self.menu.exibindo = False
                        return 1

                    elif self.menu.creditos_botao.rect.collidepoint(pygame.mouse.get_pos()):
                        self.menu.exibindo = False
                        return 2

                    elif self.menu.sair_botao.rect.collidepoint(pygame.mouse.get_pos()):
                        self.menu.exibindo = False
                        self.rodando = False
                        return 3

            pygame.display.update()

    def cena_creditos(self):
        while self.creditos.exibindo:
            self.creditos.desenha(self.janela)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.creditos.exibindo = False
                    self.rodando = False

                if evento.type == pygame.MOUSEBUTTONUP:
                    if self.creditos.voltar_botao.rect.collidepoint(pygame.mouse.get_pos()):
                        self.creditos.exibindo = False

            pygame.display.update()

    def novo_jogo(self):
        for i in range(1, 4):
            f = Fase(i)

            while self.rodando:
                pygame.time.delay(50)
                self.janela.blit(self.imagem_fundo_jogo, (0, 0))

                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        self.rodando = False

                f.acoes(pygame.key.get_pressed())
                f.desenha(self.janela)

                if f.mapa.matriz[int(f.neymar.y / 10)][int(f.neymar.x / 10)] == 2:
                    break

                pygame.display.update()

        game.rodando = False


pygame.init()

game = Principal((1000, 800), "PROJETO FINAL POO")
while game.rodando:
    opcao_menu = game.menu_inicial()

    if opcao_menu == 1:
        game.novo_jogo()

    elif opcao_menu == 2:
        game.creditos.exibindo = True
        game.cena_creditos()
        game.menu.exibindo = True

    else:
        game.rodando = False

pygame.quit()
