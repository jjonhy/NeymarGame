import pygame


class Neymar:
    def __init__(self, caminho_imagem, coordenadas_iniciais, velocidade):
        self.imagem = pygame.image.load(caminho_imagem)
        self.x = coordenadas_iniciais[0]
        self.y = coordenadas_iniciais[1]
        self.velocidade = velocidade

    def movimenta(self, comandos, mapa):
        if comandos[pygame.K_UP]:
            flag = False
            for i in range(int(self.x / 10), int(self.x / 10 + 7)):
                if mapa.matriz[int((self.y - 10) / 10)][i] == 1:
                    flag = True
                    break

            if not flag:
                self.y -= self.velocidade

        if comandos[pygame.K_DOWN]:
            flag = False
            for i in range(int(self.x / 10), int(self.x / 10 + 7)):
                if mapa.matriz[int((self.y + 100) / 10)][i] == 1:
                    flag = True
                    break

            if not flag:
                self.y += self.velocidade

        if comandos[pygame.K_RIGHT]:
            flag = False
            for i in range(int(self.y / 10), int(self.y / 10 + 10)):
                if mapa.matriz[i][int((self.x + 70) / 10)] == 1:
                    flag = True
                    break

            if not flag:
                self.x += self.velocidade

        if comandos[pygame.K_LEFT]:
            flag = False
            for i in range(int(self.y / 10), int(self.y / 10 + 10)):
                if mapa.matriz[i][int((self.x - 10) / 10)] == 1:
                    flag = True
                    break

            if not flag:
                self.x -= self.velocidade
