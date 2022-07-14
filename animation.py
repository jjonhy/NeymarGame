import pygame

class Puff(pygame.sprite.Sprite):

    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen

        try:
            self.imagePuff = pygame.image.load("campo.jpg").convert()
        except:
            raise (UserWarning, "Unable to find Puff image" )   
        self.image = self.imagePuff
        self.imagePuff.set_colorkey((0,0,255))           
        self.rect = self.image.get_rect()
        self.x = self.screen.get_width()/3
        self.y = self.screen.get_height()/3+10
        self.rect.center = (self.x, self.y)

        self.lifespan = 60
        self.speed = 1
        self.count = 0
        self.angle = 0


    def update(self):

        oldCenter = self.rect.center
        self.image = pygame.transform.rotate(self.imagePuff, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = oldCenter


    def calcPos(self):
        self.x -= 5
        self.y = self.y

    def turnLeft(self):
        self.angle = (self.angle + 45) % 360

    def turnRight(self):
        self.angle = (self.angle - 10) % 360



if __name__  == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((400,300))
    clock = pygame.time.Clock()
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    pygame.display.set_caption("Spinning sprite!!!")
    ball = Puff(screen)
    sprites = pygame.sprite.Group()
    sprites.add(ball)
    keepGoing = True
    while keepGoing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
        ball.turnRight()
        sprites.clear(screen, background)
        sprites.update()
        sprites.draw(screen)
        pygame.display.flip()   
        clock.tick(30)