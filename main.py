import pygame


if __name__ == "__main__":
    pygame.init()

    x = 400 #inicial neymar
    y = 300 #inicial neymar
    velocidade = 15
    fundo = pygame.image.load('campo.png')
    neymar = pygame.image.load('Bonecos-de-acão-mini-Brasil-futebol-Boneco-Brasil---Neymar-l.png')

    janela = pygame.display.set_mode((800, 600))  # tamanho janela
    pygame.display.set_caption("Projeto final POO")

    janela_aberta = True
    while janela_aberta:
        pygame.time.delay(50)  # a cada 50 milisegundo executa abaixo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                janela_aberta = False

        comandos = pygame.key.get_pressed()
        if comandos[pygame.K_UP]:
            y -= velocidade
        if comandos[pygame.K_DOWN]:
            y += velocidade
        if comandos[pygame.K_RIGHT]:
            x += velocidade
        if comandos[pygame.K_LEFT]:
            x -= velocidade

        if y <= 0:
            y = 600
        if y > 600:
            y = 0
        if x <= 0:
            x = 800
        if x > 800:
            x = 0

        janela.blit( fundo, (0,0))
        # janela.fill((0, 0, 0))
        janela.blit(neymar, (x, y))
        pygame.display.update()

    pygame.quit()

