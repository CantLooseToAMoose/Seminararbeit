import map_collection
import model_provider
import keras
import tensorflow as tf
import numpy as np

inputs = tf.convert_to_tensor(np.random.rand(3, 4), dtype='float32')  # 3 timesteps, 4 features
h_c = [tf.zeros((1, 2)), tf.zeros((1, 2))]  # must initialize hidden/cell state for lstm cell
h_c = tf.convert_to_tensor(h_c, dtype='float32')
lstm = tf.keras.layers.LSTMCell(2)

# example of how you accumulate cell state over repeated calls to LSTMCell
inputs = tf.unstack(inputs, axis=0)
c_states = []
for cur_inputs in inputs:
    out, h_c = lstm(tf.expand_dims(cur_inputs, axis=0), h_c)
    h, c = h_c
    c_states.append(c)

model = model_provider.get_CNN_LSTM_DNN_model(filters_cnn=[100, 50, 10], kernels_cnn=[3, 3, 3], strides_cnn=[1, 1, 1],
                                              layers_dnn=[200, 100], input_shape_cnn=[10, 10, 1],
                                              input_shape_concat=[2], lstm_layer=256,
                                              number_of_outputs=4)
keras.utils.plot_model(model, "my_first_model_with_shape_info.png", show_shapes=True)
print(model.summary())
