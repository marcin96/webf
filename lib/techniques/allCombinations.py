import os
import sys
import itertools
from itertools import permutations
from itertools import product


def allCombinations(pattern):
    if(pattern!="" and pattern!=""):
        ret = ["".join(p) for p in permutations(pattern)]
        return ret
    else:None


def allPossibilities(pattern):
    joint = []
    for p in itertools.product(pattern,repeat=len(pattern)):
        joint.append(p)
    return joint
