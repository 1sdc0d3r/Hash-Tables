import math

'''
    key = (x, y)
    if key not in cache:
        cache[key] = slowfun_too_slow(x, y)

    return cache[key]
'''


# Inverse square root
# inv_sqrt(x) = 1/sqrt(x)

inv_sqrt = {}


def build_lookup_table():
    for i in range(1, 1000):
        inv_sqrt[i] = 1 / math.sqrt(i)


build_lookup_table()

print(inv_sqrt[2])
print(inv_sqrt[12])
