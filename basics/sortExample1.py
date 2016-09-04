# the usage of key in sort functions

import collections


def count_words(s, n):
    lst = collections.Counter(s.split()).most_common()
    lst.sort(key=lambda t: (-t[1], t[0]))
    return lst[:n]


print(count_words("betty bought a bit of butter but the butter was bitter", 3))

# another example  key order in sorted function

s = 'asdf234GDSdsf23'
keyfunc = lambda x: (x.isdigit(), x.isdigit() and int(x) % 2 == 0, x.isupper(), x.islower(), x)
print("".join(sorted(s, key=keyfunc)))

s = 'asdf234GDSdsf23'
keyfunc = lambda x: (not x.islower(), not x.isupper(), not (x.isdigit() and int(x) % 2 == 1), x)
print("".join(sorted(s, key=keyfunc)))

# def show(s):
#     for x in s:
#         print((x.isdigit(), x.isdigit() and int(x) % 2 == 0, x.isupper(), x.islower(), x))
#
#
# print('key=x')
# s = sorted(s, key=lambda x: x)
# show(s)
#
# print('key=islower()')
# s = sorted(s, key=lambda x: x.islower())
# show(s)
#
# print('key=isupper()')
# s = sorted(s, key=lambda x: x.isupper())
# show(s)
#
# print('key=isdigit() and int(x)%2==0')
# s = sorted(s, key=lambda x: x.isdigit() and int(x) % 2 == 0)
# show(s)
