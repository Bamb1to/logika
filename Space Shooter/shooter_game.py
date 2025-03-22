#Створи власний Шутер!

from pygame import *
import pygame_menu
import random

init()
font.init()
mixer.init()
mixer.music.load('space.ogg')
mixer.music.set_volume(0.1)
mixer.music.play(loops=-1)

fire_sound = mixer.Sound('laser5.wav')
fire_sound.set_volume(0.1)

FONT='DarumadropOne-Regular.ttf'

FPS = 60

scr_info = display.Info()
TILE_SIZE = 40
MAP_WIDTH, MAP_HEIGHT = 20, 15
WIDTH, HEIGHT = scr_info.current_w, scr_info.current_h

#створи вікно гри
window = display.set_mode((WIDTH, HEIGHT))
display.set_caption('Space Shooter')
clock = time.Clock()
#задай фон сцени
bg = image.load('background.jpg')
bg = transform.scale(bg, (WIDTH,HEIGHT))

player_img = image.load('spaceship.png')
enemy_img = image.load('alien.png')
fire_img = image.load('fire.png')

all_sprites = sprite.Group()
all_labels = sprite.Group()

class Label(sprite.Sprite):
    def __init__(self, text, x, y, fontsize=30, color=(0, 0, 225) , font_name=FONT):
        super().__init__()
        self.font = font.Font(FONT, fontsize)
        self.image = self.font.render(text, True, color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        all_labels.add(self)

    def set_text(self, new_text, color=(225, 0, 0)):   
        self.image = self.font.render(new_text, True, color) 

class BaseSprite(sprite.Sprite):
    def __init__(self, image, x, y, width, height):
        super().__init__()
        self.image = transform.scale(image, (width, height))
        self.rect = Rect(x, y, width, height)
        self.mask = mask.from_surface(self.image)
        all_sprites.add(self)

    def draw(self, window):
        window.blit(self.image, self.rect)

class Player(BaseSprite):  
    def __init__(self, image, x, y, width, height):
        super().__init__(image, x, y, width, height)  
        self.right_image = self.image
        self.left_image = transform.flip(self.image, True, False)
        self.speed_x = 10 
        self.speed_y = 4
        self.hp = 100
        self.score = 0
        self.coins_counter = 0 
        self.damage_timer = time.get_ticks()
        self.rect.centerx = x
        self.bullets = sprite.Group()
        self.fire_timer = time.get_ticks()

    def fire(self):    
        bullet = Bullet(self.rect, fire_img, 10, 30)
        self.bullets.add(bullet)
        fire_sound.play()

    def update(self):
        old_pos = self.rect.x, self.rect.y
        keys = key.get_pressed()

        if keys[K_SPACE]:
            now = time.get_ticks()
            if now-self.fire_timer > 500:
                self.fire()
                self.fire_timer = now
        if keys[K_a] and self.rect.left > 0:
            self.rect.x -= self.speed_x
            self.image = self.left_image
        if keys[K_d] and self.rect.right < WIDTH:
            self.rect.x += self.speed_x 
            self.image = self.right_image
        if keys[K_w] and self.rect.top > 0:
            if self.speed_y < 20:
                self.speed_y += 0.1
            # self.rect.y -= self.speed 
        if keys[K_s] and self.rect.bottom < HEIGHT and self.speed_y>1:
            self.speed_y -= 0.05
                #self.rect.y += self.speed 

        if not keys[K_w] and self.speed_y>2:
            self.speed_y -= 0.1 

        coll_list = sprite.spritecollide(self, enemy_group , False, sprite.collide_mask)
        if len(coll_list)>0:
            now = time.get_ticks()
            if now-self.damage_timer > 500:
                self.damage_timer = time.get_ticks() #обнуляємо таймер дамагу
                self.hp -= 10 #віднімаємо HP
                hp_label.set_text(f"HP: {self.hp}")    

class Enemy(BaseSprite):  
    def __init__(self, image, width, height):
        x = random.randint(0, WIDTH-width)
        y = random.randint(400, HEIGHT) * -1
        super().__init__(image, x, y, width, height)  
        self.speed_x = 10 
        self.speed_y = 2
        self.max_speed = 20
        self.hp = 100

    def update(self):
            self.rect.y += self.speed_y + player.speed_y
            if self.rect.y > HEIGHT:       
                self.kill()

class Bullet(BaseSprite):  
    def __init__(self, player_rect, image, width, height):
        super().__init__(image, player_rect.x, player_rect.y, width, height)  
        self.speed_y = 5
        self.rect.bottom = player_rect.top
        self.rect.centerx = player_rect.centerx


    def update(self):
        self.rect.y -= player.speed_y
        if self.rect.bottom < 0:
            self.kill()
        

player = Player(player_img, WIDTH/2, HEIGHT-200, 110, 100)
finish=False
run = True

bg1_y = 0 
bg2_y = -HEIGHT

spawn_timer = time.get_ticks()
enemy_group = sprite.Group()
max_spawn_time = 2000

result = Label("", 300, 300, fontsize=70)
restart = Label("Press R to restart", 300, 450, fontsize=40)
all_labels.remove(restart)
hp_label = Label(f"HP: {player.hp}", 10, 10)
score_label = Label(f'Score: {player.score}', 10, 40)

def set_difficulty(value, difficulty):
    pass

def start_the_game():
    menu.disable()

def restart_game(): 
    global finish
    if finish: 
        player.hp = 100 
        player.score = 0 
        hp_label.set_text(f"HP: (player.hp)") 
        score_label.set_text(f"Score: (player.score)") 
        finish = False 
        for enemy in enemy_group: 
            enemy.kill() 
        player.rect.x = WIDTH/2 
        player.rect.y = HEIGHT-200 
        finish_menu.disable()

mytheme = pygame_menu.Theme(background_color=(0, 0, 0, 0), # transparent background
                title_background_color=(4, 47, 126),
                title_font_shadow=True,
                widget_padding=25,
                )

menu = pygame_menu.Menu('Space Shooter', WIDTH, HEIGHT,
                       theme=pygame_menu.myth)

menu.add.button('Грати', start_the_game)
menu.add.selector('Складність :', [('Hard', 1), ('Medium', 2), ('Easy', 3)], onchange=set_difficulty)
menu.add.button('Вийти', pygame_menu.events.EXIT)

finish_menu = pygame_menu.Menu('Space Shooter', WIDTH, HEIGHT,
                       theme=pygame_menu.themes.THEME_DARK)

finish_menu.add.button('Рестарт', restart_game)
finish_menu.add.selector('Складність :', [('Hard', 1), ('Medium', 2), ('Easy', 3)], onchange=set_difficulty)
finish_menu.add.button('Вийти', pygame_menu.events.EXIT)

menu.mainloop(window)

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                run = False

    if not finish:
        all_sprites.update()   
        now = time.get_ticks()
        if now - spawn_timer > random.randint(1200, max_spawn_time):
            spawn_timer = now
            enemy_count = random.randint(1,5)     
            for i in range(enemy_count):
                enemy_group.add(Enemy(enemy_img, 120, 80))

        collide_list = sprite.groupcollide(enemy_group, player.bullets, True, True, sprite.collide_mask)        
        for enemy in collide_list:
            player.score+=10
            score_label.set_text(f'Score: {player.score}')

        if player.hp<=0:
            finish = True 
            finish_menu.enable()
            finish_menu.mainloop(window)           
                
    bg1_y += player.speed_y
    bg2_y += player.speed_y 
    if bg1_y > HEIGHT:
        bg1_y = -HEIGHT
    if bg2_y > HEIGHT:
        bg2_y = -HEIGHT             
    window.blit(bg, (0,bg1_y))
    window.blit(bg, (0,bg2_y))

    all_sprites.draw(window)
    all_labels.draw(window)

    display.update()
    clock.tick(FPS)       