import os
import argparse


def create_pos_n_neg(dataset_dir, file_types):
    npath = os.path.join(dataset_dir, 'bg.txt')
    ppath = os.path.join(dataset_dir, 'info.dat')
    for file_type in file_types:
        fpath = os.path.join(dataset_dir, file_type)
        for img in os.listdir(fpath):
            if file_type == 'negative':
                line = 'negative' + '/' + img + '\n'
                with open(npath, 'a') as f:
                    f.write(line)
            elif file_type == 'positive':
                line = 'positive' + '/' + img + ' 1 0 0 50 50\n'
                with open(ppath, 'a') as f:
                    f.write(line)


if __name__ == '__main__':
    argparser = argparse.ArgumentParser(description=__doc__)
    argparser.add_argument(
        '-dr', '--datasetdir',
        default='None',
        help='Path directory of dataset')
    argparser.add_argument(
        '-ft', '--filetypes',
        nargs='+',
        default='None',
        help='Path directory of dataset')
    args = argparser.parse_args()
    create_pos_n_neg(args.datasetdir, args.filetypes)
