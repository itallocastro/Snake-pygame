import pygame,random
from pygame.locals import *

def on_grid():
    x = random.randint(0,590)
    y = random.randint(0,590)
    return (x//10 * 10, y//10 * 10)

def collision(head, apple):
    return (head[0] == apple[0] and head[1] == apple[1])

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Snake by Itallo')

snake = [(200,200),(210,200), (220,200)]
snake_style = pygame.Surface((10,10))
snake_style.fill((255,255,255))

apple  = pygame.Surface((10,10))
apple.fill((255,0,0))
apple_position = on_grid()
direction = LEFT


clock = pygame.time.Clock()
while True:
    clock.tick(15)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                direction = UP
            if event.key == K_DOWN:
                direction = DOWN
            if event.key == K_LEFT:
                direction = LEFT
            if event.key == K_RIGHT:
                direction = RIGHT

    if collision(snake[0],apple_position):
        apple_position = on_grid()
        snake.append((0,0))

    for i in range(len(snake)-1,0,-1):
        snake[i] = (snake[i-1][0],snake[i-1][1])
    
    if direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    screen.fill((0,0,0))
    screen.blit(apple,apple_position)
    for pos in snake:
        screen.blit(snake_style,pos)


    pygame.display.update()

