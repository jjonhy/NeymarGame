import pygame
import time
from fase import Fase
from vitoria import Vitoria


class Principal:
    def __init__(self, dimensoes_janela, titulo):
        pygame.display.set_caption(titulo)
        self.janela = pygame.display.set_mode(dimensoes_janela)
        self.imagem_menu = pygame.image.load('imagens/menu1.png')
        self.imagem1_menu = pygame.image.load('imagens/menu2.png')
        self.imagem_fundo_jogo = pygame.image.load('imagens/campo.png')
        self.musica = pygame.mixer.music.load('imagens/torcida.mp3')
        self.rodando = True
        self.fim_fase = Vitoria()

    def menu_inicial(self):
        i = 0

        exibir = True
        while exibir:
            if i % 2 == 0:
                self.janela.blit(self.imagem_menu, (0, 0))
            else:
                self.janela.blit(self.imagem1_menu, (0, 0))
            i += 1

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.rodando = False
                    exibir = False

                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN:
                        exibir = False

            pygame.display.update()
            time.sleep(0.5)

    def novo_jogo(self):
        for i in range(1, 4):
            f = Fase(i)
            pygame.mixer.init()
            pygame.mixer.music.play(-1)
            while self.rodando:
                pygame.time.delay(50)
                self.janela.blit(self.imagem_fundo_jogo, (0, 0))

                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        self.rodando = False

                f.acoes(pygame.key.get_pressed())
                f.desenha(self.janela)

                if f.mapa.matriz[int(f.neymar.y / 10)][int(f.neymar.x / 10)] == 2:
                    self.fim_fase.mostra_vitoria(self.janela , i)
                    break

                pygame.display.update()

        game.rodando = False


pygame.init()

game = Principal((1000, 800), "PROJETO FINAL POO")
game.menu_inicial()
game.novo_jogo()

pygame.quit()
