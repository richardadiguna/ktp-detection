import os
import cv2
import numpy as np

from sklearn.model_selection import train_test_split


class DataLoader:
    def __init__(self, config):
        self.config = config
        self.height = config.height
        self.width = config.width

        if not os.path.isfile(config.dataset_path):
            self.create_data_txt(config.dataset_dir)

        self.get_dataset()

    def create_data_txt(self, dataset_dir):
        fnames = os.listdir(dataset_dir)

        def isdir(x):
            return os.path.isdir(os.path.join(dataset, x))

        dirnames = [name for name in fnames if isdir(name)]

        with open('dataset.txt', mode='w') as f:
            lines = []
            label = 0
            for idx, dir_ in enumerate(dirnames):
                # Change this conditional statement
                # if you have different class distribution
                if dir_ == 'Other':
                    label = 0
                elif dir_ == 'KTP':
                    label = 1

                images_path = os.listdir(os.path.join(dataset_dir, dir_))
                desc = 'Writing dataset.txt for input dataset'
                for path in tqdm(images_path, desc=desc):
                    if os.path.isfile(os.path.join(dataset_dir, dir_, path)):
                        fpath = os.path.join(dataset_dir, dir_, path)
                        line = ''.join(fpath + ' ' + str(label) + ' ' + '\n')
                        lines.append(line)

            random.shuffle(lines)
            for line in lines:
                f.write(line)

    def read_file_names(self, image_list_file):
        filenames = []
        with open(image_list_file, 'r') as f:
            for line in tqdm(f, desc=image_list_file):
                filenames.append(line)
        return filenames

    def read_images_from_disk(self, filenames):
        images = []
        labels = []

        for i in range(0, len(filenames)):
            img = cv2.imread(filenames[i])

            if img is None:
                print(filenames[i])
                continue

            if img.shape != (self.height, self.width):
                img = cv2.resize(img, (self.height, self.width))

            images.append(img)

        return images

    def get_dataset(self, dataset_path):
        if self.file_extension == '.txt':

            txt_data = self.read_file_names(dataset_path)

            X = [fname.split(' ')[0] for fname in txt_data]
            y = [fname.split(' ')[1] for fname in txt_data]

            self.X_train, self.X_val, self.y_train, self.y_val = \
                train_test_split(X, y, test_size=0.20)

        self.num_train = len(self.X_train)
        self.num_val = len(self.X_val)

    def get_train_data(self):
        x = read_images_from_disk(self.X_train)
        y = self.y_train
        return x, y

    def get_valid_data(self):
        x = read_images_from_disk(self.X_val)
        y = self.y_val
        return x, y
