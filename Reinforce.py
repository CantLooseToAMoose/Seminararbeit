import random

import custom_environment
import model_provider
from tensorflow import keras
import tensorflow as tf
import numpy as np


# Here are multiple excerpts or abstractions from the Book:"Hands on Machine Learning with Scikit-Learn,Keras,Tensorflow

# The following is a common implementation of the "Reinforce" Algorithm

def play_one_step(env, obs, dest_vector, model, loss_fn):
    with tf.GradientTape() as tape:
        model_output = model([obs, dest_vector])
        action, case = model_output_to_action(model_output)
        y_target = np.zeros(4)
        y_target[case] = 1
        y_target = y_target[np.newaxis, :]
        loss = tf.reduce_mean(loss_fn(y_target, model_output))
    grads = tape.gradient(loss, model.trainable_variables)
    obs, dest_vector, reward, done = env.step(action)
    return obs, dest_vector, reward, done, grads


def play_multiple_episodes(env, n_episodes, n_max_steps, model, loss_fn):
    all_rewards = []
    all_grads = []
    for episode in range(n_episodes):
        current_rewards = []
        current_grads = []
        obs, dest_vector = env.reset()
        for step in range(n_max_steps):
            obs, dest_vector, reward, done, grads = play_one_step(env, obs, model, loss_fn)
            current_rewards.append(reward)
            current_grads.append(grads)
            if done:
                break
            all_rewards.append(current_rewards)
            all_grads.append(current_grads)
    return all_rewards, all_grads


def discount_rewards(rewards, discount_factor):
    discounted = np.array(rewards)
    for step in range(len(rewards) - 2, -1, -1):
        discounted[step] += discounted[step + 1] * discount_factor
    return discounted


def discount_and_normalize_rewards(all_rewards, discount_factor):
    all_discounted_rewards = [discount_rewards(rewards, discount_factor) for rewards in all_rewards]
    flat_rewards = np.concatenate(all_discounted_rewards)
    reward_mean = flat_rewards.mean()
    reward_std = flat_rewards.std()
    return [(discounted_rewards - reward_mean) / reward_std for discounted_rewards in all_discounted_rewards]


def start_training(env, model, n_iterations=150, n_episodes_per_update=10, n_max_steps=200, discount_factor=0.95,
                   optimizer=keras.optimizers.Adam(lr=0.010), loss_fn=keras.losses.categorical_crossentropy):
    for iteration in range(n_iterations):
        all_rewards, all_grads = play_multiple_episodes(env, n_episodes_per_update, n_max_steps, model, loss_fn)
        all_final_rewards = discount_and_normalize_rewards(all_rewards, discount_factor)
        all_mean_grads = []
        for var_index in range(len(model.trainable_variables)):
            mean_grads = tf.reduce_mean(
                [final_reward * all_grads[episode_index][step][var_index] for episode_index, final_rewards in
                 enumerate(all_final_rewards) for step, final_reward in enumerate(final_rewards)], axis=0)
        all_mean_grads.append(mean_grads)
        optimizer.apply_gradients(zip(all_mean_grads, model.trainable_variables))
    return model


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
        return [0, 1], case
    # down
    if case == 1:
        return [0, -1], case
    # left
    if case == 2:
        return [-1, 0], case
    # right
    if case == 3:
        return [1, 0], case
