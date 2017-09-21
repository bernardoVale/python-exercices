import shutil
import sys
import os
import tempfile
from datetime import datetime
try:
    dir = sys.argv[1]
except IndexError:
    print('File not found')
folder = tempfile.mkdtemp()
for root, dirs, files in os.walk(dir):
    if not 'git' in root:
        for file in files:
            full_path = os.path.join(root, file)
            mod_time = datetime.fromtimestamp(os.stat(full_path).st_mtime)
            delta = datetime.now() - mod_time
            if delta.days >= 4:
                shutil.copy(full_path, folder)
shutil.make_archive('backup2', format='zip', root_dir=folder)
print(os.listdir(folder))
shutil.rmtree(folder)
