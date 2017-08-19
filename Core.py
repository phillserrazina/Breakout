import pygame
import random
import Objects

pygame.init()

display_width = 800
display_height = 600

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Window Setup
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Breakout")
clock = pygame.time.Clock()


# Draws a rectangular shape on the screen
def draw(x, y, width, height, color):
    pygame.draw.rect(screen, color, [x, y, width, height])


# Call this function to start the game
def main():

    # Player info
    player = Objects.Player(display_width * 0.44,
                            display_height * 0.87,
                            100,
                            30,
                            0)

    # Ball info
    ball = Objects.Ball((player.x + player.width) - 59,
                        player.y - player.height + 8,
                        20,
                        20,
                        [-10, 10],
                        -15)

    enemy_list = Objects.enemy_list = []

    game_exit = False

    # Main game loop
    while not game_exit:

        # KEY HANDLING
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.speed = -25

                if event.key == pygame.K_RIGHT:
                    player.speed = +25

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.speed = 0

        # Movement changes
        player.x += player.speed
        ball.x += ball.speed_x
        ball.y += ball.speed_y

        # Draws on the screen
        screen.fill(black)
        draw(player.x, player.y, player.width, player.height, white)
        draw(ball.x, ball.y, ball.width, ball.height, white)
        if not enemy_list:
            Objects.make_enemy1(8)
            Objects.make_enemy2(8)
            Objects.make_enemy3(8)
            Objects.make_enemy4(8)
            Objects.make_enemy5(8)
            Objects.make_enemy6(8)

        # Prevents enemy drawing and deleting confusion
        for enemy in enemy_list:

            if not enemy.dead:
                draw(enemy.x, enemy.y, enemy.width, enemy.height, white)

            elif enemy.dead:
                enemy.width = 0
                enemy.height = 0
                enemy.x = 0
                enemy.y = 0

        # BOUNDARIES HANDLING

        # Doesn't let the player go off limits on the side
        if player.x < 25 or player.x + player.width + 5 > display_width - 10:
            player.speed = 0

        # Doesn't let the ball go off limits on the side
        if ball.x < 0 or ball.x - ball.width > display_width - ball.width - 25:
            ball.speed_x = -ball.speed_x

        # Doesn't let the ball go off limits on the top
        if ball.y < 0:
            ball.speed_y = -ball.speed_y

        # Resets position if player loses
        if ball.y + ball.height > display_height:
            main()

        # When ball hits the player's pad
        if ball.x + ball.width > player.x and player.x + player.width > ball.x:

            if player.y > ball.y > player.y - ball.height:
                ball.speed_y = -ball.speed_y - 1

                if ball.speed_x < 0:
                    s = random.randrange(0, 100)
                    if s < 40:
                        ball.speed_x -= 2
                    elif s > 50:
                        ball.speed_x -= 1
                    else:
                        ball.speed_x += 4
                        ball.speed_y += 2
                else:
                    s = random.randrange(0, 100)
                    if s < 40:
                        ball.speed_x += 2
                    elif s > 50:
                        ball.speed_x += 1
                    else:
                        ball.speed_x -= 4
                        ball.speed_y += 2

            elif display_height > ball.y - ball.height > player.y:
                main()

        # When ball hits enemies
        for enemy in enemy_list:

            if ball.x + ball.width > enemy.x and enemy.x + enemy.width > ball.x:

                if enemy.y + enemy.height > ball.y:
                    ball.speed_y = -ball.speed_y
                    enemy.dead = True
                    draw(enemy.x, enemy.y, enemy.width, enemy.height, black)
                    draw(enemy.x, enemy.y, enemy.width, enemy.height, white)

        # Updates the screen 30 times per second
        pygame.display.update()
        clock.tick(30)

main()
pygame.quit()
quit()
