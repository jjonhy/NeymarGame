import pygame


class Neymar:
    def __init__(self, velocidade, x_inicial, y_inicial):
        self.velocidade = velocidade
        self.x_inicial = x_inicial
        self.y_inicial = y_inicial
        self.ney_img = pygame.image.load('Bonecos-de-acão-mini-Brasil-futebol-Boneco-Brasil---Neymar-l.png')


class Fundo:
    def __init__(self):
        self.img = pygame.image.load('campo.png')


if __name__ == "__main__":
    pygame.init()

    neymar = Neymar(15, 400, 300)  # colocando o neymar no meio da tela
    fundo = Fundo()

    janela = pygame.display.set_mode((800, 600))  # tamanho janela

    pygame.display.set_caption("Projeto final POO")  # titulo da janela

    janela_aberta = True
    while janela_aberta:
        pygame.time.delay(50)  # a cada 50 milisegundo executa abaixo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                janela_aberta = False

        comandos = pygame.key.get_pressed()
        if comandos[pygame.K_UP]:
            neymar.y_inicial -= neymar.velocidade
        if comandos[pygame.K_DOWN]:
            neymar.y_inicial += neymar.velocidade
        if comandos[pygame.K_RIGHT]:
            neymar.x_inicial += neymar.velocidade
        if comandos[pygame.K_LEFT]:
            neymar.x_inicial -= neymar.velocidade

        if neymar.y_inicial <= 0:
            neymar.y_inicial = 600
        if neymar.y_inicial > 600:
            neymar.y_inicial = 0
        if neymar.x_inicial <= 0:
            neymar.x_inicial = 800
        if neymar.x_inicial > 800:
            neymar.x_inicial = 0

        janela.blit(fundo.img, (0, 0))
        # janela.fill((0, 0, 0))
        janela.blit(neymar.ney_img, (neymar.x_inicial, neymar.y_inicial))
        pygame.display.update()

    pygame.quit()
