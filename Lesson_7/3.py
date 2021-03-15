import os

setting = 'my_project\\settings'
mainapp = 'my_project\\mainapp'
authapp = 'my_project\\authapp'
temp_app = 'my_project\\mainapp\\templates\\mainapp'
temp_authapp = 'my_project\\authapp\\templates\\authapp'

if not os.path.exists(setting):
    os.makedirs(setting)
    with open(f'{setting}\\__init__.py', 'w') as file:
        file.write('')
    with open(f'{setting}\\dev.py', 'w') as file:
        file.write('')
    with open(f'{setting}\\prod.py', 'w') as file:
        file.write('')

if not os.path.exists(mainapp):
    os.makedirs(mainapp)
    with open(f'{mainapp}\\__init__.py', 'w') as file:
        file.write('')
    with open(f'{mainapp}\\models.py', 'w') as file:
        file.write('')
    with open(f'{mainapp}\\views.py', 'w') as file:
        file.write('')

if not os.path.exists(temp_app):
    os.makedirs(temp_app)
    with open(f'{temp_app}\\base.html', 'w') as file:
        file.write('')
    with open(f'{temp_app}\\index.html', 'w') as file:
        file.write('')

if not os.path.exists(authapp):
    os.makedirs(authapp)
    with open(f'{authapp}\\__init__.py', 'w') as file:
        file.write('')
    with open(f'{authapp}\\models.py', 'w') as file:
        file.write('')
    with open(f'{authapp}\\views.py', 'w') as file:
        file.write('')

if not os.path.exists(temp_authapp):
    os.makedirs(temp_authapp)
    with open(f'{temp_authapp}\\base.html', 'w') as file:
        file.write('')
    with open(f'{temp_authapp}\\index.html', 'w') as file:
        file.write('')
