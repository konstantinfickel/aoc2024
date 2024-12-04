from aocd.models import Puzzle
from aocp import ListParser
import numpy as np
import re

puzzle = Puzzle(day=4, year=2024)

parser = ListParser(ListParser())
input_data = puzzle.input_data
data = parser.parse(input_data)

def count_occurrences(data, look_for):
    count_xmas = 0;

    current_pos = 0

    for row in data:
        for field in row:
            if field == look_for[current_pos]:
                current_pos+= 1
                if current_pos == len(look_for):
                    current_pos = 0
                    count_xmas += 1
            else:
                current_pos = 1 if field == look_for[0] else 0
        current_pos = 0

    return count_xmas

def transpose(M):
    return [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]

def mirror_x(data):
    return [list(reversed(l)) for l in data]

def mirror_y(data):
    return list(reversed(data))

def diag(test, bltr=True):
    max_col = len(test[0])
    max_row = len(test)
    cols = [[] for _ in range(max_col)]
    rows = [[] for _ in range(max_row)]
    fdiag = [[] for _ in range(max_row + max_col - 1)]
    bdiag = [[] for _ in range(len(fdiag))]
    min_bdiag = -max_row + 1

    for x in range(max_col):
        for y in range(max_row):
            cols[x].append(test[y][x])
            rows[y].append(test[y][x])
            fdiag[x+y].append(test[y][x])
            bdiag[x-y-min_bdiag].append(test[y][x])
    
    return fdiag if bltr else bdiag


def star01(data):
    count_xmas = 0;
    look_for = ['X', 'M', 'A', 'S']

    count_xmas += count_occurrences(data, look_for)
    count_xmas += count_occurrences(transpose(data), look_for)
    count_xmas += count_occurrences(mirror_x(data), look_for)
    count_xmas += count_occurrences(mirror_x(transpose(data)), look_for)
    count_xmas += count_occurrences(diag(data, True), look_for)
    count_xmas += count_occurrences(diag(data, False), look_for)
    count_xmas += count_occurrences(mirror_x(diag(data, True)), look_for)
    count_xmas += count_occurrences(mirror_x(diag(data, False)), look_for)


    return count_xmas

def cut_out(data, x, y):
    return [
        data[y-1][x-1:x+2],
        data[y][x-1:x+2],
        data[y+1][x-1:x+2],
    ]

def is_diag_crossing(data):
    return (
        data[0][0] == 'M' and
        data[1][1] == 'A' and
        data[2][2] == 'S' and
        data[2][0] == 'M' and
        data[0][2] == 'S'
    )

def is_count(data):
    for t in [True, False]:
        for mx in [True, False]:
            for my in [True, False]:
                f = [r.copy() for r in data]
                if mx:
                    f = mirror_x(f)
                if my:
                    f = mirror_y(f)
                if t:
                    f = transpose(f)
                if is_diag_crossing(f):
                    return True
    return False

def star02(data):
    h = len(data)
    w = len(data[0])
    out = 0
    for y in range(1, h - 1):
        for x in range(1, w - 1):
            cut = cut_out(data, x, y)
            if is_count(cut):
                out += 1
    return out

answer_a = star01(data)
answer_b = star02(data)
print(answer_a, answer_b)
