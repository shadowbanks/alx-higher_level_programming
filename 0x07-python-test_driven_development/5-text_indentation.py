#!/usr/bin/python3
"""
This Function indents a Text passed to it
"""
import doctest


def text_indentation(text):
    """This function insert two newlines after
        each of the following characters: (. ? :)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    output = ""
    line = ""

    for i in range(len(text)):
        if text[i] in (".", "?", ":"):
            line += text[i]
            if (i + 1 < len(text)):
                if text[i + 1].isspace():
                    i += 1
                    line += text[i]
            line = line.strip()
            line += "\n\n"
            output += line
            line = ""
        line += text[i]
    output += line.strip()
    print(output, end="")


if __name__ == "__main__":
    doctest.testfile("./tests/5-text_indentation.txt")
