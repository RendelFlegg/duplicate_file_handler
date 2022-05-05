import argparse
import os

parser = argparse.ArgumentParser(description="Let's parse some directory")
parser.add_argument('dir', nargs='?', type=str, default=False, help='Enter directory')
args = parser.parse_args()
directory = args.dir


def sorting(dictionary):
    print('Size sorting options:\n'
          '1. Descending\n'
          '2. Ascending\n')
    while True:
        user_sorting = input('Enter a sorting option:\n')
        if user_sorting not in ['1', '2']:
            print('Wrong option\n')
        else:
            user_choice = user_sorting == '1'
            return sorted(dictionary, reverse=user_choice)


folder_dictionary = {}

if os.path.isdir(directory):
    for root, dirs, files in os.walk(directory, topdown=False):
        for name in files:
            file_name = os.path.join(root, name)
            file_size = os.path.getsize(file_name)
            if file_size not in folder_dictionary:
                folder_dictionary[file_size] = []
            folder_dictionary[file_size].append(file_name)
else:
    print('Directory is not specified')

file_format = input('Enter file format:\n')
keys = sorting(folder_dictionary)

for key in keys:
    print(key, 'bytes')
    for item in folder_dictionary[key]:
        if item.endswith(f'{file_format}'):
            print(item)
    print()
