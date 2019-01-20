import os

from base.BaseTrain import BaseTrain
from tensorflow.keras.callbacks import ModelCheckPoint
from tensorflow.keras.callbacks import TensorBoard


class Trainer:
    def __init__(self, model, data, config):
        super(Trainer, self).__init__(model, data, config)
        self.callbacks = []
        self.loss = []
        self.acc = []
        self.val_loss = []
        self.val_acc = []

    def init_callback(self):
        self.callbacks.append(
            ModelCheckPoint(
                filepath=None,
                monitor=None,
                mode=None,
                saved_best_only=None,
                save_weights_only=None,
                verbose=None))

        self.callbacks.append(
            TensorBoard(
                log_dir=None,
                write_graph=None))

    def train(self):
        history = self.model.fit(
            self.data[0], self.data[1],
            epochs=None,
            verbose=None,
            batch_size=None,
            validation_split=None,
            callbacks=self.callbacks)

        self.loss.extend(history.history['loss'])
        self.acc.extend(history.history['acc'])
        self.val_acc.extend(history.history['val_loss'])
        self.val_acc.extend(history.history['val_acc'])
