#!/usr/bin/python3
for i in range(26):
    if (chr(ord('a') + i) == 'q' or chr(ord('a') + i) == 'e'):
        continue
    print("{}".format(chr(ord('a') + i)), end="")
