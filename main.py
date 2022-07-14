import pygame
from mapa import Mapa


class Neymar:
    def __init__(self, velocidade, start_pos):
        self.velocidade = velocidade
        self.x_inicial = start_pos[0]
        self.y_inicial = start_pos[1]
        self.ney_img = pygame.image.load(
            'Bonecos-de-acão-mini-Brasil-futebol-Boneco-Brasil---Neymar-l.png')


class Fundo:
    def __init__(self):
        self.img = pygame.image.load('campo.png')


if __name__ == "__main__":
    pygame.init()
    mapa = Mapa(1)

    for fase in range(1, 4):
        janela = pygame.display.set_mode((1000, 800))  # tamanho janela
        pygame.display.set_caption("Projeto final POO")  # titulo da janela
        fundo = Fundo()
        mapa.att_matriz()
        # neymar = {}
        print(mapa.start_position)
        neymar = Neymar(10, mapa.start_position)
        """ if(fase == 1): neymar = Neymar(10, 0, 10)
            if(fase == 2): neymar = Neymar(10, 0, 350)
            if(fase == 3): neymar = Neymar(10, 470, 360) """

        font = pygame.font.SysFont('Arial', 12, bold=True)
        # Transforma o texto em uma imagem para ser mostrada na tela
        img = font.render('#', True, "WHITE")

        janela_aberta = True
        while janela_aberta:
            pygame.time.delay(50)  # a cada 50 milisegundo executa abaixo
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            comandos = pygame.key.get_pressed()

            # Quando uma tecla é pressionada, primeiro verifica(na matriz) se possui alguma parede impedindo o movimento, se não altera a posicao
            if comandos[pygame.K_UP]:
                flag = False
                for i in range(int(neymar.x_inicial/10), int(neymar.x_inicial/10 + 7)):
                    if(mapa.matriz[int((neymar.y_inicial-10)/10)][i] == 1):
                        flag = True
                        break
                if(flag == False):
                    neymar.y_inicial -= neymar.velocidade

            if comandos[pygame.K_DOWN]:
                flag = False
                for i in range(int(neymar.x_inicial/10), int(neymar.x_inicial/10 + 7)):
                    if(mapa.matriz[int((neymar.y_inicial+100)/10)][i] == 1):
                        flag = True
                        break
                if(flag == False):
                    neymar.y_inicial += neymar.velocidade

            if comandos[pygame.K_RIGHT]:
                flag = False
                for i in range(int(neymar.y_inicial/10), int(neymar.y_inicial/10 + 10)):
                    if(mapa.matriz[i][int((neymar.x_inicial + 70)/10)] == 1):
                        flag = True
                        break
                if(flag == False):
                    neymar.x_inicial += neymar.velocidade

            if comandos[pygame.K_LEFT]:
                flag = False
                for i in range(int(neymar.y_inicial/10), int(neymar.y_inicial/10 + 10)):
                    if(mapa.matriz[i][int((neymar.x_inicial - 10)/10)] == 1):
                        flag = True
                        break
                if(flag == False):
                    neymar.x_inicial -= neymar.velocidade

            janela.blit(fundo.img, (0, 0))
            # janela.fill((0, 0, 0))
            janela.blit(neymar.ney_img, (neymar.x_inicial, neymar.y_inicial))

            # Cada for renderiza as paredes em torno do neymar em uma direção
            for i in range(int((neymar.x_inicial - 30)/10), int((neymar.x_inicial + 100)/10)):
                if(mapa.matriz[int((neymar.y_inicial - 10)/10)][i] == 1):
                    janela.blit(img, (i*10, neymar.y_inicial - 10))

            for i in range(int((neymar.x_inicial - 30)/10), int((neymar.x_inicial + 100)/10)):
                if(mapa.matriz[int((neymar.y_inicial + 100)/10)][i] == 1):
                    janela.blit(img, (i*10, neymar.y_inicial + 100))

            for i in range(int((neymar.y_inicial - 30)/10), int((neymar.y_inicial + 130)/10)):
                if(mapa.matriz[i][int((neymar.x_inicial - 10)/10)] == 1):
                    janela.blit(img, (neymar.x_inicial-10, i*10))

            for i in range(int((neymar.y_inicial - 30)/10), int((neymar.y_inicial + 130)/10)):
                if(mapa.matriz[i][int((neymar.x_inicial + 70)/10)] == 1):
                    janela.blit(img, (neymar.x_inicial+70, i*10))

            #print(int(neymar.y_inicial/10))
            #print(int(neymar.x_inicial/10))
            #print(mapa.matriz[int(neymar.y_inicial/10)][int(neymar.x_inicial/10)])

            # Verificando se o jogador chegou no objetivo
            if(mapa.matriz[int(neymar.y_inicial/10)][int(neymar.x_inicial/10)] == 2):
                mapa.fase += 1
                print("passou aqui")
                break

            pygame.display.update()

    pygame.quit()
