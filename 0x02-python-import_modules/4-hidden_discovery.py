#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    hidden = dir(hidden_4)
    for i in hidden.sort():
        if i[0] == "_":
            pass
        else:
            print("{}".format(i))
        i = i + 1
