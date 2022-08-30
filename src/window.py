
import sys
from sdl2 import *


def run():
    window = SDL_CreateWindow("The Pong Game", 0, 0, 800, 600, SDL_WINDOW_INPUT_GRABBED | SDL_WINDOW_INPUT_FOCUS)
    window.show()
    running = True
    while running:
        events = sdl2.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
        window.refresh()
    return 0

