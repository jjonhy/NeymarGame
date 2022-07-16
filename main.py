import pygame
from mapa import Mapa

class Animation:
    def __init__(self) -> None:
        self.vecwin = []
        self.vecwin.append(pygame.image.load('win_liberta.jpg'))
        self.vecwin.append(pygame.image.load('win_uefa.jpg'))
        self.vecwin.append(pygame.image.load('rumo_hexa.jpg'))

        self.win_track = []
        self.win_track.append((190,165))
        self.win_track.append((189,225))
        self.win_track.append((298,242))
    
        

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
    fundo = Fundo()
    win_scene = Animation()
    for fase in range(1, 4):
        banana = False
        janela = pygame.display.set_mode((1000, 800))  # tamanho janela
        pygame.display.set_caption("Projeto final POO")  # titulo da janela
        
        mapa.att_matriz()
        neymar = Neymar(10, mapa.start_position)

        font = pygame.font.SysFont('Arial', 12, bold=True)
        # Transforma o texto em uma imagem para ser mostrada na tela
        img = font.render('#', True, "WHITE")

        while True:
            pygame.time.delay(50)
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
            #janela.blit(win_scene.vecwin[fase], (0,0))
            
             

            #Cada for renderiza as paredes em torno do neymar em uma direção
            for i in range(int((neymar.x_inicial - 30)/10) , int((neymar.x_inicial + 100)/10)):
                #Renderiza as paredes em volta do personagem
                if(mapa.matriz[int((neymar.y_inicial - 10)/10)][i] == 1): janela.blit(img, (i*10 , neymar.y_inicial - 10))
                if(mapa.matriz[int((neymar.y_inicial - 20)/10)][i] == 1): janela.blit(img, (i*10 , neymar.y_inicial - 20))

            for i in range(int((neymar.x_inicial - 30)/10), int((neymar.x_inicial + 100)/10)):
                #Renderiza as paredes em volta do personagem
                if(mapa.matriz[int((neymar.y_inicial + 100)/10)][i] == 1): janela.blit(img, (i*10, neymar.y_inicial + 100))
                if(mapa.matriz[int((neymar.y_inicial + 110)/10)][i] == 1): janela.blit(img, (i*10, neymar.y_inicial + 110))
                # Renderiza o trófeu quando estiver próximo
                for j in range(int((neymar.y_inicial - 30)/10), int((neymar.y_inicial + 130)/10)):
                    if(mapa.matriz[j][i] == 2): janela.blit(mapa.objetivo, (i*10, j*10))

            for i in range(int((neymar.y_inicial - 30)/10), int((neymar.y_inicial + 130)/10)):
                if(mapa.matriz[i][int((neymar.x_inicial - 10)/10)] == 1): janela.blit(img, (neymar.x_inicial-10 , i*10))
                if(mapa.matriz[i][int((neymar.x_inicial - 20)/10)] == 1): janela.blit(img, (neymar.x_inicial-20 , i*10))
                # Renderiza o trófeu quando estiver próximo
                for j in range(int((neymar.x_inicial - 20)/10), int((neymar.x_inicial + 80)/10)):
                    if(mapa.matriz[i][j] == 2): janela.blit(mapa.objetivo, (j*10, i*10))

            for i in range(int((neymar.y_inicial - 30)/10), int((neymar.y_inicial + 130)/10)):
                if(mapa.matriz[i][int((neymar.x_inicial + 70)/10)] == 1): janela.blit(img, (neymar.x_inicial+70 , i*10))
                if(mapa.matriz[i][int((neymar.x_inicial + 80)/10)] == 1): janela.blit(img, (neymar.x_inicial+80 , i*10))
                # Renderiza o trófeu quando estiver próximo
                for j in range(int((neymar.x_inicial - 20)/10), int((neymar.x_inicial + 80)/10)):
                    if(mapa.matriz[i][j] == 2): 
                        janela.blit(mapa.objetivo, (j*10, i*10)) 
                        #janela.blit(win_scene.vecwin[fase-1], (0,0))

            
            #janela.blit(win_scene.vecwin[fase-1], (0,0))
            #janela.blit(win_scene.vecwin[fase-1], (0,0))
            # Verificando se o jogador chegou no objetivo
            if(mapa.matriz[int(neymar.y_inicial/10)][int(neymar.x_inicial/10)] == 2):
                print("passou aqui")
                banana = True
                janela.blit(win_scene.vecwin[fase-1], win_scene.win_track[fase-1])
                pygame.display.update()
                pygame.time.delay(1000)
                mapa.fase += 1
                break
                
            
            pygame.display.update()

    pygame.quit()
