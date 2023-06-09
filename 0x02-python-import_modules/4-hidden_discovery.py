#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    hidden = dir(hidden_4)
    hidden.sort()
    for i in hidden:
        if i[:1] == "__":
            pass
        else:
            print("{}".format(i))
