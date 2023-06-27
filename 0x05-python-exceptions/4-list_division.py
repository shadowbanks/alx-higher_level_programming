#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Divide element by element 2 lists"""
    output = []
    for i in range(list_length):
        x = 0
        try:
            x = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        else:
            pass
        finally:
            output.append(x)
    return output
