from pygame import *

FPS = 60
WIDTH, HEIGHT = 700,500
#створи вікно гри
window = display.set_mode((700,500))
display.set_caption('Catch Up')
clock = time.Clock()
#задай фон сцени
bg = image.load('background.png')
bg = transform.scale(bg, (WIDTH,HEIGHT))

player_1_img = image.load('sprite1.png')
player_2_img = image.load('sprite2.png')
#створи 2 спрайти та розмісти їх на сцені

class Player(sprite.Sprite):
    def __init__(self, image, x, y, width, height):
        super().__init__()
        self.image = transform.scale(image, (width, height))
        self.rect = Rect(x, y, width, height)
        self.speed = 5

    def draw(self, window):
        window.blit(self.image, self.rect)

player1 = Player(player_1_img, 200, 300, 100, 100)
player2 = Player(player_2_img, 500, 300, 100, 100)

run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    keys = key.get_pressed()
    if keys[K_LEFT]:
        player1.rect.x -= player1.speed
    if keys[K_RIGHT]:
        player1.rect.x += player1.speed 
    if keys[K_UP]:
        player1.rect.y -= player1.speed 
    if keys[K_DOWN]:
        player1.rect.y += player1.speed         
              

    window.blit(bg, (0,0))
    player1.draw(window)
    player2.draw(window)

    display.update()
    clock.tick(FPS)