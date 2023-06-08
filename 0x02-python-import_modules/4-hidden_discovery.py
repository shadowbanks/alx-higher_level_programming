#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    for i in dir(hidden):
        if i[0] == "_":
            pass
        else:
            print("{}".format(i))
        i = i + 1
