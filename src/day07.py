from aocd.models import Puzzle
from aocp import IntParser, ListParser, TupleParser
import numpy as np
import re
from decimal import Decimal

puzzle = Puzzle(day=7, year=2024)

parser = ListParser(TupleParser((IntParser(), ListParser(IntParser()))))
input_data = puzzle.input_data
# input_data = puzzle.examples[0].input_data
data = parser.parse(input_data)

def get_result(numbers, operators):
    calculation = Decimal(numbers[0])
    for num, op in zip(numbers[1:], operators):
        if op == "+":
            calculation += Decimal(num)
        elif op == "*":
            calculation *= Decimal(num)
        elif op == "|":
            calculation = Decimal(str(calculation)+str(num))
        else:
            raise Exception("No Op!")
    return calculation

def get_all_operators(num_len, add_concat):
    op = [[]]
    for i in range(num_len - 1):
        op = [o + ['+'] for o in op] + [o + ['*'] for o in op] + ([o + ['|'] for o in op] if add_concat else [])
    return op

def star01(data):
    out = Decimal(0)
    for result, num in data:
        works = False

        ops = get_all_operators(len(num), False)
        for op in ops:
            if get_result(num, op) == Decimal(result):
                works = True
                break
    
        if works:
            out += Decimal(result)
    return Decimal(out)

def star02(data):
    out = Decimal(0)
    for result, num in data:
        works = False

        ops = get_all_operators(len(num), True)
        for op in ops:
            if get_result(num, op) == Decimal(result):
                works = True
                break
    
        if works:
            out += Decimal(result)
    return Decimal(out)

answer_a = star01(data)
answer_b = star02(data)
print(answer_a, answer_b)