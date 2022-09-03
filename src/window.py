
import pygame

background = (0,0,0)

screen = pygame.display.set_model((300,300))

pygame.display.set_caption("Pong")

screen.fill(background)

pygame.display.flip()
running = True

while(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
