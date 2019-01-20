import numpy as np

from base.BaseModel import BaseModel
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, Dense, Conv2D
from tensorflow.keras.layers import MaxPooling2D, Dropout, Flatten


class NeuralNetwork(BaseModel):
    def __init__(self, config):
        super(NeuralNetwork, self).__init__(config)
        self.build_model()

    def build_model(self):
        self.model = Sequential()
        self.model.add(Conv2D(
            32,
            kernel_size=(5, 5),
            strides=(1, 1),
            activation=tf.nn.relu,
            input_shape=[175, 175, 3]))
        self.model.add(MaxPooling2D(
            pool_size=(2, 2),
            strides=(2, 2)))
        self.model.add(Conv2D(
            64,
            strides=(5, 5),
            activation=tf.nn.relu))
        self.model.add(MaxPooling2D(
            pool_size=(2, 2)),
            stride=(2, 2))
        self.model.add(Flatten())
        self.model.add(Dense(100, activation=tf.nn.relu))
        self.model.add(Dense(1, activation=tf.nn.sigmoid))

        self.model.compile(
            loss='binary_crossentropy',
            optimizer=self.config.model.optimizer
            metrics=['accuracy'])
