import pixelmap
import numpy as np

pm = pixelmap.Pixelmap(50, 50,3)

obstacle_1 = np.zeros((2, 3))
obstacle_1[0, 0:3] = 1

pm.set_obstacle(obstacle_1,location=(2,2))
pm.plot_map()
