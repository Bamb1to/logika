from pygame import *
import random 

init()
font.init()
mixer.init()
mixer.music.load('space.ogg')
mixer.music.set_volume(0.1)
# mixer.music.play(loops=-1)

fire_sound = mixer.Sound('laser5.wav')
fire_sound.set_volume(0.5)

FONT = 'Play-Regular.ttf'

FPS = 60

scr_info = display.Info()
WIDTH, HEIGHT = scr_info.current_w,  scr_info.current_h

#створи вікно гри
window = display.set_mode((WIDTH,HEIGHT), flags=FULLSCREEN)
display.set_caption("Space Shooter")
clock = time.Clock()
#задай фон сцени
bg = image.load("background.jpg")
bg = transform.scale(bg, (WIDTH,HEIGHT))

player_img = image.load("spaceship.png")
enemy_img = image.load("alien.png")

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
        self.speed = 5
        self.hp = 100
        self.coins_counter= 0
        self.damage_timer = time.get_ticks() #фіксуємо чая від початку гри в мілісекундах

    
    def update(self):
        old_pos = self.rect.x, self.rect.y
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
            self.image = self.left_image
        if keys[K_d]:
            self.rect.x += self.speed
            self.image = self.right_image
        if keys[K_w]:
            self.rect.y -= self.speed
        if keys[K_s]:
            self.rect.y += self.speed
        
        


run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                run = False

    window.blit(bg, (0,0))
    all_sprites.draw(window)
    all_labels.draw(window)
  
        
    display.update()
    clock.tick(FPS)