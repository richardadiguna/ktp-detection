from dataloader.DataLaoder import DataLaoder
from model.CNN import ConvNet
from train.Trainer import Trainer
from utils.Parser import process_config
from utils.Utils import get_args


def Main():
    try:
        args = get_args()
        config = process_config(args.config)
    except RuntimeError:
        print('Missing or invalid arguments')
        exit(0)


if __name__ == '__main__':
    main()
