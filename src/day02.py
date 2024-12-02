from aocd.models import Puzzle
from aocp import IntParser, ListParser, TupleParser
import numpy as np

puzzle = Puzzle(day=2, year=2024)

parser = ListParser(ListParser(IntParser()))
input_data = puzzle.input_data
# input_data = """
# 7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9
# """
data = parser.parse(input_data)

def is_safe(row, f, damp):
    j = row[0]
    d = damp
    for i in row[1:]:
        if f * (i - j) > 3 or f * (i - j) < 1:
            if damp > 0:
                damp -= 1
                continue
            return False
        j = i
    return True


def star01(data):
    o = 0
    for i in data:
        if is_safe(i, -1, 0) or is_safe(i,  1, 0):
            o+= 1
    return o

def star02(data):
    o = 0
    for i in data:
        p = 0
        if is_safe(i, -1, 0) or is_safe(i,  1, 0):
            p+= 1
        for x, j in enumerate(i):
            y = i.copy()
            y.pop(x)
            if is_safe(y, -1, 0) or is_safe(y,  1, 0):
                p+= 1
        o += min(p, 1)

    return o

answer_a = star01(data)
answer_b = star02(data)
print(answer_a, answer_b)
# puzzle.answer_a = answer_a
# puzzle.answer_b = answer_b

