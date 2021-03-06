# importing some important modules
import pygame
import random

# Declaring some colors and list of colors so that color of food not remain constant
pygame.init()
pygame.mixer.init()
color_screen=  (0,200,0)
color_rect = (0,100,0)
color_foodls = [(255,165,0),(0,0,255),(0,0,128),(102,0,102),(255,0,255),(255,0,0),(0,0,0)]

# Making a display for gaming
size_screen = (900,600)
screen = pygame.display.set_mode(size_screen)
pygame.display.set_caption('Snake Game @MauryaJi')

# Loading some images
image = pygame.image.load('1ak.jpg')
image2 = pygame.image.load('2nd.jpg')
image3 =  pygame.image.load('end.jpg')

pygame.display.update()
clock = pygame.time.Clock()
font  = pygame.font.SysFont(None,50)


def screen_score(text , color,x,y):
    """A function for display text on screen"""
    screen_text = font.render(text,True,color)
    screen.blit(screen_text,[x,y])


def snake_sizeyyy(screen,color,snk_list,snake_size):
    """A function for making snake body and increase the length of snake"""
    for x,y in snk_list:
     pygame.draw.rect(screen, color, [x, y, 15, 20])


def welcome():
    """Making a Welcome screen"""
    exit_game = True
    pygame.mixer.music.load('welcome.mp3')
    pygame.mixer.music.play(0)
    while exit_game:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.stop()


                    game_loop()
            elif event.type == pygame.QUIT:
                exit_game = False
        screen.fill((102, 0, 102))
        screen.blit(image2, (0, 0))

        pygame.display.update()


def game_loop():
    """All the activities like snake move , speed increase , score increase will done in this function"""

    # Open high score in text file and reading it
    with open('highscore.txt', 'r') as f:
        high_score = f.read()

    #declaring some values
    rect_x = 40
    rect_y = 35
    velocity_x = 0
    velocity_y = 0
    food_x = random.randrange(40, 845)
    food_y = random.randrange(30, 550)
    score = 0
    snake_size = 30
    snake_list = []
    color_food = (255, 165, 0)
    snake_length = 1
    runnig = True
    gameover = False

    #playing sound in background
    pygame.mixer.music.load('background.mp3')
    pygame.mixer.music.play()
    z = 5

    while runnig:

        if gameover == True:
            pygame.mixer.init()
            pygame.mixer.music.load('gameover.mp3')
            pygame.mixer.music.play(0)
            play = True

            while play:
                m = open('highscore.txt', 'w')
                m.write(str(high_score))
                screen.blit(image3, (0, 0))
                screen_score(f'Your score is {score}', (255, 255, 255), 320, 500)
                pygame.display.update()

                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        play = False
                        runnig = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            pygame.mixer.music.stop()
                            game_loop()


        else:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    runnig = False

                if event.type == pygame.KEYDOWN:

                        if event.key == pygame.K_RIGHT:
                            velocity_x = z
                            velocity_y = 0

                        if event.key == pygame.K_LEFT:
                            velocity_x = - z
                            velocity_y = 0

                        if event.key == pygame.K_UP:
                            velocity_y = - z
                            velocity_x = 0

                        if event.key == pygame.K_DOWN:
                            velocity_y = z
                            velocity_x = 0

            # Providing speed to snake
            rect_x = rect_x+velocity_x
            rect_y = rect_y+velocity_y
            screen.fill(color_screen)
            screen.blit(image,(0,0))

            # Drawing head of snake
            pygame.draw.rect(screen, color_rect, [rect_x, rect_y, snake_size,snake_size])

            # Drawing food
            pygame.draw.rect(screen, color_food, [food_x, food_y, 23, 23])

            # Eating food and making new food
            if abs(rect_x-food_x)<21 and abs(rect_y-food_y)<21:
                color_food = random.choice(color_foodls)
                food_x = random.randrange(40, 845)
                food_y = random.randrange(30, 550)
                score+=10
                # playing sound in different channel so that two sounds play together
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('eat.wav'))
                snake_length+=5

                # Making new high score
                if score>int(high_score):
                     high_score = score


            # Coordinates for snake body
            head  = []
            head.append(rect_x+4)
            head.append(rect_y+4)
            snake_list.append(head)
            for i in snake_list:
                print(i)
            #deleting the snake extra length
            if len(snake_list)>snake_length:
                del snake_list[0]

            # Showing score on screen
            screen_score("Score is : "+str(score)+"  HighScore: "+str(high_score),(255,0,0),5,5)

            # Callin a function to draw body of snake
            snake_sizeyyy(screen,color_rect,snake_list,snake_size)

            if rect_x >= 900 or rect_y >= 600 or rect_x <= 0 or rect_y <= 0:
             """ snake colliding with  boundary and itself the sign must be <= not == because if condition is == and in
             the coordinate rectx =599 and if it will eat food then rectx = 599+5 which is equal = 604 and hence it will
             not out because condition is == but if condition is >= then it will out because 604 is > then 600"""
             gameover = True

            # Colliding head of snake with itself
            if head in snake_list[:-1]:
                gameover =True


        # Changing speed of snake after fix scores
        if score>=70 and score<170:
            z = 8
        elif score>=170 and score<250:
            z = 10
        elif score>=250:
            z = 13

        pygame.display.update()
        clock.tick(45)
    pygame.quit()
    quit()
# Calling the Welcome function so that game will start
welcome()
