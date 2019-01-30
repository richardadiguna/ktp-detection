import os
import argparse
import numpy as np


def get_args():
    argparser = argparse.ArgumentParser(description=__doc__)
    argparser.add_argument(
        '-c', '--config',
        metavar='C',
        default='None',
        help='The Configuration file')
    args = argparser.parse_args()
    return args


def store_raw_images(negtives_data_path, write_dir):
    fnames = os.listdir(negtives_data_path)

    for fname in fnames:
        full_path = os.path.join(negtives_data_path, fname)

        image = cv2.imread(full_path, cv2.IMREAD_GRAYSCALE)
        resized_images = cv2.resize(image, (100, 100))

        cv2.imwrite(write_dir + fname, resized_images)


def create_pos_n_neg():
    return
