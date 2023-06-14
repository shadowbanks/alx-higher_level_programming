#!/usr/bin/python3

def search_replace(my_list: list, search: int, replace: list) -> list:
    return [i if i != search else replace for i in  my_list]
