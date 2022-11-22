# https://karthikkaranth.me/blog/drawing-pixels-with-python/

import pygame
import threading


class Viewer:
    def __init__(self, update_func, display_size):
        self.update_func = update_func
        pygame.init()
        self.display = pygame.display.set_mode(display_size)

    def set_title(self, title):
        pygame.display.set_caption(title)

    def start(self):
        visualizer = MyVisualizerThread(1, "myThread", self)
        visualizer.start()


class MyVisualizerThread(threading.Thread):
    def __init__(self, threadID, name, view):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.view = view

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            Z = self.view.update_func()
            surf = pygame.surfarray.make_surface(Z)
            surf.set_palette_at(0, (255, 255, 255))
            surf.set_palette_at(1, (0, 0, 0))
            surf.set_palette_at(2, (250, 5, 5))
            surf.set_palette_at(3, (3, 200, 3))
            self.view.display.blit(surf, (0, 0))
            pygame.display.update()

        pygame.quit()
