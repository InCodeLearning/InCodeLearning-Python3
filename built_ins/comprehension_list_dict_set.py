import os
import glob

# mapping one list into another
a_list = [1, 2, 3]
# safe to assign result to original var, python constructs copy in memory
a_list = [elem * 2 for elem in a_list]
print([os.path.realpath(f) for f in glob.glob('*.py')])

# filter list items, find primes < 50
nums = range(2, 50)
print(*nums)
for i in range(2, 8):
    nums = [num for num in nums if num == i or num % i]
    print('after {}th loop, nums is {}'.format(i, nums))

# tuples can often be created without parentheses, but not here
print([(os.stat(f).st_size, f) for f in glob.glob('*.py')])

# nested for loops
vec1 = [2, 4, 6]
vec2 = [-1, 0, 1]
print('Cartesian product', [x * y for x in vec1 for y in vec2])
print('Cartesian sum', [x + y for x in vec1 for y in vec2])
print('sequence product', [vec1[i] * vec2[i] for i in range(len(vec1))])

# apply to complex expression and nested function
print([str(round(355/113, i)) for i in range(1, 6)])

matrix = [
          [1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
         ]
print('transpose', [[row[i] for row in matrix] for i in [0, 1, 2]])
print(list(zip(*matrix)))  # equivalent built-in zip function

print("======dict comprehension======")
a_dict = {'a': 1, 'b': 2, 'c': 3}
print({value: key for key, value in a_dict.items()})  # value must be hashable

print("======set comprehension======")
print({x ** 2 for x in a_list})
print({x for x in range(10) if x % 2 == 0})
print({2 ** x for x in range(10)})
