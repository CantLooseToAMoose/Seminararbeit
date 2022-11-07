import pixelmap
import numpy as np
import custom_environment
import time

pm = pixelmap.Pixelmap(50, 50, 10)

obstacle_1 = np.zeros((2, 3))
obstacle_1[0, 0:3] = 1

pm.set_obstacle(obstacle_1, location=(2, 2))

environment = custom_environment.Environment(pm)
environment.initialize_environment(start_pos=(1, 1), goal=(20, 20), vision_size=5)
environment.show_environment()

for i in range(200):
    input = np.random.randint(-1, 2, 2)
    environment.step(input)
    time.sleep(0.3)
