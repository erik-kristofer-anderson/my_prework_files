def sort_last(tuples):
    tuples = list(tuples)
    tuples.sort(key = lambda t: t[-1])
    return tuples

print(sort_last([(1, 3),(2, 1),(3, 2)]))
