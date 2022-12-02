import numpy as np

import BreadthFirstSearch
import Viewer
from pixelmap import Pixelmap
from BreadthFirstSearch import BFSNode


class Environment:
    agent_index = 2
    goal_index = 3

    def __init__(self, pixelmap: Pixelmap):
        self.vision_size = None
        self.reward_function = None
        self.goal = None
        self.numpy_array = None
        self.agent_pos = None
        self.view = None
        self.pixelmap = pixelmap
        self.num_of_steps = 0
        self.steps_between_localisation = 0
        self.localisation_error = 0
        self.last_localisation = None
        self.start_pos = None
        self.steps_to_goal_array = None

    def initialize_environment(self, start_pos: (int, int), goal: (int, int), vision_size, reward_function,
                               steps_between_localisation=0, localisation_error=0):
        self.numpy_array = self.pixelmap.numpy_array
        self.initialize_agent(start_pos)
        self.initialize_goal(goal)
        self.vision_size = vision_size
        self.set_reward_function(reward_function)
        self.num_of_steps = 0
        self.steps_between_localisation = steps_between_localisation
        self.localisation_error = localisation_error

    def reset(self):
        self.agent_pos = self.start_pos
        self.num_of_steps = 0
        self.last_localisation = self.start_pos
        obs = self.get_observation()
        dest_vec = self.get_destination_vector()
        return obs, dest_vec

    def initialize_agent(self, start_pos: (int, int)):
        self.agent_pos = np.array(start_pos)
        self.start_pos = np.array(start_pos)
        self.last_localisation = start_pos

    def initialize_goal(self, pos: (int, int)):
        self.goal = np.array(pos)

    def set_reward_function(self, function):
        self.reward_function = function

    def smaller_distance_to_goal_reward_function(self, input):
        if not self.check_if_movement_is_valid(input):
            return -1
        dist_1 = self.goal - self.agent_pos
        dist_1 = dist_1[0] ** 2 + dist_1[1] ** 2
        dist_2 = self.goal - (self.agent_pos + input)
        dist_2 = dist_2[0] ** 2 + dist_2[1] ** 2
        if dist_2 == dist_1:
            return -1
        if dist_2 < dist_1:
            return 0
        if dist_2 > dist_1:
            return -2

    def steps_reward_function(self, input):
        return -1

    def reduce_steps_to_goal_reward_function(self, input):
        dist_1 = self.steps_to_goal(self.agent_pos)
        dist_2 = self.steps_to_goal(np.add(self.agent_pos, input))
        if dist_2 == dist_1:
            return -1
        if dist_2 < dist_1:
            return 0
        if dist_2 > dist_1:
            return -2

    # Breadth first search for shortest way to Goal
    def steps_to_goal(self, pos):
        # If this is the first time the algorithm runs I want to create an array with the number of steps required to reach the goal
        if (self.steps_to_goal_array is None):
            # Create array by use of Breadth First Search Algorithm
            # First Create an "array" of nodes
            node_array = list()
            for i in range(len(self.numpy_array)):
                node_array.append(list())
                for j in range(len(self.numpy_array[0])):
                    node_array[i].append(BFSNode(pos=(i, j)))
            # Then add nodes as neigbours
            for i in range(0, len(self.numpy_array)):
                for j in range(0, len(self.numpy_array[0])):
                    neighbours = [(-1, 0), (1, 0), (0, 1), (0, -1)]
                    for neighbour in neighbours:
                        if self.check_if_position_is_moveable((i + neighbour[0], j + neighbour[1])):
                            node_array[i][j].add_neighbour(node_array[i + neighbour[0]][j + neighbour[1]])
            # Now fill the steps to goal array with the actual number of steps to the goal at this point
            self.steps_to_goal_array = np.ones((len(self.numpy_array), len(self.numpy_array[0])))
            for i in range(len(self.numpy_array)):
                for j in range(len(self.numpy_array[0])):
                    BreadthFirstSearch.reset_list_of_list_of_nodes_previous(node_array)
                    path = BreadthFirstSearch.breadth_first_search(node_array, (i, j), self.goal)
                    self.steps_to_goal_array[i, j] = len(path)
        return self.steps_to_goal_array[pos[0], pos[1]]

    def check_if_position_is_moveable(self, position_to_check):
        if len(self.numpy_array) <= position_to_check[0] or position_to_check[0] < 0 or position_to_check[1] < 0 or len(
                self.numpy_array[0]) <= position_to_check[1]:
            return False
        if self.numpy_array[position_to_check[0], position_to_check[1]] == 0:
            return True
        else:
            return False

    def check_if_movement_is_valid(self, input):
        position_to_check = np.add(self.agent_pos, input)
        return self.check_if_position_is_moveable(position_to_check)

    def check_if_done(self):
        if self.reached_destination():
            return True
        else:
            return False

    def get_destination_vector(self):
        if self.num_of_steps % (self.steps_between_localisation + 1) == 0:
            if self.localisation_error == 0:
                # WIP for the error
                self.last_localisation = tuple(self.agent_pos)

        dest_vector = np.subtract(self.goal, self.last_localisation)
        return dest_vector[np.newaxis, :]

    def get_observation(self):
        obs = np.zeros((2 * self.vision_size, 2 * self.vision_size))
        x_borders = [self.agent_pos[0] - self.vision_size, self.agent_pos[0] + self.vision_size]
        y_borders = [self.agent_pos[1] - self.vision_size, self.agent_pos[1] + self.vision_size]
        x_copy_start = 0
        y_copy_start = 0
        x_copy_end = len(self.numpy_array)
        y_copy_end = len(self.numpy_array[0])
        if x_borders[0] < 0:
            x_copy_start = -x_borders[0]
            x_borders[0] = 0
        if x_borders[1] > len(self.numpy_array):
            x_copy_end -= x_borders[1]
            x_borders[1] = len(self.numpy_array)
        if y_borders[0] < 0:
            y_copy_start = -y_borders[0]
            y_borders[0] = 0
        if y_borders[1] > len(self.numpy_array[0]):
            y_copy_end -= y_borders[1]
            y_borders[1] = len(self.numpy_array[0])

        obs_cut = self.numpy_array[x_borders[0]:x_borders[1], y_borders[0]:y_borders[1]]
        obs[x_copy_start:x_copy_end, y_copy_start:y_copy_end] = obs_cut
        return obs[np.newaxis, :, :, np.newaxis]

    def reached_destination(self):
        if np.array_equal(self.goal, self.agent_pos):
            return True
        else:
            return False

    def step(self, input):
        reward = self.reward_function(input)
        if self.check_if_movement_is_valid(input):
            self.agent_pos = np.add(self.agent_pos, input)

        obs = self.get_observation()
        dest_vector = self.get_destination_vector()
        done = self.check_if_done()
        self.num_of_steps += 1
        return obs, dest_vector, reward, done

    def view_update_function(self):
        scale = self.pixelmap.scale_factor
        screen_array = self.pixelmap.numpy_pixel_array.copy()
        for i in range(scale):
            for j in range(scale):
                screen_array[self.agent_pos[0] * scale + i, self.agent_pos[1] * scale + j] = Environment.agent_index

        for i in range(scale):
            for j in range(scale):
                screen_array[self.goal[0] * scale + i, self.goal[1] * scale + j] = Environment.goal_index
        return screen_array

    def show_environment(self):
        screen_size = (
            self.pixelmap.heigth * self.pixelmap.scale_factor, self.pixelmap.heigth * self.pixelmap.scale_factor)
        self.view = Viewer.Viewer(self.view_update_function, screen_size)
        self.pixelmap.pixel_array_to_screen_pixel_array()
        self.view.start()
