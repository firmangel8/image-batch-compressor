import pathlib
import os
import argparse
from PIL import Image


def flag_ok(value):
    return '\x1b[6;30;42m' + value + '\x1b[0m'


def main(path_input, path_output, width_target, height_target):
    wt = int(width_target)
    ht = int(height_target)
    maxsize = (wt, ht)
    if not os.path.exists(path_input):
        print('Not have folder input, please reserve it')
    for input_img_path in pathlib.Path(path_input).iterdir():
        if not os.path.exists(path_output):
            os.mkdir(path_output)
        output_img_path = str(input_img_path).replace(path_input, path_output)
        with Image.open(input_img_path) as im:
            im.thumbnail(maxsize)
            im.save(output_img_path, "JPEG", dpi=(300, 300))
            source = str(input_img_path)
            dest = str(output_img_path)
            flag = str(flag_ok("SAVED"))
            print(f'{source:<50s} {dest:<50s} {flag:<10s}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i", "--Input", help="Directory Input", default="input")
    parser.add_argument(
        "-o", "--Output", help="Directory Output", default="output")
    parser.add_argument("-ww", "--Width", help="Width target", default=500)
    parser.add_argument("-hh", "--Height",
                        help="Height target", default=500)
    args = parser.parse_args()
    main(args.Input, args.Output, args.Width, args.Height)
