from aocd.models import Puzzle
from aocp import IntParser, ListParser, TupleParser
import numpy as np
import re

puzzle = Puzzle(day=5, year=2024)

parser = TupleParser((ListParser(TupleParser([IntParser(), IntParser()])), ListParser(ListParser(IntParser()))))
input_data = puzzle.input_data
# input_data = puzzle.examples[0].input_data
order_list, updates = parser.parse(input_data)

def get_before_dict(order_list):
    order_dict = {}
    for before, after in order_list:
        order_dict[after] = order_dict[after] + [before] if after in order_dict else [before]
    return order_dict

def get_after_dict(order_list):
    order_dict = {}
    for after, before in order_list:
        order_dict[after] = order_dict[after] + [before] if after in order_dict else [before]
    return order_dict

before_dict = get_before_dict(order_list)
after_dict = get_after_dict(order_list)

def get_middle_number(update):
    return update[int(len(update)/2)]

def is_valid_update(update):
    for i in range(len(update)):
        for j in range(i):
            r = update[i]
            l = update[j]
            if r in after_dict and l in after_dict[r]:
                return False
    return True


def star01():
    valid_updates = []

    for u in updates:
        if is_valid_update(u):
            valid_updates.append(u)

    return sum([get_middle_number(u) for u in valid_updates])

def order_update(update):
    output = []
    remaining_numbers = update.copy()

    while not len(remaining_numbers) == 0:
        for r in remaining_numbers:
            is_valid = True
            for l in remaining_numbers:
                if l == r:
                    continue
                if r in before_dict and l in before_dict[r]:
                    is_valid = False
                    break
            if is_valid:
                remaining_numbers.remove(r)
                output.append(r)

    return output

def star02():
    invalid_updates = []

    for u in updates:
        if not is_valid_update(u):
            invalid_updates.append(u)

    return sum([get_middle_number(order_update(u)) for u in invalid_updates])

answer_a = star01()
answer_b = star02()
print(answer_a, answer_b)