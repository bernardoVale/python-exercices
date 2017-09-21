import os
from os.path import join, getsize

output = {}

for root, dirs, files in os.walk('.'):
    if not 'git' in root:
        for file in files:
            _,ext = os.path.splitext(file)
            output[ext] = output.get(ext, 0) + 1

    output['directory'] = output.get('directory', 0) + len(dirs)

print(output)


import shutil

shutil.make_archive()