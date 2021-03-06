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
        config = self.congig

        filepath = os.path.join(
            self.config.callbacks.checkpoint_dir, '.hdf5')

        self.callbacks.append(ModelCheckPoint(
            filepath=filepath,
            monitor=config.callbacks.checkpoint_monitor,
            mode=config.callbacks.checkpoint_mode,
            saved_best_only=config.callbacks.checkpoint_save_best_only,
            save_weights_only=config.callbacks.checkpoint_save_weights_only,
            verbose=config.checkpoint_verbose))

        self.callbacks.append(
            TensorBoard(
                log_dir=conf.callbacks.tensorboard_log_dir,
                write_graph=conf.callbacks.tensorboard_write_graph))

    def train(self):
        config = self.config
        history = self.model.fit(
            self.data[0], self.data[1],
            epochs=config.trainer.num_epochs,
            verbose=config.trainer.verbose_training,
            batch_size=config.trainer.batch_size,
            validation_split=config.traininer.validation_split,
            callbacks=self.callbacks)

        self.loss.extend(history.history['loss'])
        self.acc.extend(history.history['acc'])
        self.val_acc.extend(history.history['val_loss'])
        self.val_acc.extend(history.history['val_acc'])
