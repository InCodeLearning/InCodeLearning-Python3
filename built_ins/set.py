""" Key word for set: unordered, unique value, any datatypes, curly bracket
    {} is a dict, not set, empty set expression set(), including no argument.
    two sets comparison: union, intersection, difference.
"""

s = set(i for i in range(5))
print(s, len(s))  # {0, 1, 2, 3, 4} 5
print(4 in s)  # True
print(5 in s)  # False

s.add("a")
s.add("python")
print(s, len(s))  # {0, 1, 2, 3, 4, 'a', 'python'} 7
s.add(4)
print(s, len(s))  # {0, 1, 2, 3, 4, 'a', 'python'} 7
s.update({2, 7, 9}, {5, "a", "C#"})
print(s, len(s))  # {0, 1, 2, 3, 4, 5, 7, 'C#', 9, 'a', 'python'} 11

s.discard(9)
s.discard(9)
print(s, len(s))  # {0, 1, 2, 3, 4, 5, 'python', 7, 'a', 'C#'} 10
s.remove(4)
print(s, len(s))  # {0, 1, 2, 3, 'python', 5, 7, 'C#', 'a'} 9
# s.remove(4)    raise KeyError

print(s.pop())  # 0
print(s.pop())  # 1
# print(s.pop("C#"))  raise TypeError, no argument needed in pop method.
s.clear()
print(s)  # set() empty set

"""  Common set operations: union(),  intersection(),
     symmetric_difference(), difference().
     The first three operations are symmetric.
"""
a = {1, 2, 5, 8}
b = {2, 4, 6, 9}
print(a.union(b), b.union(a))  # {1, 2, 4, 5, 6, 8, 9} {1, 2, 4, 5, 6, 8, 9}
print(a.intersection(b), b.intersection(a))  # {2} {2}
print(a.symmetric_difference(b), b.symmetric_difference(a))
# {1, 4, 5, 6, 8, 9} {1, 4, 5, 6, 8, 9}
print(a.difference(b), b.difference(a))  # {8, 1, 5} {9, 4, 6}

c = {2, 5}
print(c.issubset(a))  # True
print(c.issubset(b))  # False
print(a.issuperset(c))  # True
print(b.issuperset(c))  # False

""" Frozenset is immutable set, cannot use the methods which
will change its contents.
"""
d = frozenset({2, 5, 3, 7, 10})
print(d, len(d))   # frozenset({10, 3, 2, 5, 7}) 5
print(5 in d)     # True
print(a.union(d))  # {1, 2, 3, 5, 7, 8, 10}
print(a.difference(d))   # {8, 1}
print(d.difference(a))    # frozenset({10, 3, 7})
print(d.intersection(a))  # frozenset({2, 5})
print(a.intersection(d))   # {2, 5}
