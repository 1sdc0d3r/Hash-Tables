# Your code here
import math
import random

cache = {}


def buildTable():
    for x in range(2, 14):
        for y in range(3, 6):
            if (x, y) not in cache:
                cache[(x, y)] = (
                    (math.factorial(math.pow(x, y)))//(x+y)) % 982451653


def slowfun_too_slow(x, y):
    # key = (x,y)
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653
    return v


def slowfun(x, y):
    # cache = {}
    # key = (x,y)
    # if key not in cache: #if key is not a key in the cache
    #     cache[key] = whatever _expensive_thing_here
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same output, but completes quickly instead of taking ages to run.
    """
    # Your code here
    buildTable()
    return cache[(x, y)]


# Do not modify below this line!
for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
