def swap_first_last():
    my_list = input("Введите текст ")
    my_list = my_list.split()
    t = list(my_list)
    print(t)
    if t == []:
        return []
    else:
        my_list[-1], my_list[0] = my_list[0], my_list[-1]
        return my_list


my_list = swap_first_last()
print(my_list)
