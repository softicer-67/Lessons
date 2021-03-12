import os

try:
    dir_name = '--my_project'
    folders = ['--settings', '--mainapp', '--adminapp', '--authapp']
    for folder in folders:
        os.makedirs(os.path.join(dir_name, folder))
except FileExistsError:
    print('\nТакая папка уже существует!')
