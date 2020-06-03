from string import ascii_letters


def word_count(s):
    # Your code here
    cache = {}
    s = s.lower().strip("").split()
    # print(s)
    allow = ascii_letters + "'"
    # print(allow)
    for i in range(len(s)):
        key = ''.join(filter(allow.__contains__, s[i]))
        if key not in cache:
            cache[key] = 1
        else:
            cache[key] = cache[key]+1
    return cache


if __name__ == "__main__":
    # print(word_count(""))
    # print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    # print(word_count(
    #     'This is a test of the emergency broadcast network. This is only a test.'))
