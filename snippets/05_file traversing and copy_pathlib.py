
import os
import errno
from shutil import copyfile
from pathlib import Path

# todo: rename filename
# todo: rename content

# os crawler
from numpy.distutils.conv_template import paren_repl

output_root = '../output'
target = 'to_here'

for path, directory, files in os.walk('../scaffolder/default_folder'):
    # path = root.split(os.sep)
    print(path, directory, files)
    root_directory = path.split('/', 3)[-1]
    print('root directory:', root_directory)

    for file in files:
        # get the path, etc
        # file_source_path = os.path.join(path, file)
        file_source_path = Path(path, file)

        if root_directory == 'default_folder':
            # file_dest_path = os.path.join(output_root, target, file)
            file_dest_path = Path(output_root, target, file)
        else:
            # file_dest_path = os.path.join(output_root, target, root_directory, file)
            file_dest_path = Path(output_root, target, root_directory, file)

        print('source:', file_source_path)
        print('dest:', file_dest_path)


        # todo: process the file

        # make sure that directory is exist
        if not file_dest_path.exists():
            try:
                os.makedirs(os.path.dirname(file_dest_path))
                # file_dest_path.mkdir(file_dest_path.parent, exist_ok=True)
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise

        # copy
        copyfile(file_source_path, file_dest_path)

    print()