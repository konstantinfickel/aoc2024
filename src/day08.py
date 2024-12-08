from aocd.models import Puzzle
from aocp import ListParser
from itertools import permutations
import re

puzzle = Puzzle(day=8, year=2024)

parser = ListParser(ListParser())
input_data = puzzle.input_data
# input_data = puzzle.examples[0].input_data

def antenna_positions(data):
    antenna_dict = {}

    for y, r in enumerate(data):
        for x, f in enumerate(r):
            if f != '.':
                pos = (x, y)
                antenna_dict[f] =  antenna_dict[f] + [pos] if f in antenna_dict else [pos]

    return antenna_dict, len(data[0]), len(data)

antenna_pos, width, height = antenna_positions(parser.parse(input_data))

def in_map(pos):
    return pos[0] >= 0 and pos[1] >= 0 and pos[0] < width and pos[1] < height

def get_pos(left, right, i = 1):
    dx = right[0] - left[0]
    dy = right[1] - left[1]

    return (left[0] - dx * i, left[1] - dy * i)


def star01():
    antinodes = set()
    for name, positions in antenna_pos.items():
        for left, right in permutations(positions,2):
            a_pos = get_pos(left, right)
            if in_map(a_pos):
                antinodes.add(a_pos)
    return len(antinodes)

def star02():
    antinodes = set()
    for name, positions in antenna_pos.items():
        for left, right in permutations(positions,2):
            i = 1
            a_pos = get_pos(left, right, i)
            while in_map(a_pos):
                antinodes.add(a_pos)
                i += 1
                a_pos = get_pos(left, right, i)

            i = 0
            a_pos = get_pos(left, right, i)
            while in_map(a_pos):
                antinodes.add(a_pos)
                i -= 1
                a_pos = get_pos(left, right, i)
    return len(antinodes)

answer_a = star01()
answer_b = star02()
print(answer_a, answer_b)