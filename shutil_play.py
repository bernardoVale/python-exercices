import shutil
import os


def cat(path, mode='r'):
    with open(path, mode=mode) as reader:
        print(reader.read())

home = os.path.expanduser("~")
file_name = "foo.txt"

full_path = os.path.join(home, file_name)

#cat(full_path)


# for i in range(10):
#     path = os.path.join("tmp", "{}.tmp".format(i))
#     with open(path, mode='w') as writer:
#         writer.write("file %d" % i)

#os.mkdir('/tmp/backup_folder')
#shutil.copytree('tmp', dst='/tmp/backup_folder2')

print os.listdir('/tmp/backup_folder2')
