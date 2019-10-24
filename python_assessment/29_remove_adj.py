def remove_adjacent(nums):
    prev = None
    res = []
    for num in nums:
        if num != prev:
            res.append(num)
        prev = num
    return res





print(remove_adjacent([1, 2, 2, 3]))
