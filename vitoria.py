
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
    

    def mostra_vitoria(self, janela, fase):
        janela.blit(self.vecwin[fase-1], self.win_track[fase-1])
        pygame.display.update()
        pygame.time.delay(5000)


    def update(self):

        oldCenter = self.rect.center
        self.image = pygame.transform.rotate(self.imagePuff, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = oldCenter
        

    