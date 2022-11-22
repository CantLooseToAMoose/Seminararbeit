import pixelmap
import numpy as np
import custom_environment
import time
import Reinforce
import model_provider
import matplotlib.pyplot as plt

pm = pixelmap.Pixelmap(50, 50, 10)

obstacle_1 = np.zeros((2, 3))
obstacle_1[0, 0:3] = 1
obstacle_2 = np.ones((5, 3))
obstacle_3 = np.ones((15, 4))
obstacle_4 = np.ones((3, 5))
obstacle_5 = np.ones((7, 7))
obstacle_6 = np.ones((4, 15))

pm.set_obstacle(obstacle_1, location=(25, 14))
pm.set_obstacle(obstacle_2, location=(40, 10))
pm.set_obstacle(obstacle_3, location=(5, 5))
pm.set_obstacle(obstacle_4, location=(30, 30))
pm.set_obstacle(obstacle_5, location=(15, 25))
pm.set_obstacle(obstacle_6, location=(5, 5))

pm.show_pixelmap()

environment = custom_environment.Environment(pm)
environment.initialize_environment(start_pos=(1, 1), goal=(20, 20), vision_size=5,
                                   reward_function=environment.smaller_distance_to_goal_reward_function)
print("Start step to goal Array")
environment.steps_to_goal((1, 1))
plt.imshow(environment.steps_to_goal_array.T)
plt.show()
environment.show_environment()

model = model_provider.get_CNN_DNN_model(filters_cnn=[100, 50, 10], kernels_cnn=[3, 3, 3], strides_cnn=[1, 1, 1],
                                         layers_dnn=[200, 100], input_shape_cnn=[10, 10, 1], input_shape_concat=[2],
                                         number_of_outputs=4)

# model = model_provider.load_model("test_model")
print(model.summary())
trained_model = Reinforce.start_training(env=environment, model=model, n_iterations=50, n_episodes_per_update=20)
# model_provider.save_model(trained_model, "test_model")
