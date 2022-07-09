data_1 = [1, 2, 3, 2, 1]  # unique: 3
data_2 = [54, 90, 52, 10, 62, 54, 90, 52, 10, 62, 42]  # unique: 42


def find_unique(data):
    temp = {}
    for item in data:
        if temp.get(item) is None:
            temp[item] = 1
        else:
            temp[item] += 1
    return [item[0] for item in temp.items() if item[1] == 1][0]


print(find_unique(data_1))
print(find_unique(data_2))
