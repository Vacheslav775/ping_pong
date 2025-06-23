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
    def update(self) :
        keys_pressed = key.get_pressed()
        
        if keys_pressed[K_LEFT] and self.rect.x > 5 :
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 640 :
            self.rect.x += self.speed
        



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
        
    
    


    display.update()
    clock.tick(60)