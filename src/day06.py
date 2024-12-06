from aocd.models import Puzzle
from aocp import IntParser, ListParser, TupleParser
import numpy as np
import re

puzzle = Puzzle(day=6, year=2024)

parser = ListParser(ListParser())
input_data = puzzle.input_data
# input_data = puzzle.examples[0].input_data
data = parser.parse(input_data)

def find_guard(data):
    for y, r in enumerate(data):
        for x, f in enumerate(r):
            if f == '^':
                return x,y

def turn(direction):
    if direction == (0, -1):
        return (1, 0)
    if direction == (1, 0):
        return (0, 1)
    if direction == (0, 1):
        return (-1, 0)
    if direction == (-1, 0):
        return (0, -1)

def star01(data):
    visited = {}
    loop_det = {}

    x,y = find_guard(data)
    w = len(data[0])
    h = len(data)

    direction = (0, -1)

    while x >= 0 and y >= 0 and x < w and y < h:
        if (x,y,direction) in loop_det.keys():
            return -1
        visited[(x,y)] = True
        loop_det[(x,y,direction)] = True

        next_x = x + direction[0]
        next_y = y + direction[1]

        if not (next_x >= 0 and next_y >= 0 and next_x < w and next_y < h):
            break

        if  data[next_y][next_x] == "#":
            direction = turn(direction)
            continue
        
        x = next_x
        y = next_y

    return len(visited.keys())

def star02(data):
    w = len(data[0])
    h = len(data)

    out = 0

    for y in range(h):
        for x in range(w):
            data_copy = [row.copy() for row in data]
            if data_copy[y][x] != ".":
                continue
            data_copy[y][x] = "#"
            if star01(data_copy) == -1:
                out += 1
            
    return out

answer_a = star01(data)
answer_b = star02(data)
print(answer_a, answer_b)