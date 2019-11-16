import os

"""
Script by Jarred Vardy <jarred.vardy@gmail.com>.
Intended for internal within the IBDocuments team.

Run this script in the same directory as the top-level directory of 'source_directory'. Like so:
 .
 ├── script.py
 └── source
"""

# START CONFIG

source_directory = "source"
output_directory = "output"
debug = False

# END CONFIG

absolute_path_source = os.path.abspath(source_directory)
absolute_path_output = os.path.abspath(output_directory)

if debug:
    common_prefix = os.path.commonprefix([os.path.abspath(source_directory), os.path.abspath(output_directory)])
    print('Absolute path of source dir: ' + absolute_path_source)
    print('Absolute path of output dir: ' + absolute_path_output)
    print('Common prefix of source and output dirs: ' + common_prefix)

for path, dirs, files in os.walk(absolute_path_source):
    if debug:
        print('Stepped into: ' + path)
        if next(os.scandir(path), sentinel) is sentinel:
            print('  Empty directory found: %s' % path)
            print('')
        else:
            print('  Directories within: %s' % dirs)
            print('  Files within: %s' % files)
            print('')
    for filename in files:
        new_filepath_dir = os.path.join(absolute_path_output, path.replace(absolute_path_source, '')[1:])
        new_filepath = os.path.join(new_filepath_dir, filename)
        if debug:
            print('    Filename: %s' % filename)
            print('    Reduced path: %s' % path.replace(absolute_path_source, ''))
            print('    Final destination: %s' % new_filepath)
            print('')
        os.makedirs(os.path.dirname(new_filepath), exist_ok=True)
        with open(new_filepath, "w") as f:
            f.write('')
