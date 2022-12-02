#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = len(sys.argv) - 1

    if arg == 0:
        print("{} arguments.".format(arg))
    elif arg == 1:
        print("{} argument:".format(arg))
    else:
        print("{} arguments:".format(arg))

    if arg >= 1:
        i = 0
        for item in sys.argv:
            if item != sys.argv[0]:
                print("{}: {}".format(i, item))
            i += 1
