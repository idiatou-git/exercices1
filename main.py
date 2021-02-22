def tableau(first, second):
    tab = []

    for elem in first:
        if elem not in second:
            if elem not in tab:
                tab.append(elem)
    #
    for elem in second:
        if elem not in first:
            if elem not in tab:
                tab.append(elem)

    return tab;


#
result = tableau([2, 4, 7, 8, 2], [1, 3, 9, 4, 6, 7])
print(result)