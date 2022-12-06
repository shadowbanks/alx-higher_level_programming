#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new_list = my_list[:]
    my_list.clear()
    if idx < 0 or idx >= len(new_list):
        return new_list
    for i in new_list:
        if i == idx + 1:
            pass
        else:
            my_list.append(i)
    return my_list
