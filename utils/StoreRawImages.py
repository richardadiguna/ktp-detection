import os
import cv2
import argparse


def store_raw_images(negtives_data_path, write_dir):
    fnames = os.listdir(negtives_data_path)

    for fname in fnames:
        full_path = os.path.join(negtives_data_path, fname)

        image = cv2.imread(full_path, cv2.IMREAD_GRAYSCALE)
        resized_images = cv2.resize(image, (100, 100))

        cv2.imwrite(write_dir + fname, resized_images)


if __name__ == '__main__':
    argparser = argparse.ArgumentParser(description=__doc__)
    argparser.add_argument(
        '-sp', '--savepath',
        default='None',
        help='Path directory of dataset')
    argparser.add_argument(
        '-wd', '--writedir',
        default='None',
        help='Path directory of store directory')
    args = argparser.parse_args()
    store_raw_images(args.savepath, args.writedir)
