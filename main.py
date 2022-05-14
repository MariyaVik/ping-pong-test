from pygame import *

# классы
class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (wight, height)) 
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
 
# игровая сцена
back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)
 
# шрифты
font.init()
font = font.Font(None, 35)
text_lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
text_lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))

# картинки
img_ball = 'images/tenis_ball.png'
img_rocket = 'images/tenis_ball.png'

# константы

 
# флаги, отвечающие за состояние игры
game = True
finish = False
clock = time.Clock()
FPS = 60
 
# создание мяча и ракеток  


# игровой цикл
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        window.fill(back)

    
    display.update()
    clock.tick(FPS)