"""
Declaring a function.
Function related knowledge points.
"""


def is_positive(num):
    """ Identify whether an integer is positive or not."""
    return True if num > 0 else False

print(is_positive(0))


# python is dynamically typed, no need to specify type for parameter
def is_positive2(num):
    """Implicitly returns None."""
    if num > 0:
        return True

print(is_positive2(0))


# optional parameter with default value must be at right/end
# def add_or_minus(num1, add=True, num2): SyntaxError
def add_or_minus(num1, num2, add=True):
    """Add or subtract two numbers with optional boolean param."""
    return num1 + num2 if add else num1 - num2

print(add_or_minus(1, 2))
# keyword argument must be at right/end
# print(add_or_minus(add=False, 1, 2)) SyntaxError
# benefit can swap positions with keywords
print(add_or_minus(num2=2, num1=1, add=False))


# multiple arguments
def multiple_args(*args):
    print("called with", len(args), "arguments:", args)
    total = 0
    for num in args:
        total += num
    print("sum =", total)
    return total

multiple_args(1)
multiple_args(1, 2, 3, 4, 5)


# multiple arguments and keyword arguments
def multiple_key_args(*args, **kwargs):
    length = len(args)
    if 'limit' in kwargs.keys():
        length = kwargs['limit']
    total = 0
    for i in range(0, length):
        total += args[i]
    return total

print(multiple_key_args(1, 2, 3, 4, 5, nolimit=None, random=333))
print(multiple_key_args(1, 2, 3, 4, 5, limit=3))
