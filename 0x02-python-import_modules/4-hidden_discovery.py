#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    hidden = dir(hidden_4)
    hidden.sort()
    for i in hidden:
        if i[:2] != "__":
            print("{}".format(i))
