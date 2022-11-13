import numpy as np

import Viewer
from pixelmap import Pixelmap


class Environment:
    agent_index = 2

    def __init__(self, pixelmap: Pixelmap):
        self.vision_size = None
        self.reward_function = None
        self.goal = None
        self.numpy_array = None
        self.agent_pos = None
        self.view = None
        self.pixelmap = pixelmap

    def initialize_environment(self, start_pos: (int, int), goal: (int, int), vision_size,reward_function):
        self.numpy_array = self.pixelmap.numpy_array
        self.initialize_agent(start_pos)
        self.initialize_goal(goal)
        self.vision_size = vision_size
        self.set_reward_function(reward_function)

    def initialize_agent(self, start_pos: (int, int)):
        self.agent_pos = start_pos

    def initialize_goal(self, pos: (int, int)):
        self.goal = pos

    def set_reward_function(self, function):
        self.reward_function = function

    def check_if_movement_is_valid(self, input):
        position_to_check = self.agent_pos + input
        if self.numpy_array[position_to_check[0], position_to_check[1]] == 0:
            return True
        else:
            return False

    def reached_destination(self):
        if self.agent_pos == self.goal:
            return True
        else:
            return False

    def step(self, input):
        if self.check_if_movement_is_valid(input):
            self.agent_pos += input

        return self.numpy_array[self.agent_pos[0] - self.vision_size:self.agent_pos[0] + self.vision_size,
               self.agent_pos[1] - self.vision_size:self.agent_pos[
                                                        1] + self.vision_size]

    def view_update_function(self):
        scale = self.pixelmap.scale_factor
        screen_array = self.pixelmap.numpy_pixel_array.copy()
        for i in range(scale):
            for j in range(scale):
                screen_array[self.agent_pos[0] * scale + i, self.agent_pos[1] * scale + j] = Environment.agent_index
        return screen_array

    def show_environment(self):
        screen_size = (
            self.pixelmap.heigth * self.pixelmap.scale_factor, self.pixelmap.heigth * self.pixelmap.scale_factor)
        self.view = Viewer.Viewer(self.view_update_function, screen_size)
        self.pixelmap.pixel_array_to_screen_pixel_array()
        self.view.start()
