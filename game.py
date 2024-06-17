import pygame
import random

# Initialize the game
pygame.init()

# Screen dimensions
screen_width = 600
screen_height = 400

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()
snake_size = 10
snake_speed = 15

font_style = pygame.font.SysFont(None, 50)

def our_snake(snake_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], snake_size, snake_size])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [screen_width / 6, screen_height / 3])

def gameLoop():
    while True:
        game_over = False
        game_close = False

        x1 = screen_width / 2
        y1 = screen_height / 2

        x1_change = 0
        y1_change = 0

        snake_List = []
        Length_of_snake = 1

        foodx = round(random.randrange(0, screen_width - snake_size) / 10.0) * 10.0
        foody = round(random.randrange(0, screen_height - snake_size) / 10.0) * 10.0

        while not game_over:

            while game_close:
                screen.fill(white)
                message("You Lost! Press Q-Quit or C-Play Again", red)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            gameLoop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -snake_size
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = snake_size
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -snake_size
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = snake_size
                        x1_change = 0

            if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
                game_close = True
            x1 += x1_change
            y1 += y1_change
            screen.fill(white)
            pygame.draw.rect(screen, green, [foodx, foody, snake_size, snake_size])
            snake_Head = [x1, y1]
            snake_List.append(snake_Head)
            if len(snake_List) > Length_of_snake:
                del snake_List[0]

            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True

            our_snake(snake_size, snake_List)

            pygame.display.update()

            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, screen_width - snake_size) / 10.0) * 10.0
                foody = round(random.randrange(0, screen_height - snake_size) / 10.0) * 10.0
                Length_of_snake += 1

            clock.tick(snake_speed)

        if game_over:
            break

    pygame.quit()
    quit()

gameLoop()
