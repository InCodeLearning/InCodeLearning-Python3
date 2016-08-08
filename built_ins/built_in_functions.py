# abs() returns magnitude for complex number
numbers = [-1, -2.3, complex(3, 4)]
for n in numbers:
    print(abs(n))

print(all(numbers))  # true if all elements are true
print(any([0, None]))  # true if any element is true

print(ascii("'中文Àabc"))  # use \x \U \u escapes
# \xhh hex value hh char
# \uxxxx 16 bit hex char
# \Uxxxxxxxx 32 bit hex value char
# https://docs.python.org/3/reference/lexical_analysis.html
print(repr("'中文Àabc"), repr([1, 2]))  # string representation
# a class can define __repr__()


class Person:
    def __init__(self, gender, age):
        self.gender = gender
        self.age = age

    def __repr__(self):
        return "[Person: " + self.gender + " " + str(self.age) + "]"

    def __index__(self):
        return self.age

Tom = Person("male", 34)
print(repr(Tom))

print(bin(10))
print(bin(Tom)) # use __index__ of object
