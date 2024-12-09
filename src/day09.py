from aocd.models import Puzzle
from aocp import IntParser, ListParser, TupleParser
import numpy as np
import re
from itertools import batched

puzzle = Puzzle(day=9, year=2024)

parser = ListParser(IntParser())
input_data = puzzle.input_data
# input_data = puzzle.examples[0].input_data

def expand(c_disk):
    disk = []

    i = 0
    for x in batched(c_disk, 2):
        disk.extend([i for _ in range(x[0])])
        i += 1
        if len(x)>1:
            disk.extend([None for _ in range(x[1])])

    return disk

data = expand(parser.parse(input_data))

def checksum(disk):
    check = 0
    for i, x in enumerate(disk):
        if x is not None:
            check += int(x) * i
    return check

def compact(o_disk):
    disk = o_disk.copy()

    r = len(disk)-1
    l = 0
    while l < r:
        while disk[l] is not None and l < r:
            l += 1
        while disk[r] is None and l < r:
            r -= 1

        if l >= r:
            break

        disk[l] = disk[r]
        disk[r] = None

    return disk

def compact_m(o_disk):
    disk = o_disk.copy()

    r = len(disk)-1
    while True:
        while disk[r] is None:
            r -= 1
        r_val = disk[r]
        r_c = 1
        while disk[r-1] == r_val:
            r -= 1
            r_c += 1
        
        l_p = 0
        l_c = 0
        for l in range(len(disk)):
            if disk[l] is None:
                if l_c == 0:
                    l_p = l
                l_c += 1
            else:
                l_c = 0

            if l_c >= r_c:
                break
        
        if r <= 0:
            break
        if l_c < r_c or r <= l_p:
            r -= 1
            continue
        
        for x in range(r_c):
            lx = l_p + x
            rx = r + x
            disk[lx] = disk[rx]
            disk[rx] = None

    return disk

def star01(data):
    return checksum(compact(data))

def star02(data):
    return checksum(compact_m(data))

answer_a = star01(data)
answer_b = star02(data)
print(answer_a, answer_b)