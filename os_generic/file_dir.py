# DIP3 chapter3

import os
import glob
import time

print('current working directory', os.getcwd())
os.chdir('..')
print('current working directory', os.getcwd())

# python adds slash \ or / depending on os
print(os.path.join('..', 'pep8_recursive.py'))
print(os.path.join('../', 'pep8_recursive.py'))

print(os.path.expanduser('~'))

pathname = os.path.join(os.getcwd(), 'file_dir.py')
dirname, filename = os.path.split(pathname)
print('dir', dirname)
print('filename', filename)
shortname, extension = os.path.splitext(filename)
print('shortname', shortname)
print('extension', extension)

os.chdir('InCodeLearning-Python3')
print(glob.glob('*.py'))

print("======getting file metadata======")
# modification time
metadata = os.stat('pep8_recursive.py')
print(time.localtime(metadata.st_mtime))
print(metadata.st_size)  # in bytes
print(os.path.realpath('pep8_recursive.py'))   # absolute file path
