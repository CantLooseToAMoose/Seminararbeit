import tensorflow as tf
from tensorflow import keras


def get_CNN_DNN_model(filters_cnn, kernels_cnn, strides_cnn, layers_dnn, input_shape_cnn, input_shape_concat,
                      number_of_outputs):
    input_cnn = keras.layers.Input(shape=input_shape_cnn)
    cnn = keras.layers.Conv2D(filters=filters_cnn[0], kernel_size=kernels_cnn[0], strides=strides_cnn[0])(input_cnn)
    for i in range(len(filters_cnn)):
        if i != 0:
            cnn = keras.layers.Conv2D(filters=filters_cnn[i], kernel_size=kernels_cnn[i], strides=strides_cnn[i])(cnn)
    cnn = keras.layers.Flatten()(cnn)
    input_concat = keras.layers.Input(input_shape_concat)
    concat = keras.layers.Concatenate()([cnn, input_concat])
    for i in range(len(layers_dnn)):
        concat = keras.layers.Dense(units=layers_dnn[i], activation="relu")(concat)
    concat = keras.layers.Dense(number_of_outputs, activation=keras.activations.softmax)(concat)
    model = keras.Model(inputs=[input_cnn, input_concat], outputs=[concat])
    return model


def get_CNN_LSTM_DNN_model(filters_cnn, kernels_cnn, strides_cnn, layers_dnn, input_shape_cnn, input_shape_concat,
                           lstm_layer,
                           number_of_outputs):
    input_cnn = keras.layers.Input(shape=input_shape_cnn)
    cnn = keras.layers.Conv2D(filters=filters_cnn[0], kernel_size=kernels_cnn[0], strides=strides_cnn[0])(input_cnn)
    for i in range(len(filters_cnn)):
        if i != 0:
            cnn = keras.layers.Conv2D(filters=filters_cnn[i], kernel_size=kernels_cnn[i], strides=strides_cnn[i])(cnn)
    cnn = keras.layers.Flatten()(cnn)
    input_concat = keras.layers.Input(input_shape_concat)
    concat = keras.layers.Concatenate()([cnn, input_concat])
    # WIP add LSTMCELL
    input_c = keras.layers.Input((1, lstm_layer))
    input_h = keras.layers.Input((1, lstm_layer))
    h_c = tf.convert_to_tensor([input_h, input_c], dtype='float32')
    # h_c=keras.layers.Input((2,1,lstm_layer))
    concat, states = keras.layers.LSTMCell(units=lstm_layer)(concat, h_c)
    for i in range(len(layers_dnn)):
        concat = keras.layers.Dense(units=layers_dnn[i], activation="relu")(concat)
    concat = keras.layers.Dense(number_of_outputs, activation=keras.activations.softmax)(concat)
    model = keras.Model(inputs=[input_cnn, input_concat], outputs=[concat, states])
    return model


def save_model(model, name):
    pathname = "models/"
    model.save(pathname + name)


def load_model(name):
    pathname = "models/"
    return keras.models.load_model(pathname + name)
