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
        self.model.add(Flatten(input_shape=(175, 175, 3)))
        self.model.add(Dense(64, activation=tf.nn.relu))
        self.model.add(Dense(32, activation=tf.nn.relu))
        self.model.add(Dense(1, activation=tf.nn.sigmoid))

        self.model.compile(
            loss='binary_crossentropy',
            optimizer=self.config.model.optimizer
            metrics=['accuracy'])
