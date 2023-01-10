#!/usr/bin/python3
"""
Filename: 0-lookup.py
function returns list of available attributes and methods of an object
"""


def lookup(object):
    """List Info about given object"""
    return dir(object)
