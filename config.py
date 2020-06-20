import os
import argparse
import json

def load_config(json_fn):
    with open(json_fn, 'r') as infile:
        config = json.load(infile)
    return config

def create_config(args):
    path = os.path.join('models',args['model_name'])
    if not os.path.exists(path):
        os.mkdir(path)
    with open(os.path.join(path,'config.json'), 'w') as outfile:
        json.dump(args, outfile)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Create a config JSON')

    #possible types/values

    parser.add_argument('model_name',
                        help='model name. will create a directory for model where config,data,etc will go')
    parser.add_argument('spec_type',
                        help='Spectrogram Type, cqt or logstft')
    parser.add_argument('init_lr', type=float,
                        help='Initial Learning Rate')
    parser.add_argument('lr_decay',
                        help='How the Learning Rate Will Decay')
    parser.add_argument('bin_multiple', type=int,
                        help='Used to calculate bins_per_octave')
    parser.add_argument('residual', type=bool,
                        help='Use Residual Connections or not')
    parser.add_argument('full_window',
                        help='Whether or not the convolution window spans the full axis')


    args = vars(parser.parse_args())

    create_config(args)
