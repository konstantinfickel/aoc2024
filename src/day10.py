from aocd.models import Puzzle
from aocp import IntParser, ListParser, TupleParser
import numpy as np
import re

puzzle = Puzzle(day=10, year=2024)

parser = ListParser(ListParser(IntParser()))
input_data = puzzle.input_data
data = parser.parse(input_data)

def in_map(data, pos):
    width = len(data[0])
    height = len(data)
    return 0 <= pos[1] < height and 0 <= pos[0] < width

def neighbours(data, pos):
    n = [
        (pos[0], pos[1]-1),
        (pos[0]-1, pos[1]),
        (pos[0]+1, pos[1]),
        (pos[0], pos[1]+1),
    ]
    return list(filter(lambda p: in_map(data, p), n))

def evaluate_trailhead(data, pos):
    width = len(data[0])
    height = len(data)

    count = set()

    p_val = data[pos[1]][pos[0]]

    if p_val == 9:
        count.add(pos)
        return count

    for pos_n in neighbours(data, pos):
        p_n_val = data[pos_n[1]][pos_n[0]]
        if p_val + 1 == p_n_val:

            count = count.union(evaluate_trailhead(data, pos_n))
    
    return count

def star01(data):
    width = len(data[0])
    height = len(data)

    out = 0

    for y in range(height):
        for x in range(width):
            if data[y][x] == 0:
                out += len(evaluate_trailhead(data, (x, y)))

    return out

def evaluate_trailhead_a(data, pos):
    width = len(data[0])
    height = len(data)

    count = []

    p_val = data[pos[1]][pos[0]]

    if p_val == 9:
        return [pos]

    for pos_n in neighbours(data, pos):
        p_n_val = data[pos_n[1]][pos_n[0]]
        if p_val + 1 == p_n_val:
            count.extend(evaluate_trailhead_a(data, pos_n))
    
    return count

def star02(data):
    width = len(data[0])
    height = len(data)

    out = 0

    for y in range(height):
        for x in range(width):
            if data[y][x] == 0:
                out += len(evaluate_trailhead_a(data, (x, y)))

    return out

answer_a = star01(data)
answer_b = star02(data)
print(answer_a, answer_b)