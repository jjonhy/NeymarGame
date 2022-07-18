import pygame


class Transicao:
    def __init__(self):
        self.vecwin = []
        self.vecwin.append(pygame.image.load('imagens/transicao/win_liberta.jpg'))
        self.vecwin.append(pygame.image.load('imagens/transicao/win_uefa.jpg'))
        self.vecwin.append(pygame.image.load('imagens/transicao/rumo_hexa.jpg'))

        self.win_track = []
        self.win_track.append((190, 165))
        self.win_track.append((189, 225))
        self.win_track.append((298, 242))

        self.confetti = pygame.image.load('imagens/transicao/confetti.png')
        self.confetti = pygame.transform.scale(self.confetti, (1000, 800))

    def executa_transicao(self, janela, fase):
        janela.blit(self.confetti, (0, 0))
        janela.blit(self.vecwin[fase - 1], self.win_track[fase - 1])
        pygame.display.update()
        pygame.time.delay(2000)
