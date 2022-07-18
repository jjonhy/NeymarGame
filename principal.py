import pygame
from fase import Fase
from vitoria import Vitoria
from menu import Menu
from creditos import Creditos


class Principal:
    def __init__(self, dimensoes_janela, titulo):
        pygame.display.set_caption(titulo)
        self.janela = pygame.display.set_mode(dimensoes_janela)
        self.menu = Menu()
        self.creditos = Creditos()
        self.imagem_fundo_jogo = pygame.image.load('imagens/campo.png')
        # self.musica = pygame.mixer.music.load('imagens/torcida.mp3')
        # pygame.mixer.init()
        # pygame.mixer.music.play(-1)
        self.rodando = True
        self.fim_fase = Vitoria()

    def menu_inicial(self):
        self.menu.exibindo = True
        while self.menu.exibindo:
            self.menu.desenha(self.janela)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.menu.exibindo = False
                    self.rodando = False
                    return 3

                if evento.type == pygame.MOUSEBUTTONUP:
                    if self.menu.jogar_botao.rect.collidepoint(pygame.mouse.get_pos()):
                        self.menu.exibindo = False
                        return 1

                    elif self.menu.creditos_botao.rect.collidepoint(pygame.mouse.get_pos()):
                        self.menu.exibindo = False
                        return 2

                    elif self.menu.sair_botao.rect.collidepoint(pygame.mouse.get_pos()):
                        self.menu.exibindo = False
                        self.rodando = False
                        return 3

            pygame.display.update()

    def cena_creditos(self):
        while self.creditos.exibindo:
            self.creditos.desenha(self.janela)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.creditos.exibindo = False
                    self.rodando = False

                if evento.type == pygame.MOUSEBUTTONUP:
                    if self.creditos.voltar_botao.rect.collidepoint(pygame.mouse.get_pos()):
                        self.creditos.exibindo = False

            pygame.display.update()

    def novo_jogo(self):
        for i in range(1, 4):
            f = Fase(i)
            while self.rodando:
                pygame.time.delay(50)
                self.janela.blit(self.imagem_fundo_jogo, (0, 0))

                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        pygame.quit()

                f.acoes(pygame.key.get_pressed())
                f.desenha(self.janela)

                if f.mapa.matriz[int(f.neymar.y / 10)][int(f.neymar.x / 10)] == 2:
                    self.fim_fase.mostra_vitoria(self.janela, i)
                    break

                pygame.display.update()
        self.final()
        self.rodando = True

    def final(self):
        font = pygame.font.SysFont('Arial', 120, bold=True)

        self.fadeout()
        texto = font.render('VAMOS', True, "WHITE")
        self.janela.blit(texto, (268, 100))
        pygame.display.flip()
        pygame.time.delay(400)
        texto = font.render('BRASIL', True, "WHITE")
        self.janela.blit(texto, (268, 500))
        pygame.display.flip()
        pygame.time.delay(1000)
        self.fadeout()
        font = pygame.font.SysFont('Arial', 48, bold=True)
        texto = font.render('Apesar de tudo e todos!', True, "WHITE")
        self.janela.blit(texto, (200, 100))
        pygame.display.flip()
        pygame.time.delay(400)
        texto = font.render('E os flagelos da nação', True, "WHITE")
        self.janela.blit(texto, (220, 350))
        pygame.display.flip()
        pygame.time.delay(400)
        texto = font.render('Entregamos nossos Corações!!!', True, "WHITE")
        self.janela.blit(texto, (130, 600))
        pygame.display.flip()
        pygame.time.delay(3000)
        self.fadeout()
        self.cena_creditos()
    

    def fadeout(self):
        for i in range(0,255,10):
            self.imagem_fundo_jogo.set_alpha(i)
            self.janela.blit(self.imagem_fundo_jogo, (0,0))
            pygame.display.flip()
            pygame.time.delay(50)

pygame.init()

game = Principal((1000, 800), "PROJETO FINAL POO")
while game.rodando:
    opcao_menu = game.menu_inicial()

    if opcao_menu == 1:
        print(game.rodando)
        game.novo_jogo()
        print(game.rodando)

    elif opcao_menu == 2:
        game.creditos.exibindo = True
        game.cena_creditos()
        game.menu.exibindo = True

    else:
        game.rodando = False

pygame.quit()
