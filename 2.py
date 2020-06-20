my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


def my_func(list_1):
    new_list = []
    for i in range(len(list_1) - 1):
        if list_1[i] < list_1[i + 1]:
            new_list.append(list_1[i + 1])
    return new_list


print(my_func(my_list))
