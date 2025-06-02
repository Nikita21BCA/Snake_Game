import pygame
import time
import random

# Initialize pygame
pygame.init()

# Colors (classic look)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Display size (classic phone aspect ratio)
DIS_WIDTH = 400
DIS_HEIGHT = 400

dis = pygame.display.set_mode((DIS_WIDTH, DIS_HEIGHT))
pygame.display.set_caption('Snake Xenzia (Classic Snake 2)')

clock = pygame.time.Clock()

SNAKE_BLOCK = 10
SNAKE_SPEED = 15

font_style = pygame.font.SysFont("consolas", 24)

def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, GREEN, [x[0], x[1], snake_block, snake_block])

def show_score(score):
    value = font_style.render(f"Score: {score}", True, WHITE)
    dis.blit(value, [10, 10])

def gameLoop():
    game_over = False
    game_close = False

    x1 = DIS_WIDTH // 2
    y1 = DIS_HEIGHT // 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, DIS_WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
    foody = round(random.randrange(0, DIS_HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0

    direction = 'RIGHT'
    change_to = direction

    while not game_over:

        while game_close:
            dis.fill(BLACK)
            msg = font_style.render("Game Over! Press C to Play Again or Q to Quit", True, WHITE)
            dis.blit(msg, [DIS_WIDTH // 16, DIS_HEIGHT // 2.5])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != 'RIGHT':
                    change_to = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    change_to = 'RIGHT'
                elif event.key == pygame.K_UP and direction != 'DOWN':
                    change_to = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    change_to = 'DOWN'

        direction = change_to

        if direction == 'LEFT':
            x1_change = -SNAKE_BLOCK
            y1_change = 0
        elif direction == 'RIGHT':
            x1_change = SNAKE_BLOCK
            y1_change = 0
        elif direction == 'UP':
            y1_change = -SNAKE_BLOCK
            x1_change = 0
        elif direction == 'DOWN':
            y1_change = SNAKE_BLOCK
            x1_change = 0

        # Wall wrapping
        x1 = (x1 + x1_change) % DIS_WIDTH
        y1 = (y1 + y1_change) % DIS_HEIGHT

        dis.fill(BLACK)
        pygame.draw.rect(dis, RED, [foodx, foody, SNAKE_BLOCK, SNAKE_BLOCK])
        snake_Head = [x1, y1]
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Check self-collision
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        draw_snake(SNAKE_BLOCK, snake_List)
        show_score(Length_of_snake - 1)

        pygame.display.update()

        # Eating food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, DIS_WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
            foody = round(random.randrange(0, DIS_HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0
            Length_of_snake += 1
            # Optional: Increase speed as snake grows
            # SNAKE_SPEED = min(30, SNAKE_SPEED + 0.5)

        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()

if __name__ == "__main__":
    gameLoop()
