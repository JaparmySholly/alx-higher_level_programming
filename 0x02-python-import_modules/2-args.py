#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    """Print total number of argument.
    Follows by argument index number and the name.
    """
    if len(argv) == 1:
        print("0 arguments", end=".\n")
    elif len(argv) == 2:
        print("{} argument".format(len(argv) - 1), end=":\n")
        for i in range(len(argv) - 1):
            print("{}: {}".format(i + 1, argv[i + 1]))
        else:
            print("{} arguments".format(len(argv) - 1), end=":\n")
            for i in range(len(argv) - 1):
                print("{}: {}".format(i + 1, argv[i + 1]))
