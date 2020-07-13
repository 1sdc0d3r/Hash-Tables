data = [None] * 15  # 15 Slots


def hashing_func(s):
    string_bytes = s.encode()
    total = 0

    for b in string_bytes:
        total += b

    return total


# print(hashing_func("string"))


def get_slot(s):
    hash_value = hashing_func(s)
    return hash_value % len(data)


# print(get_slot("golden"))
# print(get_slot("trout"))
# print(get_slot("bear"))  # collision w/ wolf
# print(get_slot("wolf"))  # collision w/ bear
# print(get_slot("eagle"))


def put(key, value):
    slot = get_slot(key)
    data[slot] = value
    # data[slot] = HashTableEntry(key, value)


put("golden", 1)
put("trout", 2)
put("bear", 3)
put("wolf", 4)  # overides data position of bear
put("eagle", 5)
print(data)


def get(key):
    slot = get_slot(key)
    hash_entry = data[slot]
    if hash_entry is not None:
        # return hash_entry.value
        return hash_entry
    return None
    # return data[slot]


print(get("golden"))
print(get("trout"))
print(get("coffee"))


def delete(key):
    put(key, None)


delete("bear")
print(get("bear"))
