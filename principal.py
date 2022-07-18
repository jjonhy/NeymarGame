import pygame
from menu_inicial import MenuInicial
from ajuda import Ajuda
from creditos import Creditos
from menu import Menu
from fase import Fase
from transicao import Transicao
from final import Final


class Principal:
    def __init__(self, dimensoes_janela, titulo):
        pygame.display.set_caption(titulo)
        self.janela = pygame.display.set_mode(dimensoes_janela)
        self.menu_inicial = MenuInicial()
        self.ajuda = Ajuda()
        self.creditos = Creditos()
        self.menu = Menu()
        self.imagem_fundo_jogo = pygame.image.load('imagens/jogo/campo.png')
        self.transicoes = Transicao()
        self.final = Final()
        self.rodando = True

    def desenha_jogo(self):
        self.janela.blit(self.imagem_fundo_jogo, (0, 0))

    def verifica_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return 4

            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                return self.menu.executa_cena(self.janela)

        return 0

    def novo_jogo(self):
        aux = 0

        i = 1
        while i < 4:
            f = Fase(i)

            while True:
                pygame.time.delay(50)
                self.desenha_jogo()

                aux = self.verifica_eventos()
                if aux == 4 or aux == 6 or aux == 8:
                    break

                f.acoes(pygame.key.get_pressed())
                f.desenha(self.janela)

                if f.mapa.matriz[int(f.neymar.y / 10)][int(f.neymar.x / 10)] == 2:
                    self.transicoes.executa_transicao(self.janela, i)
                    i += 1
                    break

                pygame.display.update()

            if aux == 4 or aux == 6 or aux == 8:
                break

        return aux


pygame.init()

game = Principal((1000, 800), "Neymar´s Tale")

opcao_menu_inicial = game.menu_inicial.executa_cena(game.janela)

while game.rodando:
    if opcao_menu_inicial == 1:
        opcao_jogo = game.novo_jogo()
        if opcao_jogo == 0:
            game.final.executa_cena(game.janela)
            opcao_menu_inicial = 3

        elif opcao_jogo == 4:
            game.rodando = False

        elif opcao_jogo == 6:
            opcao_menu_inicial = game.menu_inicial.executa_cena(game.janela)

        elif opcao_jogo == 8:
            opcao_menu_inicial = 1

    elif opcao_menu_inicial == 2:
        opcao_ajuda = game.ajuda.executa_cena(game.janela)
        if opcao_ajuda == 4:
            game.rodando = False

        elif opcao_ajuda == 6:
            opcao_menu_inicial = game.menu_inicial.executa_cena(game.janela)

    elif opcao_menu_inicial == 3:
        opcao_creditos = game.creditos.executa_cena(game.janela)
        if opcao_creditos == 4:
            game.rodando = False

        elif opcao_creditos == 6:
            opcao_menu_inicial = game.menu_inicial.executa_cena(game.janela)
    else:
        game.rodando = False

pygame.quit()
