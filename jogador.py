import pygame


class Jogador:
    def __init__(self, caminho_imagem, x, y, velocidade):
        self.x = x
        self.y = y
        self.imagem = pygame.image.load(caminho_imagem)
        self.velocidade = velocidade

    def movimenta(self, comandos):
        if comandos[pygame.K_UP]:
            self.y -= self.velocidade
        if comandos[pygame.K_DOWN]:
            self.y += self.velocidade
        if comandos[pygame.K_RIGHT]:
            self.x += self.velocidade
        if comandos[pygame.K_LEFT]:
            self.x -= self.velocidade

    def verifica_limites(self, largura_janela, altura_janela):
        self.x = self.x % largura_janela
        self.y = self.y % altura_janela
