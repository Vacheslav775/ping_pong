from pygame import *
from random import *
from time import time as tm


mixer.init()
font.init()

window = display.set_mode((700,500))
display.set_caption('ping-pong')
background = transform.scale(image.load('fon.jpg'),(700,500))
clock = time.Clock()


class GameSprite(sprite.Sprite) :
    def __init__(self, player_image, player_x, player_y, player_speed, wihgt, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wihgt, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self) :
        window.blit(self.image, (self.rect.x, self.rect.y))
    
class Player(GameSprite) :
    def update_l(self) :
        keys_pressed = key.get_pressed()
        
        if keys_pressed[K_UP] and self.rect.y > 0 :
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 390 :
            self.rect.y += self.speed

    def update_r(self) :
        keys_pressed = key.get_pressed()
        
        if keys_pressed[K_w] and self.rect.y > 0 :
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 390 :
            self.rect.y += self.speed

    
player_l = Player('raketka.png', 0, 250, 5, 60, 110)
player_r = Player('raketka.png', 640, 250, 5, 60, 110)
ball = GameSprite('ball.png', 300, 200 ,5 , 100, 100)

speed_x = 3
speed_y = 3

finish = False

win2 = font.SysFont('Arial', 70).render('YOU WIN', True, (255, 215, 0))
lose = font.SysFont('Arial', 70).render('YOU LOSE', True, (255, 0, 0))


game = True
while game :
    
    for e in event.get() :
        if e.type == QUIT :
            game = False
        
    if finish != True :
        window.blit(background,(0,0))
        player_l.update_l()
        player_r.update_r()
        player_l.reset()
        player_r.reset()
        ball.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        
        
    
    


    display.update()
    clock.tick(60)
