import numpy as np
import matplotlib.pyplot as plt
import pygame


class Pixelmap:
    wall = 1
    run=True

    def quit_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

    def __init__(self, width: int, heigth: int,scale_factor:int):
        self.width = width
        self.heigth = heigth
        self.scale_factor=scale_factor
        self.pixel_array = np.zeros((heigth,width))
        self.screen_pixel_array=np.zeros((self.heigth*self.scale_factor,self.width*self.scale_factor))
        self.set_border()

    def set_border(self):
        for i in range(self.heigth):
            self.pixel_array[i, 0] = Pixelmap.wall
        for j in range(self.width):
            self.pixel_array[0, j] = Pixelmap.wall
        for i in range(self.heigth):
            self.pixel_array[i, self.width-1] = Pixelmap.wall
        for j in range(self.width):
            self.pixel_array[self.heigth-1, j] = Pixelmap.wall

    def set_obstacle(self, obstacle: np.array, location: (int, int)):
        for i in range(len(obstacle)):
            for j in range(len(obstacle[0])):
                self.pixel_array[i + location[0], j + location[1]] = obstacle[i,j]


    def pixel_array_to_screen_pixel_array(self):
        self.screen_pixel_array=np.zeros((self.heigth*self.scale_factor,self.width*self.scale_factor))
        for i in range(self.heigth):
            for j in range(self.width):
                for k in range(self.scale_factor):
                    for l in range(self.scale_factor):
                        self.screen_pixel_array[i+k,j+l]=self.pixel_array[i,j]




    def plot_map(self):
        pygame.init()
        screen = pygame.display.set_mode((self.width*self.scale_factor, self.heigth*self.scale_factor))
        screen.fill((255, 255, 255))
        black = screen.map_rgb((0, 0, 0))
        white=screen.map_rgb((255,255,255))
        self.pixel_array_to_screen_pixel_array()
        surf = pygame.surfarray.make_surface(self.screen_pixel_array)

        while self.run:
            # check if game is closed
            self.quit_game()
            screen.blit(surf, (0, 0))
            pygame.display.update()
