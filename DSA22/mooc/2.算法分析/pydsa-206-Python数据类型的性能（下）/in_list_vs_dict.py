import timeit
import random
for i in range(10000, 1000001, 20000):
    t = timeit.Timer(f"random.randrange({i}) in x", "from __main__ import random, x")
    x = list(range(i))
    lst_time = t.timeit(number=1000)
    x = {j:None for j in range(i)}
    d_time = t.timeit(number=1000)

    print(f"{i}, {lst_time:10.3f}, {d_time:10.3f}")