#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    i = 0
    div = []
    while (i < list_length):
        try:
            temp = my_list_1[i] / my_list_2[i]

        except TypeError:
            temp = 0
            print("wrong type")

        except ZeroDivisionError:
            temp = 0
            print("Division by 0")

        except IndexError:
            temp = 0
            print("out of range")

        finally:
            i += 1
            div.append(temp)

    return (div)
