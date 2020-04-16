import pygame,random,time
from pygame.locals import *
from pygame.font import *


pygame.init()
def bottom(x,y,widht,height,color1,color2,message, action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + widht > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screen, color1 , (x,y,widht,height))
        if click[0]==1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, color2, (x,y,widht,height))
    text_bottom =  pygame.font.Font('mytype.ttf',20)
    TextSurf,TextRect = text_objects(message,text_bottom,(0,0,0))
    TextRect.center = ((x + widht/2,y + height/2))
    screen.blit(TextSurf,TextRect)

def pause():
    text_bottom =  pygame.font.Font('mytype.ttf',50)
    TextSurf,TextRect = text_objects(messa,text_bottom,(0,0,0))
    TextRect.center = ((x + widht/2,y + height/2))
    screen.blit(TextSurf,TextRect)
    
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            #print(event)
            if(event.type == pygame.QUIT):
                pygame.display.quit()
        screen.fill((0,0,0))
        big_text = pygame.font.Font('mytype.ttf',50)
        TextSurf,TextRect = text_objects("Snake by Itallo",big_text)
        TextRect.center = ((300,300))
        screen.blit(TextSurf,TextRect)

        bottom(150,450,100,50,(255,0,0), (200,0,0), "Start",game)
        bottom(300,450,100,50,(255,0,0), (200,0,0), "Exit", exit)


        pygame.display.update()
        clock.tick(15)

def on_grid():
    x = random.randint(0,590)
    y = random.randint(0,590)
    return (x//10 * 10, y//10 * 10)
def text_objects(text, font, color = (255,0,0)):
    textSurface = font.render(text,True,color)
    return textSurface,textSurface.get_rect()

def message_display(text):
    big_text = pygame.font.Font('mytype.ttf',80)
    TextSurf,TextRect = text_objects(text,big_text)
    TextRect.center = ((300,300))
    screen.blit(TextSurf,TextRect)

    pygame.display.update()
    time.sleep(2)



def game_over():
    message_display("Game Over")
    game_intro()


def collision(head, apple):
    return (head[0] == apple[0] and head[1] == apple[1])

def collision_body(snake):

   for i in range(1,len(snake)-1,1):
        if(snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]):
            game_over()
            return True
def pontuation(cont):
    font =  pygame.font.SysFont(None,25)
    text = font.render("Pontuation: " + str(cont), True, (255,255,255))
    screen.blit(text,(0,0))

def exit():
    pygame.display.quit()
    quit()

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Snake by Itallo')
clock = pygame.time.Clock()

def game():
    start = True

    apple_position = on_grid()
    direction = LEFT


    while True:
        cont = 0
        velo = 15

        screen = pygame.display.set_mode((600,600))
        pygame.display.set_caption('Snake by Itallo')

        snake = [(200,200),(210,200), (220,200)]
        snake_style = pygame.Surface((10,10))
        snake_style.fill((255,255,255))

        apple  = pygame.Surface((10,10))
        apple.fill((255,0,0))
        apple_position = on_grid()

        direction = LEFT
        start = not start
        
        while start:
            clock.tick(velo)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.display.quit()
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
                cont+=10
                velo+=2
                snake.append((0,0))
            #verifica se colidiu
            if collision_body(snake):
                start = not start

            #cada pedaço pega o anterior
            for i in range(len(snake)-1,0,-1):
                snake[i] = (snake[i-1][0],snake[i-1][1])

            

            screen.fill((0,0,0))
            pontuation(cont)

            #proxima direção
            if direction == UP:
                snake[0] = (snake[0][0], 600 if snake[0][1] - 10 == 0 else snake[0][1] - 10)
            if direction == DOWN:
                snake[0] = (snake[0][0], 0 if snake[0][1] + 10 == 600 else snake[0][1] + 10)
            if direction == RIGHT:
                snake[0] = (0 if snake[0][0] + 10 == 600 else snake[0][0] + 10, snake[0][1])
            if direction == LEFT:
                snake[0] = (600 if snake[0][0] - 10 == 0 else snake[0][0]-10, snake[0][1])

            #plota a maçã na tela
            screen.blit(apple,apple_position)

            #plota a snake na tela
            for pos in snake:
                screen.blit(snake_style,pos)

            pygame.display.update()


game_intro()
game()


