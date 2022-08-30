from sdl2 import *
import window

def main():

    SDL_Init(SDL_INIT_VIDEO | SDL_INIT_AUDIO | SDL_INIT_EVENTS)
    window.run()

    return 0


if __name__ == "__main__":
    main()
