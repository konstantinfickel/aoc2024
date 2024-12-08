from aocd.models import Puzzle
from aocp import IntParser, ListParser, TupleParser
import numpy as np
import re

puzzle = Puzzle(day=9, year=2024)

parser = ListParser(ListParser(IntParser()))
input_data = puzzle.input_data
input_data = puzzle.examples[0].input_data
data = parser.parse(input_data)

def star01(data):
    out = 0
    return out

def star02(data):
    out = 0
    return out

answer_a = star01(data)
answer_b = star02(data)
print(answer_a, answer_b)