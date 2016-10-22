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

print([(os.stat(f).st_size, f) for f in glob.glob('*.py')])
