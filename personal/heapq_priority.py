# priority queue

# A priority queue is an abstract data type (ADT) which is like a regular queue or stack data structure,
#  but where additionally each element has a priority associated with it.
try:
    import Queue as Q  # ver. < 3.0
except ImportError:
    import queue as Q
q = Q.PriorityQueue()
q.put((10, 'ten'))
q.put((1, 'one'))
q.put((5, 'five'))
while not q.empty():
    print q.get(),  # the "," can concanate the resuit to one line

# heapq :

# binary trees for which every parent node has a value less than or equal to any of its children.
# This implementation uses arrays for which heap[k] <= heap[2*k+1] and heap[k] <= heap[2*k+2] for all k,
# counting elements from zero.
#
# basic functions:
#
# heapq.heappush(heap, item)

#
# Push the value item onto the heap, maintaining the heap invariant.
#
# heapq.heappop(heap)
#
# Pop and return the smallest item from the heap, maintaining the heap invariant.
# If the heap is empty, IndexError is raised. To access the smallest item without popping it, use heap[0].
import heapq


def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]


print heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
#
#     heapq.heappushpop(heap, item)
#
# Push item on the heap, then pop and return the smallest item from the heap.
# The combined action runs more efficiently thanheappush() followed by a separate call to heappop().
#

import heapq


def heapsort(iterable):
    heapq.heapify(iterable)
    return heapq.heappop(iterable)


print heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
# heapq.heapify(x)
#
# Transform list x into a heap, in-place, in linear time.
#
