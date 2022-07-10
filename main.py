import pygame
from jogador import Jogador

if __name__ == "__main__":
    pygame.init()

    neymar = Jogador('neymar.png', 400, 300, 15)

    fundo = pygame.image.load('campo.png')

    janela = pygame.display.set_mode((800, 600))  # tamanho janela
    pygame.display.set_caption("Projeto final POO")

    janela_aberta = True
    while janela_aberta:
        pygame.time.delay(50)  # a cada 50 milisegundo executa abaixo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                janela_aberta = False

        neymar.movimenta(pygame.key.get_pressed())
        neymar.verifica_limites(800, 600)

        janela.blit(fundo, (0, 0))
        # janela.fill((0, 0, 0))
        janela.blit(neymar.imagem, (neymar.x, neymar.y))
        pygame.display.update()

    pygame.quit()
