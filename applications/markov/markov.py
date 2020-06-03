import random

# Read in all the words in one go
with open("input.txt", "r") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
cache = {}
words = words.lower().strip().split()
for i in range(len(words)-1):
    key = words[i]
    if key not in cache:
        # print(True)
        cache[key] = [words[i+1]]
    else:
        # print(False)
        cache[key].append(words[i+1])
# print(cache)


# TODO: construct 5 random sentences
# Your code here
sentences = [str()]*5
paragraph = str()

for i in range(len(sentences)):
    nWord = random.choice(
        [word for word in words if word[0] == "\"" or word[1].isupper()])
    while True:
        sentences[i] += f"{nWord} "
        if nWord[-1] in [".", "?", "!"]:
            cap = sentences[i][1:].capitalize()
            sentences[i] = f"\"{cap}"
            paragraph += f"{sentences[i].strip()}\""
            break
        nWord = random.choice(cache[nWord])

print(paragraph)
