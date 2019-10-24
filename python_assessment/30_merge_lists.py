def linear_merge(list1, list2):
    res = []
    while list1 != [] and list2 != []:
        if list1[0] < list2[0]:
            res.append(list1.pop(0))
        else:
            res.append(list2.pop(0))
    while list1 != []:
        res.append(list1.pop(0))
    while list2 != []:
        res.append(list2.pop(0))
    return res
