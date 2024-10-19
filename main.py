import pygame 
pygame.init()

window = pygame.display.set_mode((500,500))
background = pygame.image.load("photo.jpg")
background = pygame.transform.scale(background,(500,500))

class Wall:
    def __init__(self,x,y,width,height):
        self.rect = pygame.Rect(x,y,width, height) # створюємо прямокутник

    def draw(self, window):
        pygame.draw.rect(window, (0,0,0), self.rect)

class Player:
    def __init__(self,x,y,width,height,image):
        self.image = pygame.image.load(image) # завантажуємо зображення
        self.image = pygame.transform.scale(self.image,(width,height))
        self.rect = self.image.get_rect(topleft=(x,y))

        # параметри для гравітації
        self.gravity = 0.5 # швидкість падіння об'єкта
        self.jump_power = -12 # величина стрибка
        self.vertical = 0 # вертикальна швидкість
        self.can_jump = True # змінна для перевірки можливості стрибка


    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= 10
        if keys[pygame.K_d]:
            self.rect.x += 10

        # горизонтальна колізія
        for w in walls: # перебір всіх елементів в списку walls
            if self.rect.colliderect(w.rect):
                if self.rect.right > w.rect.left and self.rect.left < w.rect.left:
                    self.rect.right = w.rect.left
                elif self.rect.left < w.rect.right and self.rect.right > w.rect.right:
                    self.rect.left = w.rect.right

        self.vertical += self.gravity
        self.rect.y += self.vertical

        # вертикальна колізія
        for w in walls: # перебір всіх елементів в списку walls
            if self.rect.colliderect(w.rect):
                if self.vertical > 0:
                    self.rect.bottom = w.rect.top
                    self.vertical = 0
                    self.can_jump = True
                elif self.vertical < 0:
                    self.rect.top = w.rect.bottom
                    self.vertical = 0
    
    def jump(self):
        if self.can_jump:
            self.vertical = self.jump_power
            self.can_jump = False

walls = [
    Wall(100,350,100,20),
    Wall(250,350,100,20)
]      

            


player = Player(100,100,100,100,"bird.png") # removebg


game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN: ##########
            if event.key == pygame.K_w:  #########
                player.jump() ############
 
    window.blit(background, (0,0))
    for w in walls:   #######
        w.draw(window)  ######

    window.blit(player.image, player.rect)
    player.move()

    pygame.display.update()
    pygame.time.Clock().tick(60)
