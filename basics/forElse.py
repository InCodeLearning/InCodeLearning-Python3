# usage of for else

from math import sqrt

for n in range(1, 100):
    t = int(sqrt(n))
    for m in range(2, t + 1):
        if n % m == 0:
            break
    else:
        print(n)
