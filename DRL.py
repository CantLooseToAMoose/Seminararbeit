import random

import custom_environment
import model_provider
from tensorflow import keras
import tensorflow as tf


# Here are multiple excerpts or abstractions from the Book:"Hands on Machine Learning with Scikit-Learn,Keras,Tensorflow

def play_one_step(env, obs, model, loss_fn):
    with tf.GradientTape() as tape:
        model_output = model(obs)
        action = model_output_to_action(model_output)


def model_output_to_action(model_output):
    rand = random.Random.random()
    summed_prob = 0
    case = -1
    for i in range(len(model_output)):
        summed_prob += model_output[i]
        case = i
        if summed_prob > rand:
            break
    # up
    if case == 0:
        return [0, 1]
    # down
    if case == 1:
        return [0, -1]
    # left
    if case == 2:
        return [-1, 0]
    # right
    if case == 3:
        return [1, 0]
