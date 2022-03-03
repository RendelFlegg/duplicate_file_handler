import argparse
import os

parser = argparse.ArgumentParser(description="Let's parse some directory")
parser.add_argument('dir', nargs='?', type=str, default=False, help='Enter directory')
args = parser.parse_args()
directory = args.dir

if os.path.isdir(directory):
    for root, dirs, files in os.walk(directory, topdown=False):
        for name in files:
            print(os.path.join(root, name))
else:
    print('Directory is not specified')

