# implicitly return None
def is_positive(num):
    return True if num > 0 else False


print(is_positive(0))


# python is dynamically typed, no need to specify type for parameter


def is_positive2(num):
    if num > 0:
        return True


print(is_positive2(0))


def default_param(num=1):
    return num + 1

print(default_param())
