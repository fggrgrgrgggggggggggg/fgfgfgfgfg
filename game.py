from pygame import * 
player_image = 'img/hero/m1.png'
win_width = 800 
win_height = 600
window = display.set_mode((win_width,win_height))
backg = 'img/back.png'
display.set_caption('Arcade')
background = transform.scale(image.load(backg),(win_width,win_height))
walkRight = [image.load('img/hero/right_1.png'),
image.load('img/hero/right_2.png'),
image.load('img/hero/right_3.png'),
image.load('img/hero/right_4.png'),
image.load('img/hero/right_5.png'),
image.load('img/hero/right_6.png'),
image.load('img/hero/right_7.png'),
image.load('img/hero/right_8.png'),
image.load('img/hero/right_9.png'),
image.load('img/hero/right_10.png'),
image.load('img/hero/right_11.png'),
image.load('img/hero/right_12.png')]
img_counter = 0
player_width = 80
walkLeft = [image.load('img/hero/left_1.png'),
image.load('img/hero/left_2.png'),
image.load('img/hero/left_3.png'),
image.load('img/hero/left_4.png'),
image.load('img/hero/left_5.png'),
image.load('img/hero/left_6.png'),
image.load('img/hero/left_7.png'),
image.load('img/hero/left_8.png'),
image.load('img/hero/left_9.png'),
image.load('img/hero/left_10.png'),
image.load('img/hero/left_11.png'),
image.load('img/hero/left_12.png')]

all_sprites = sprite.Group()
barriers = sprite.Group()

w = Wall(50, 150, 480, 20)
barriers.add(w)
all_sprites.add(w)
w = Wall(700, 0, 30, 400)
barriers.add(w)
all_sprites.add(w)

w = Wall(350, 380, 640, 20)
barriers.add(w)
all_sprites.add(w)
w = Wall(-200, 590, 1600, 20)
barriers.add(w)
all_sprites.add(w)



class Gamesprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, x_speed, y_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.x_speed = x_speed
        self.y_speed = y_speed

    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT]:
            self.x_speed = -5
        elif keys[K_RIGHT]:
            self.x_speed = 5
        elif keys[K_UP]:
            self.jump()
        else:
            self.x_speed = 0
        self.rect.x += self.x_speed
        self.gravitate()
        self.rect.y += self.y_speed

    def gravitate(self):
        self.y_speed += 0.25

    def jump(self):
        if self.stands_on:
            self.y_speed = -10
 
    def draw_hero(self):
        global img_counter
        if img_counter == 36:
            img_counter = 0
        if self.x_speed > 0:
            self.image = transform.scale(walkRight[img_counter//3], (player_width, 120))
        elif self.x_speed < 0: 
            self.image = transform.scale(walkLeft[img_counter//3], (player_width, 120))
            
        img_counter +=1 
        window.blit(self.image,(0,78))

class Wall(sprite.Sprite):
    def __init__(self, x, y, width, height, color=C_GREEN):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y 

robin = Gamesprite(player_image,50,50,80,120,12,12)
finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finished:
        all_sprites.update()
    window.blit(background,(0,0))
    robin.draw_hero()
    robin.update()
    display.update()
    time.delay(20)
