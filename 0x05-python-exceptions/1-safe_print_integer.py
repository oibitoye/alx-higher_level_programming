#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except (SyntaxError, ValueError, TypeError):
        return False