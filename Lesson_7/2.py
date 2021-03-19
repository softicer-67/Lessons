import os
from collections import defaultdict
from os.path import relpath


root_dir = os.walk(r'D:/DISTRIB/')
for dirs in root_dir:
    print(dirs)