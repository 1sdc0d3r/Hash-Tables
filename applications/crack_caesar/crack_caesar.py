from string import ascii_uppercase
# Use frequency analysis to find the key to ciphertext.txt,#  and then
# decode it.
decode = {
    "E": 11.53, "T": 9.75, "A": 8.46, "O": 8.08, "H": 7.71, "N": 6.73, "R": 6.29, "I": 5.84, "S": 5.56, "D": 4.74, "L": 3.92, "W": 3.08, "U": 2.59, "G": 2.48, "F": 2.42, "B": 2.19, "M": 2.18, "Y": 2.02, "C": 1.58, "P": 1.08, "K": 0.84, "V": 0.59, "Q": 0.17, "J": 0.07, "X": 0.07, "Z": 0.03}

# Your code here
with open("ciphertext.txt", "r") as f:
    code = f.read()

cache = {}
count = 0
decoded = str()
cypher = {}
for c in [c for c in code if c in ascii_uppercase]:
    count += 1
    if c not in cache:
        cache[c] = 1
    else:
        cache[c] += 1

cache = dict(sorted(cache.items(), key=lambda kv: kv[1], reverse=True))
# print(cache)
for c in code:
    if c in cache:
        for key, value in decode.items():
            if round((cache[c]/count*100), 2) == value:
                decoded += key
                if key not in cypher:
                    cypher[key] = c
    else:
        decoded += c

print(decoded, cypher)
