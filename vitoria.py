
import pygame


class Vitoria:
    def __init__(self) -> None:
        self.vecwin = []
        self.vecwin.append(pygame.image.load('imagens/win_liberta.jpg'))
        self.vecwin.append(pygame.image.load('imagens/win_uefa.jpg'))
        self.vecwin.append(pygame.image.load('imagens/rumo_hexa.jpg'))

        self.win_track = []
        self.win_track.append((190,165))
        self.win_track.append((189,225))
        self.win_track.append((298,242))

        self.confetti = pygame.image.load('imagens/confetti.png')
        self.confetti = pygame.transform.scale(self.confetti, (1000, 800))
    

    def mostra_vitoria(self, janela, fase):
        janela.blit(self.confetti, (0,0))
        janela.blit(self.vecwin[fase-1], self.win_track[fase-1])
        pygame.display.update()
        pygame.time.delay(2000)



        

    