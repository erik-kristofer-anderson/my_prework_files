def front_x(words):
    words.sort()
    res = []
    for word in words:
        if word[0] == 'x':
            res.append(word)
    for word in words:
        if word[0] != 'x':
            res.append(word)
    return res

words = ["mix", "xyz", "apple", "xanadu", "aardvark"]

print(front_x(words))