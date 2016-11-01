"""
LP1: to read and write file (mode:'r', 'w', 'a' or 'rb', encoding: 'utf-8'...)

if the file you read is miscoded,
the following code can help to figure the encoding mode
# import pkgutil
# import os
# import encodings
#
# def all_encodings():
#     modnames = set(
#         [modname for importer, modname, ispkg in pkgutil.walk_packages(
#             path=[os.path.dirname(encodings.__file__)], prefix='')])
#     aliases = set(encodings.aliases.aliases.values())
#     return modnames.union(aliases)
#
# filename = 'example.txt'
# encodings = all_encodings()
# for enc in encodings:
#     try:
#         with open(filename, encoding=enc) as f:
#             # print the encoding and the first 500 characters
#             print(enc, f.read(500))
#     except Exception:
#         pass

LP2 stream objects from non-file sources

"""
import gzip
import io
import sys

# read a .txt file
a_file = open('example.txt', encoding='gb2312')
# encoding might be different depends on the file you read.
print(a_file.read())
a_file.seek(0)
print(a_file.read(16))
print(a_file.read(1))
print(a_file.read(1))
print((a_file.tell()))
a_file.seek(18)
# a_file.read((1))
a_file.close()

# if file is closed, error will be raised as for following uses.
# a_file.seek(0)
# a_file.tell()
print(a_file.closed)

# Python call a_file.close() automatically when the with block ends.
line_number = 0
with open('example.txt', encoding='gb2312') as a_file:
    for a_line in a_file:
        line_number += 1
        print('{:>4} {}'.format(line_number, a_line.rstrip()))

with open('test.log', mode='w', encoding='utf-8') as b_file:
    b_file.write('test succeeded.')

with open('test.log', encoding='utf-8') as b_file:
    print(b_file.read())

with open('test.log', mode='a', encoding='utf-8') as b_file:
    b_file.write('\nand again.')

# open return an stream object with many methods
with open('test.log', encoding='utf-8') as b_file:
    print("stream object.name =" + a_file.name)
    print("stream object.encoding = " + a_file.encoding)
    print("stream object.mode = " + a_file.mode)

# read binary file.
with open('dog.jpg', mode='rb') as an_image:
    print(an_image.mode)
    print(an_image.name)
    print(an_image.tell())
    data = an_image.read(3)
    print(data)
    print(an_image.tell())
    an_image.seek(0)
    print(type(data))
    data = an_image.read()
    print(len(data))

# LP2: stream object
c_string = 'PapayaWhip is the new black.'

c_file = io.StringIO(c_string)
c_file.read()
c_file.seek(0)
print(c_file.read(10))
c_file.tell()

# io.StringIO treat a string as a .txt file;
# io.BytesIO treat a byte array as a binary file

# handling compressed files
# two popular non-windows compression schemes: gzip & bzip2

with gzip.open('out.log.gz', mode='wb') as z_file:
    z_file.write('A nine mile walk is no joke, especially in '
                 'the rain.'.encode('utf-8'))

with gzip.open('out.log.gz', mode='rb') as z_file:
    print(z_file.read())


# redirect stdout to a file
class RedirectStdoutTo:
    def __init__(self, out_new):
        self.out_new = out_new

    def __enter__(self):
        self.out_old = sys.stdout
        sys.stdout = self.out_new

    def __exit__(self, *args):
        sys.stdout = self.out_old

with open('out.log', mode='w', encoding='utf-8') as a_file:
    with RedirectStdoutTo(a_file):
        print(u'Stdout is redirected to a file')

# with open('out.log', mode='r') as a_file:
with open('out.log', encoding='utf-8') as a_file:
    print(a_file.read())
