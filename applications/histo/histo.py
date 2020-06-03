from string import ascii_letters
with open("robin.txt", "r") as f:
    robin = f.read()

cache = {}


def word_count(s):
    # Your code here
    s = s.lower().strip().split()
    for i in range(len(s)):
        key = ''.join(c for c in s[i] if c not in '\,.-+=/|[]{}()*^&"')
        if key not in cache:
            cache[key] = 1
        else:
            cache[key] = cache[key]+1


word_count(robin)
cache = sorted(cache.items())
cache = sorted(cache, key=lambda kv: kv[1])
for x in cache:
    print(f"{x[0]}: {'*'*x[1]}")
