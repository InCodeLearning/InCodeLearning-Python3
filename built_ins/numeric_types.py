# Boolean


# class must be defined before use
class UserDefined1:
    def __bool__(self):
        return False


# class name should use camel cases like Java...
class UserDefined2:
    # class user_defined1:
    def __len__(self):
        return 0

# Any object can be tested for truth, following are considered false.
if (not (None or False or
         0 or 0j or 0.0 or  # pep8 aligning to opening parenthesis
         '' or () or [] or
         {} or
         UserDefined1() or UserDefined2())):
    print("hello all the False's, everything else is True.")

# legacy from python 2 True=1 False=0
logic_ops = {
    "True + True": True + True,
    "True - False": True - False,
    "True * 3": True * 3,
    # True/False division by zero Error
}

for k, v in logic_ops.items():
    print('  ', '{:<13}={:>6}'.format(k, v))


# comparison operators <, >, <=, >=,  ==, !=. In C, == and != has less
# precedence than the other 4. In python, all same, which has less precedence
# than arithmetic, bitwise, shifting operations.
# C precedence http://en.cppreference.com/w/c/language/operator_precedence
# Use parentheses when not sure.

A = 3
B = 6
C = 32

print(8, A == 3 < B)  # false in C, True in python
print(9, B != 8)
print(10, A > B)
print(11, A + B < C)

# other functions that return boolean

D = 'abcdef'
print(12, 'a' in D)
print(13, 'h' not in D)
print(14, '' in D)
print(15, 'abcdef' is D)
print(16, 'abcd' is not D)
# TODO: isinstance, issubclass
# TODO: string methods: tring methods, isslnum, isalpha, isdecimal, .etc

# "rich comparison"  special methods


def __eq__(self, other):
    return not self < other and not other < self


def __ne__(self, other):
    return self < other or other < self     # return not self == other


def __lt__(self, other):
    return self < other


def __le__(self, other):
    return not self > other


def __gt__(self, other):
    return other < self


def __ge__(self, other):
    return not self < other

p1 = 3
p2 = 4
print(21, p1.__lt__(p2))    # calls int.__lt__()
print(22, __lt__(p1, p2))   # calls __lt__()
print(23, __le__(p1, p2))
print(24, __eq__(p1, p2))
print(25, __ne__(p1, p2))
print(26, __gt__(p1, p2))
print(27, __ge__(p1, p2))