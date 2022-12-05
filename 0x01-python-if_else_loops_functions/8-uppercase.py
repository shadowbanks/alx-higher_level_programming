#!/usr/bin/python3
def uppercase(str):
    for i in str:
        char_asci = ord(i)
        if char_asci >= 97 and char_asci <= 123:
            i = chr(char_asci - 32)
        print("{}".format(i), end="")
    print()
