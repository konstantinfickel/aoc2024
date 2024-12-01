from aocd.models import Puzzle
from aocp import IntParser, ListParser, TupleParser
import numpy as np

puzzle = Puzzle(day=2, year=2024)

parser = ListParser(TupleParser((IntParser(), IntParser())))
data = np.array(parser.parse(puzzle.input_data))

def star01(data):
    return 0

def star02(data):
    return 0

answer_a = star01(data)
answer_b = star02(data)
# puzzle.answer_a = answer_a
# puzzle.answer_b = answer_b

