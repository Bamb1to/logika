from pygame import *
import random 
import math

init()
font.init()
mixer.init()
mixer.music.load('f1.mp3')
mixer.music.set_volume(0.1)
# mixer.music.play(loops=-1)

fire_sound = mixer.Sound('signal car.mp3')
fire_sound.set_volume(0.5)

FONT = 'Play-Regular.ttf'

FPS = 60

scr_info = display.Info()
WIDTH, HEIGHT = 900,  900

#створи вікно гри
window = display.set_mode((WIDTH,HEIGHT))
display.set_caption("Gonki 2D")
clock = time.Clock()
#задай фон сцени
bg = image.load("map for gonki.png")
map = image.load("map.png")
bg = transform.scale(bg, (WIDTH,HEIGHT))

player_img = image.load("red bull car.png")
enemy_img = image.load("orange car.png")

all_sprites = sprite.Group()

all_labels = sprite.Group()

class Label(sprite.Sprite):
    def __init__(self, text, x, y, fontsize=30, color=(225, 228, 232) , font_name=FONT):
        super().__init__()
        self.color = color
        self.font = font.Font(FONT, fontsize)
        self.image = self.font.render(text, True, color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y  = y
        all_labels.add(self)
    
    def set_text(self, new_text, color=(225, 228, 232)):
        self.image = self.font.render(new_text, True, color) 


class BaseSprite(sprite.Sprite):
    def __init__(self, image, x, y, width, height):
        super().__init__()
        self.image = transform.scale(image, (width, height))
        self.rect = Rect(x,y,width, height)
        self.mask = mask.from_surface(self.image)
        all_sprites.add(self)
                
    def draw(self, window):
        window.blit(self.image, self.rect)

class Player(BaseSprite):
    def __init__(self, image, x, y, width, height):
        super().__init__(image, x, y, width, height)
        self.right_image = self.image
        self.left_image = transform.flip(self.image, True, False)
        self.speed = 0
        self.hp = 100
        self.coins_counter= 0
        self.damage_timer = time.get_ticks() #фіксуємо чая від початку гри в мілісекундах
        self.angle = 0
    
    def update(self):
        old_pos = self.rect.x, self.rect.y
        keys = key.get_pressed()
        if keys[K_a]:
            self.angle += 3
        if keys[K_d]:
            self.angle -= 3
        if keys[K_w]:
            self.speed = min(self.speed -0.2, 10)
        elif keys[K_s]:
            self.speed = max(self.speed +0.2, -10)
        else:
            if self.speed > 0:
                self.speed -= 0.1
            else:
                self.speed += 0.1    

        rad = math.radians(self.angle)
        dx = -self.speed * math.sin(rad)
        dy = -self.speed * math.cos(rad)
        self.rect.x += dx
        self.rect.y += dy

        self.image = transform.rotate(self.right_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

class Enemy(BaseSprite):  
    def __init__(self, image, x, y, width, height):
        super().__init__(image, x, y, width, height)  
        self.original_image = self.image
        
        self.speed = 3 
        self.dir_list = ['left', 'right', 'up', 'down']
        self.dir = random.choice(self.dir_list)

    def update(self):
        old_pos = self.rect.x, self.rect.y     

map = BaseSprite(map, 0, 0, WIDTH, HEIGHT)      
        
enemy1 = Enemy(enemy_img,132, 10, 30, 60)

player = Player(player_img, 87, 165, 30, 60) 

run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                run = False

    window.blit(bg, (0,0))
    player.update()
    all_sprites.draw(window)
    all_labels.draw(window)
  
        
    display.update()
    clock.tick(FPS)