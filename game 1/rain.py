import pygame
import random
import time
#init pygame!!
pygame.init()

#display-is obieqtis gaketeba zomaze
width = 920
height = 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My platformer Game")


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the player
player_size = 50
player_x = width // 2 - player_size // 2
player_y = height - player_size
player_speed = 2
  
# Set up the enemy
enemy_size = 50
enemy_x = random.randint(0, width - enemy_size)
enemy_y = 0
enemy_speed = 1.2
#suratis chatvirtva!
background_img = pygame.image.load("start_screen.png")
end_screen = pygame.image.load("end_screen.jpg")
end_screen = pygame.transform.scale(end_screen, (width, height))
#gilakis gaketeba zomaze da suratis mimagreba!
start_btn_img = pygame.image.load("start_button.png")
button_width = 150
button_height = 100
start_btn_img = pygame.transform.scale(start_btn_img, (button_width, button_height))
start_btn_rect = start_btn_img.get_rect()
start_btn_rect.center = (453, 600)

gameon = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if start_btn_rect.collidepoint(mouse_pos):
                gameon = True
                print("Start button clicked!!!") # aq dawer shens logikas ra unda mmoxdes startze dacherisas
    if gameon:
        # Handle player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < width - player_size:
            player_x += player_speed

        # Update enemy position
        enemy_y += enemy_speed
        if enemy_y > height:
            enemy_x = random.randint(0, width - enemy_size)
            enemy_y = 0

        # Check for collision
        if (enemy_x >= player_x and enemy_x < player_x + player_size) or (
            player_x >= enemy_x and player_x < enemy_x + enemy_size
        ):
            if (enemy_y >= player_y and enemy_y < player_y + player_size) or (
                player_y >= enemy_y and player_y < enemy_y + enemy_size
            ):


                #screen image-is chveneba
                screen.blit(end_screen, (0, 0))
                #ganaxleba monitoris
                pygame.display.flip()
                time.sleep(3)
                running = False

        # Draw everything
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, (player_x, player_y, player_size, player_size))
        pygame.draw.rect(screen, WHITE, (enemy_x, enemy_y, enemy_size, enemy_size))
        pygame.display.update()
    else:
        #screen image-is chveneba
        screen.blit(background_img, (0, 0))

        #achvene start button-i
        screen.blit(start_btn_img, start_btn_rect)

        #ganaxleba monitoris
        pygame.display.flip()

pygame.quit()
