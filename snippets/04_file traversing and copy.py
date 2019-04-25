
import os
import errno
from shutil import copyfile

# os crawler

output_root = '../output'
target = 'to_here'

for path, directory, files in os.walk('../scaffolder/default_folder'):
    # path = root.split(os.sep)
    print(path, directory, files)
    root_directory = path.split('/', 3)[-1]
    print('root directory:', root_directory)

    for file in files:
        # get the path, etc
        file_source_path = os.path.join(path, file)
        if root_directory == 'default_folder':
            file_dest_path = os.path.join(output_root, target, file)
        else:
            file_dest_path = os.path.join(output_root, target, root_directory, file)

        print('source:', file_source_path)
        print('dest:', file_dest_path)

        # process the file

        # make sure that directory is exist
        if not os.path.exists(os.path.dirname(file_dest_path)):
            try:
                os.makedirs(os.path.dirname(file_dest_path))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise

        # copy
        copyfile(file_source_path, file_dest_path)

    print()