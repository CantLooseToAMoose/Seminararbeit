import pixelmap
import numpy as np
import custom_environment
import time

pm = pixelmap.Pixelmap(50, 50, 10)

obstacle_1 = np.zeros((2, 3))
obstacle_1[0, 0:3] = 1
obstacle_2 = np.ones((5, 3))
obstacle_3 = np.ones((5, 40))
obstacle_4 = np.ones((3, 5))
obstacle_5 = np.ones((7, 7))

pm.set_obstacle(obstacle_1, location=(25, 14))
pm.set_obstacle(obstacle_2, location=(40, 10))
pm.set_obstacle(obstacle_3, location=(5, 5))
pm.set_obstacle(obstacle_4, location=(30, 30))
pm.set_obstacle(obstacle_5,location=(15,25))

pm.show_pixelmap()

environment = custom_environment.Environment(pm)
environment.initialize_environment(start_pos=(1, 1), goal=(20, 20), vision_size=5)

for i in range(200):
    input = np.random.randint(-1, 2, 2)
    environment.step(input)
    time.sleep(0.3)

environment.show_environment()
