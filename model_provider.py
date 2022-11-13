import tensorflow as tf
from tensorflow import keras


def get_CNN_DNN_model(filters_cnn,kernels_cnn,strides_cnn, layers_dnn, input_shape,number_of_outputs):
    model=keras.models.Sequential()
    for i in range(len(filters_cnn)):
        if i==0:
            model.add(keras.layers.Conv2D(filters=filters_cnn[i],kernel_size=kernels_cnn[i],strides=strides_cnn[i],input_shape=input_shape))
        else:
            model.add(keras.layers.Conv2D(filters=filters_cnn[i], kernel_size=kernels_cnn[i], strides=strides_cnn[i]))

    model.add(keras.layers.Dropout(0.5))
    model.add(keras.layers.Flatten())
    for i in range(len(layers_dnn)):
        model.add(keras.layers.Dense(layers_dnn[i],activation="relu"))
    model.add(keras.layers.Dense(number_of_outputs, activation=keras.activations.softmax))

