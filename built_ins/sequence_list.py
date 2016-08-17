# C source https://github.com/python/cpython/blob/master/Include/listobject.h
# dynamic array, not linked list
# using list as a queue, not efficient
queue = [0, 1, 2, 3, 4]
queue.append(5)
queue.append(6)
print(queue)
queue.pop(0)
print(queue)  # elements 1-6 shifted left by one O(n) time
