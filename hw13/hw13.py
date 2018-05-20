import os

def walking(start_path):
    max_files = 0
    max_folder_root = ''
    for root, dirs, files in os.walk(start_path):
        if len(files) > max_files:
            max_files = len(files)
            max_folder_root = root
    return max_files, max_folder_root

max_files, max_folder_root = walking('.')
if max_folder_root == '.':
    print('Больше всего файлов ({}) лежит в корневой директории.'.format(max_files))
else:
    folder_name = max_folder_root.split('\\')[-1]
    print('Больше всего файлов ({}) лежит в папке {}. Путь к ней: {}.'.format(max_files, folder_name, max_folder_root))