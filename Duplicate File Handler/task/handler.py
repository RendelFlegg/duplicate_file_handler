import argparse
import os
import hashlib

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
duplicates = {}
free_space = 0

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

answer = input('Check for duplicates?\n')
while answer.lower() not in ['yes', 'no']:
    print('\nWrong option')
    answer = input('\nCheck for duplicates?\n')

if answer.lower() == 'yes':
    counter = 1
    for key in keys:
        if len(folder_dictionary[key]) > 1:
            print(key, 'bytes')
            list_of_items = folder_dictionary[key]
            folder_dictionary[key] = {}
            for item in list_of_items:
                if item.endswith(f'{file_format}'):
                    item_hash = hashlib.md5()
                    with open(item, "rb") as f:
                        for chunk in iter(lambda: f.read(4096), b""):
                            item_hash.update(chunk)
                    if item_hash.hexdigest() not in folder_dictionary[key]:
                        folder_dictionary[key][item_hash.hexdigest()] = []
                    folder_dictionary[key][item_hash.hexdigest()].append(item)
            for hash_key in folder_dictionary[key]:
                if len(folder_dictionary[key][hash_key]) > 1:
                    print(f'Hash: {hash_key}')
                    for item in folder_dictionary[key][hash_key]:
                        if item.endswith(f'{file_format}'):
                            duplicates[str(counter)] = {'path': item, 'size': int(key)}
                            print(f'{counter}.', item)
                            counter += 1
            print()

    answer = input('Delete files?\n')
    while answer.lower() not in ['yes', 'no']:
        print('\nWrong option')
        answer = input('\nDelete files?\n')
    if answer.lower() == 'yes':
        file_numbers = set(input('\nEnter file numbers to delete:\n').split())
        while not file_numbers.issubset(set(duplicates.keys())) or not len(file_numbers):
            print('\nWrong format')
            file_numbers = set(input('\nEnter file numbers to delete:\n').split())
        for number in file_numbers:
            os.remove(duplicates[number]['path'])
            free_space += duplicates[number]['size']
        print(f'Total freed up space: {free_space} byte{"s" if free_space > 1 else ""}')

