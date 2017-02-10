__author__ = 'Marcin'
import sys
import os


def printProgress(val):
    if (val < 100 and val > 0):
        sys.stdout.flush()
        sys.stdout.write("[")
        sys.stdout.write("=")
