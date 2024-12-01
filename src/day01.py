from aocd.models import Puzzle
from aocp import IntParser, ListParser, TupleParser
import numpy as np

puzzle = Puzzle(day=1, year=2024)

parser = ListParser(TupleParser((IntParser(), IntParser())))
data = np.array(parser.parse(puzzle.input_data))

def star01(data):
    return np.sum(np.abs(np.sort(data[:, 0]) - np.sort(data[:, 1])))

def star02(data):
    score = 0
    left = data[:, 0]

    right = data[:, 1]
    for i in left:
        score += len(np.where(right == i)[0]) * i
    return score

answer_a = star01(data)
answer_b = star02(data)
# puzzle.answer_a = answer_a
# puzzle.answer_b = answer_b

