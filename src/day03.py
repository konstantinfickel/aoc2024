from aocd.models import Puzzle
from aocp import IntParser, ListParser, TupleParser
import numpy as np
import re

puzzle = Puzzle(day=3, year=2024)

input_data = puzzle.input_data
data = input_data

def star01(data):
    return sum([int(m.group(1))*int(m.group(2)) for m in re.finditer(r"mul\((\d+),(\d+)\)", data)])

def star02(data):
    return sum(
        [
            star01(s.group(2))
                for s in re.finditer(r"(?s)(^|do\(\)|don't\(\))(.*?)(?=do\(\)|don't\(\)|$)", data)
                if s.group(1) != "don't()"
        ]
    )

answer_a = star01(data)
answer_b = star02(data)
print(answer_a, answer_b)

