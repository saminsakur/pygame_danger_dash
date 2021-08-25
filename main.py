import sys
import pygame

# Initialize pygame
pygame.init()
pygame.display.init()

HEIGHT = 400
WIDTH = 800
FRAME_RATE = 60

# Define colors
white = (255, 255, 255)
red = (255, 0, 0)

# Initialize window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cool game")


# Define clock
clock = pygame.time.Clock()

text = pygame.font.Font("font/Pixeltype.ttf", 50)

sky_surface = pygame.image.load("graphics/Sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()

text_surface = text.render("hello world!", False, "black")

snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_x_pos = 600
snail_speed = 4

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

    window.blit(sky_surface, (0, 0))
    window.blit(ground_surface, (0, 300))
    window.blit(text_surface, (300, 50))

    snail_x_pos -= snail_speed
    if snail_x_pos <= -100:
        snail_x_pos = WIDTH

    window.blit(snail_surface, (snail_x_pos, 260))

    pygame.display.update()
    pygame.display.flip()
    clock.tick(FRAME_RATE)
