import numpy as np
import matplotlib.pyplot as plt
import pygame
import Viewer


class Pixelmap:
    wall = 1

    def __init__(self, width: int, heigth: int, scale_factor: int):
        self.width = width
        self.heigth = heigth
        self.scale_factor = scale_factor
        self.numpy_array = np.zeros((heigth, width))
        self.numpy_pixel_array = np.zeros((self.heigth * self.scale_factor, self.width * self.scale_factor))
        self.set_border()

    def set_border(self):
        for i in range(self.heigth):
            self.numpy_array[i, 0] = Pixelmap.wall
        for j in range(self.width):
            self.numpy_array[0, j] = Pixelmap.wall
        for i in range(self.heigth):
            self.numpy_array[i, self.width - 1] = Pixelmap.wall
        for j in range(self.width):
            self.numpy_array[self.heigth - 1, j] = Pixelmap.wall

    def set_obstacle(self, obstacle: np.array, location: (int, int)):
        for i in range(len(obstacle)):
            for j in range(len(obstacle[0])):
                self.numpy_array[i + location[0], j + location[1]] = obstacle[i, j]

    def pixel_array_to_screen_pixel_array(self):
        self.numpy_pixel_array = np.zeros((self.heigth * self.scale_factor, self.width * self.scale_factor))
        for i in range(self.heigth):
            for j in range(self.width):
                for k in range(self.scale_factor):
                    for l in range(self.scale_factor):
                        self.numpy_pixel_array[i * self.scale_factor + k, j * self.scale_factor + l] = self.numpy_array[
                            i, j]

    def show_pixelmap(self):
        plt.imshow(self.numpy_array.T)
        plt.show()
