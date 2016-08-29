""" Case is sensitive in python. so there are two booleans: True and False
It can be assigned as boolean value,, also can be writen as expressions.
None, False, 0, 0.0, 0j, empty sequence or mapping, such as '', (), [], {}
"""
a = 0
print(1, bool(a))
b = None
print(2, bool(b))
c = []
print(3, bool(c))
d = {}
print(4, bool(d))
e = False
print(5, bool(e))
f = 1
print(6, bool(f))
g = True
print(7, bool(g))

"""comparison operators: <, >, <=, >=,  =, !=,
Unlike C, all comparison operations in Python have the same priority,
which is lower than that of any arithmetic,
shifting or bitwise operation.
when you are not sure about the priority, you can use parentheses ().
"""
A = 3
B = 6
C = 32

print(8, A == 3)
print(9, B != 8)
print(10, A > B)
print(11, A + B < C)

""" related functions (the return value is boolean),
such as, is, is not, in, not in etc.
built-in funcitons: isinstance, issubclass
string methods, isslnum, isalpha, isdecimal, isdigit, islower,
isupper, isspace, istitle......, start with is***.
"""
D = 'abcdef'
print(12, 'a' in D)
print(13, 'h' not in D)
print(14, '' in D)  # empty string returns True all the time.
print(15, 'abcdef' is D)
print(16, 'abcd' is not D)

"""logical operators: and, or, not;
short circuit (F or T --> T; T or F --> T; T or T --> T; F or F --> F);
(T and T --> T; T and F --> F; F and T --> F; F and F --> T)
(not T --> F; not F --> T)
"""
print(17, A > B or A < C)
print(18, A > B and A < C)
print(19, not A > B)
print(20, not(A > B or A < C))


# "rich comparison"  special methods object.__lt__(first, second)
#   __le__, __eq__, __ne__, __gt__, __ge__,


def __eq__(first, second):
    return not first < second and not second < first


def __ne__(first, second):
    return first < second or second < first     # return not first == other


def __lt__(first, second):
    return first < second


def __le__(first, second):
    return not first > second


def __gt__(first, second):
    return second < first


def __ge__(first, second):
    return not first < second

p1 = 3
p2 = 4
#  print(21, p1.__lt__(p2))
print(22, __lt__(p1, p2))
print(23, __le__(p1, p2))
print(24, __eq__(p1, p2))
print(25, __ne__(p1, p2))
print(26, __gt__(p1, p2))
print(27, __ge__(p1, p2))
