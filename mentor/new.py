def unpacking(spisok):
    new_list = []
    for items in spisok:
        if isinstance(items, list):
            for item in unpacking(items):
                new_list.append(item)
        else:
            new_list.append(items)
    return new_list


spisok = [1, [2, 3], [4, [5, 6]]]
print(unpacking(spisok))