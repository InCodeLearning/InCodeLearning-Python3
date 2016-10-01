# https://docs.python.org/3.6/library/itertools.html#module-itertools
# These functions return iterators, which make looping more efficient
from itertools import product, permutations

# itertools.product()
# ===================

# itertools.product(*iterables, repeat = 1)
# computes the cartesian product of input iterables,
# which is equivalent to nested for-loops

A = [1, 2]
B = [3, 4]

print(product(A, B))
print(((x, y) for x in A for y in B))

# prints
# <itertools.product object at 0x7fdf0cc9f1f8>
# <generator object <genexpr> at 0x7fdf0c4054c0>

print(*product(A, B))
print(*((x, y) for x in A for y in B))
# *iterable (like list, tuple) returns each element in the iterable

# prints
# (1, 3) (1, 4) (2, 3) (2, 4)
# (1, 3) (1, 4) (2, 3) (2, 4)

print(*product(A, repeat=2))
# prints
# (1, 1) (1, 2) (2, 1) (2, 2)

print(list(product(A, repeat=2)))
# prints
# [(1, 1), (1, 2), (2, 1), (2, 2)]

print(*product(A, repeat=3))
# prints
# (1, 1, 1) (1, 1, 2) (1, 2, 1) (1, 2, 2)
# (2, 1, 1) (2, 1, 2) (2, 2, 1) (2, 2, 2)

C = [[1, 2, 3], [3, 4, 5]]

print(*product(*C))
# prints
# (1, 3) (1, 4) (1, 5) (2, 3) (2, 4) (2, 5) (3, 3) (3, 4) (3, 5)


# itertools.permutations()
# ========================

# itertools.permutations(iterable, r=None)
# returns successive r length permutations of
# elements in an iterable.

print(permutations(list("ABC")))
# prints
# <itertools.permutations object at 0x7fdf0c405468>

# if r not specified, then r defaults to
# the lenght of the iterable
print(*permutations(list("ABC")))
# prints
# ('A', 'B', 'C') ('A', 'C', 'B') ('B', 'A', 'C')
# ('B', 'C', 'A') ('C', 'A', 'B') ('C', 'B', 'A')

# compare product to permutation
two_letters = list("AB")
print(*product(two_letters, repeat=2))
print(*permutations(two_letters))

# permutations are printed in a lexicographic
# sorted order.
print(*permutations(list("ACB"), 2))
# prints
# ('A', 'C') ('A', 'B') ('C', 'A') ('C', 'B') ('B', 'A') ('B', 'C')

# if the input is in order, the permutation
# tuples will be producted in a sorted order
print(*permutations(list("ABC"), 2))
# prints
# ('A', 'B') ('A', 'C') ('B', 'A') ('B', 'C') ('C', 'A') ('C', 'B')
