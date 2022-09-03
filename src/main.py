import pygame


def main():

    pygame.init()
    surface = pygame.display.set_mode((400,300))
    pygame.display.set_caption('Hello world')


    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                return

    return


if __name__ == "__main__":
    main()
