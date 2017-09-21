import os
import shutil

print os.getenv('PATHH')

os.getenv('HOME')

print(os.path.join(os.getenv('HOME'), 'foo.txt'))

print(os.path.expanduser("~/foo.txt"))

f = os.path.expanduser("~/foo.txt")

print(os.path.split(f))

os.remove()