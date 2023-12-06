import pygame
import label
from picture import *


back = (135,248,255)
mw = pygame.display.set_mode((500,500))
mw.fill(back)
clock = pygame.time.Clock()

ball = Picture(mw,'ball.png',200,200,50,50)
speed_x = 3
speed_y = 3
platform = Picture(mw,'platform.png',330,400,100,30)

monsters = []
count = 9
start_x = 5
start_y = 5

for i in range(3):
    x = start_x + (28 * i)
    y = start_y + (55 * i)
    for i in range(count):
        monster = Picture(mw,'enemy.png',x,y,50,50)
        monsters.append(monster)
        x += 55
    count -= 1 
flag = True
move_right = False
move_left = False


while flag :
    ball.fill()
    platform.fill()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT: #если нажата клавиша
                move_right = True #поднимаем флаг
            if event.key == pygame.K_LEFT:
                move_left = True #поднимаем флаг
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                move_right = False #опускаем флаг
            if event.key == pygame.K_LEFT:
                move_left = False #опускаем флаг
    
    if move_right: #флаг движения вправо
        platform.rect.x +=4
    if move_left: #флаг движения влево
        platform.rect.x -=4
    
    ball.rect.x += speed_x
    ball.rect.y += speed_y

    if ball.colliderect(platform.rect):
        speed_y *= -1
    if ball.rect.x > 450 or ball.rect.x < 0:
        speed_x *= -1
    if ball.rect.y < 0:
        speed_y *= -1
    if platform.rect.x > 400:
        move_right = False
    if platform.rect.x < 0:
        move_left = False
    if ball.rect.y > 500:
        text = label.Label(mw,0,0,500,500,(255,0,0))
        text.set_text('You lose',70)
        text.draw(100,300)
        flag = False
    if len(monsters) == 0:
        text = label.Label(mw,0,0,500,500,(0,255,0))
        text.set_text('You win',70,)
        text.draw(100,300)
        flag = False

    ball.draw()
    platform.draw()

    for i in monsters:
        i.draw()
        if i.rect.colliderect(ball.rect):
            monsters.remove(i)
            i.fill()
            speed_y *= -1 

        


    pygame.display.update()
    clock.tick(40)