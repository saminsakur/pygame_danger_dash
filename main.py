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

test_surface = pygame.Surface((60, 60))
test_surface.fill("Red")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
    window.fill(white)

    window.blit(test_surface, (0, 0))

    pygame.display.update()
    clock.tick(FRAME_RATE)
