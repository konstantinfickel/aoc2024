from aocd.models import Puzzle
from aocp import IntParser, ListParser, TupleParser
import numpy as np
import re
import functools

puzzle = Puzzle(day=11, year=2024)

parser = ListParser(IntParser())
input_data = puzzle.input_data
# input_data = "125 17"
data = parser.parse(input_data)

@functools.cache
def get_stones_after_generations(number: int, generations: int) -> int:
    if generations <= 0:
        return 1
    
    if number == 0:
        return get_stones_after_generations(1, generations - 1)
    if len(str(number)) % 2 == 0:
        both = str(number)
        left = int(both[:len(both)//2])
        right = int(both[len(both)//2:])
        return get_stones_after_generations(left, generations - 1) + get_stones_after_generations(right, generations - 1)
    else:
        return get_stones_after_generations(number * 2024, generations - 1)

def star01(data):
    return sum([get_stones_after_generations(i, 25) for i in data])

def star02(data):
    return sum([get_stones_after_generations(i, 75) for i in data])

answer_a = star01(data)
answer_b = star02(data)
print(answer_a, answer_b)