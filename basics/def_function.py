# implicitly return None
def isPositive(num):
    return True if num > 0 else False
print(isPositive(0))
# python is dynamically typed, no need to specify type for parameter
def isPositive2(num):
    if num > 0:
        return True
print(isPositive2(0))