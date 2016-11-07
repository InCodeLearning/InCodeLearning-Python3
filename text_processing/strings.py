# coding=utf-8
# CP-1252 Western European like French, Spanish, German. windows-1252
# ain't no such thing as "plain text"
# utf-16 byte order mask u+feff u+fffe, little/big endian
# utf-8 use exactly same byte ordering on big/little endians
# utf-8 uses 1 byte for ASCII, 2 for Latin, 3 for Chinese
import sys

s = '深入Python'
print(len(s))
print(s[0])

print('=====formatting strings=====')
print("{1}'s password is {0}".format("too short", "someone"))
si_suffixes = ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']
# compound field names, access data structures
print('1000{0[0]} = 1{0[1]}'.format(si_suffixes))

for (k, v) in sys.modules.items():
    print(k, ':', v)
print('1MB = 1000{0.modules[__main__].si_suffixes[0]}'.format(sys))

# format specifier, see format specification mini-language in python doc
print('{0:.1f} {1}'.format(698.255, 'GB'))
