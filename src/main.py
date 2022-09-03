import pygame
import window

def main():

    pygame.init()
    surface = pygame.display.set_mode((400,300))


    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                return

    return


if __name__ == "__main__":
    window.window()
    
