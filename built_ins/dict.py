"""A dictionary(dict) is unordered set of key-value pairs.
   the only standard mapping type.
   LP1: create a dict
        {} is empty dict
        dict key should be hashable types, otherwise raise TypeError.
        dict value can be any types.
        dict is not hashable type.
   LP2: look up a dict value by its key
   LP3: dict methods
        delete k-v pair, add k-v pair, change k-v pair

"""

# LP1 and LP2
d = {(1,): 1,
     '2nd': 2, 3: [3, 3.0],
     'pybook': 'diveinpy3',
     frozenset({4, 5}): {4, '5th'}}
print(d)
print(d[(1,)])    # 1
print(d['2nd'])    # 2
print(d[3])    # [3, 3.0]
print(d[frozenset({4, 5})])    # {'5th', 4}

# LP3
#  delete k-v pair method, no remove method
del d['pybook']
print(d)    # {3: [3, 3.0], '2nd': 2, (1,): 1, frozenset({4, 5}): {'5th', 4}}
print(d.pop(frozenset({4, 5})))    # {'5th', 4}
# unlike list & set,dict pop() need one argument
print(d)    # {3: [3, 3.0], '2nd': 2, (1,): 1}
# d.remove(3)   raise AttributeError

# add k-v pair, no append(), extend() method, mapping type reason?
d['4th'] = 4
print(d)    # {3: [3, 3.0], '2nd': 2, (1,): 1, '4th': 4}

# change k-v pair
d['4th'] = 'four'
print(d)    # {3: [3, 3.0], '2nd': 2, (1,): 1, '4th': 'four'}

# other methods
print(len(d))    # 4
print(2 in d)    # False, 2 is value not key
print('2nd' in d)    # True
print(d.keys())    # dict_keys([3, (1,), '2nd', '4th'])
print(d.values())    # dict_values([[3, 3.0], 'four', 1, 2])
print(d.items())
# dict_items([(3, [3, 3.0]), ('2nd', 2), ((1,), 1), ('4th', 'four')])
d1 = d.copy()    # shallow copy
d['4th'] = 4
print(d)     # {3: [3, 3.0], (1,): 1, '2nd': 2, '4th': 4}
print(d1)    # {3: [3, 3.0], '4th': 'four', '2nd': 2, (1,): 1}
print(d.get('4th'))   # 4   TODO make sure whether is d.get(key) same as d[key]
print(d.popitem())    # (3, [3, 3.0])   TODO find out pop order
print(d.get(5))     # None, default default is None
d.setdefault(5, '5th')
print(d.get(5))    # 5th
d2 = {6: '6th'}
print(d.update(d2))
# None  Pay attention, d.update() is None; d change to merge dict with d2
d.update(d2)
print(d)    # {'4th': 4, (1,): 1, 6: '6th', '2nd': 2, 5: '5th'}
d.pop(5)
print(d.get(5))    # None, if key is deleted, default to None
print(d.clear())    # None
print(d)    # {}, empty dict
