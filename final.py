import pygame


class Final:
    def __init__(self):
        self.fundo = pygame.image.load('imagens/final/fundo.png')
        self.exibindo = True

    def fadeout(self, janela):
        for i in range(0, 255, 10):
            self.fundo.set_alpha(i)
            janela.blit(self.fundo, (0, 0))
            pygame.display.flip()
            pygame.time.delay(50)

    def executa_cena(self, janela):
        font = pygame.font.SysFont('Arial', 120, bold=True)

        self.fadeout(janela)
        texto = font.render('VAMOS', True, "WHITE")
        janela.blit(texto, (268, 100))
        pygame.display.flip()
        pygame.time.delay(400)
        texto = font.render('BRASIL', True, "WHITE")
        janela.blit(texto, (268, 500))
        pygame.display.flip()
        pygame.time.delay(1000)
        self.fadeout(janela)
        font = pygame.font.SysFont('Arial', 48, bold=True)
        texto = font.render('Apesar de tudo e todos!', True, "WHITE")
        janela.blit(texto, (200, 100))
        pygame.display.flip()
        pygame.time.delay(400)
        texto = font.render('E os flagelos da nação', True, "WHITE")
        janela.blit(texto, (220, 350))
        pygame.display.flip()
        pygame.time.delay(400)
        texto = font.render('Entregamos nossos Corações!!!', True, "WHITE")
        janela.blit(texto, (130, 600))
        pygame.display.flip()
        pygame.time.delay(3000)
        self.fadeout(janela)
