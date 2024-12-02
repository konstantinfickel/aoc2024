from aocd.models import Puzzle
from aocp import IntParser, ListParser, TupleParser
import numpy as np

puzzle = Puzzle(day=3, year=2024)

parser = ListParser(ListParser(IntParser()))
input_data = puzzle.input_data
input_data = puzzle.examples[0].input_data
data = parser.parse(input_data)

def star01(data):
    return 0

def star02(data):
    return 0

answer_a = star01(data)
answer_b = star02(data)
print(answer_a, answer_b)

