#!/usr/bin/python3

def remove_char_at(str, n):
    copy = ""
    for i in range(len(str)):
        if i == n:
            continue
        else:
            copy = copy + str[i]
    return (copy)
