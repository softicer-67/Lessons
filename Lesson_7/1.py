import os

path = 'my_project'
folders = ['settings', 'mainapp', 'adminapp', 'authapp']

for folder in folders:
    try:
        if not os.path.exists(folder):
            os.makedirs(os.path.join(path, folder))
            print(f'Добавлена папка: \\{folder}\\')
    except FileExistsError:
        print('')

