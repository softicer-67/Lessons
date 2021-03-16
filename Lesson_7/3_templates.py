import os
import shutil

mainapp = 'my_project\\mainapp\\templates'
authapp = 'my_project\\authapp\\templates\\authapp'
templates = 'my_project\\templates'

if os.path.exists(mainapp):
    shutil.move(mainapp, templates)
    shutil.move(authapp, templates)



