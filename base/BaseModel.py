class BaseModel:
    def __init__(self, config):
        self.config = config
        self.model = None

    def save(self, checkpoint_path):
        if self.model is None:
            raise Exception('You have to build the model first')

        print('Saving Model...')
        self.model.save_weights(checkpoint_path)
        print('Model saved')

    def load(self, checkpoint_path):
        if self.model is None:
            raise Exception('You have to build the model first')

        print('Loading model checkpoint {1} ...\n'.format(checkpoint_path))
        self.model.load_weights(checkpoint_path)
        print('Model loaded')
        return

    def build_model(self):
        raise NotImplementedError
