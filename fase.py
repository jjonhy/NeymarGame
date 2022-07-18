import pygame
from mapa import Mapa
from neymar import Neymar


class Fase:
    def __init__(self, num_fase):
        self.mapa = Mapa(num_fase)
        self.neymar = Neymar('imagens/jogo/neymar.png', [0, 0], 10)
        if num_fase == 1:
            self.neymar.y = 10
        elif num_fase == 2:
            self.neymar.y = 350
        else:
            self.neymar.x = 470
            self.neymar.y = 360

    def acoes(self, comandos):
        self.neymar.movimenta(comandos, self.mapa)

    def desenha(self, janela):
        janela.blit(self.neymar.imagem, (self.neymar.x, self.neymar.y))

        neymar = self.neymar
        mapa = self.mapa

        font = pygame.font.SysFont('Arial', 12, bold=True)
        img = font.render('#', True, "WHITE")

        for i in range(int((neymar.x - 30) / 10), int((neymar.x + 100) / 10)):
            if mapa.matriz[int((neymar.y - 10) / 10)][i] == 1:
                janela.blit(img, (i * 10, neymar.y - 10))
            if mapa.matriz[int((neymar.y - 20) / 10)][i] == 1:
                janela.blit(img, (i * 10, neymar.y - 20))

        for i in range(int((neymar.x - 30) / 10), int((neymar.x + 100) / 10)):
            if mapa.matriz[int((neymar.y + 100) / 10)][i] == 1:
                janela.blit(img, (i * 10, neymar.y + 100))
            if mapa.matriz[int((neymar.y + 110) / 10)][i] == 1:
                janela.blit(img, (i * 10, neymar.y + 110))

            for j in range(int((neymar.y - 30) / 10), int((neymar.y + 130) / 10)):
                if mapa.matriz[j][i] == 2:
                    janela.blit(mapa.objetivo, (i * 10, j * 10))

        for i in range(int((neymar.y - 30) / 10), int((neymar.y + 130) / 10)):
            if mapa.matriz[i][int((neymar.x - 10) / 10)] == 1:
                janela.blit(img, (neymar.x - 10, i * 10))
            if mapa.matriz[i][int((neymar.x - 20) / 10)] == 1:
                janela.blit(img, (neymar.x - 20, i * 10))

            for j in range(int((neymar.x - 20) / 10), int((neymar.x + 80) / 10)):
                if mapa.matriz[i][j] == 2:
                    janela.blit(mapa.objetivo, (j * 10, i * 10))

        for i in range(int((neymar.y - 30) / 10), int((neymar.y + 130) / 10)):
            if mapa.matriz[i][int((neymar.x + 70) / 10)] == 1:
                janela.blit(img, (neymar.x + 70, i * 10))
            if mapa.matriz[i][int((neymar.x + 80) / 10)] == 1:
                janela.blit(img, (neymar.x + 80, i * 10))

            for j in range(int((neymar.x - 20) / 10), int((neymar.x + 80) / 10)):
                if mapa.matriz[i][j] == 2:
                    janela.blit(mapa.objetivo, (j * 10, i * 10))
