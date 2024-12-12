from aocd.models import Puzzle
from aocp import IntParser, ListParser, TupleParser
import numpy as np
import re

puzzle = Puzzle(day=12, year=2024)

parser = ListParser(ListParser())
input_data = puzzle.input_data

data = parser.parse(input_data)

def get_neighbours(pos):
    return [
        (pos[0], pos[1]-1),
        (pos[0]-1, pos[1]),
        (pos[0]+1, pos[1]),
        (pos[0], pos[1]+1),
    ]

def in_map(data, cur):
    return 0 <= cur[0] < len(data[0]) and 0 <= cur[1] < len(data)

def count_perimiters(same_direction_perimiter):
    out = 0
    for r, p in same_direction_perimiter.items():
        sorted_p = sorted(p)

        val = 1
        prev = sorted_p[0]
        for q in sorted_p[1:]:
            if q > prev + 1:
                val += 1
            prev = q
        out += val
    return out



def measure_area(data, pos, visited):
    area = 0
    perimiter = 0

    area_letter = data[pos[1]][pos[0]]

    v_in_perimiter = {}
    h_in_perimiter = {}
    v_out_perimiter = {}
    h_out_perimiter = {}

    queue = [pos]

    while len(queue) > 0:
        cur = queue.pop()
        if cur in visited:
            continue
        area += 1
        visited.add(cur)
        own_letter = data[cur[1]][cur[0]]

        for ngh in get_neighbours(cur):
            if not in_map(data, ngh) or area_letter != data[ngh[1]][ngh[0]]:
                perimiter += 1
                if ngh[0] < cur[0]:
                    pval = ngh[1]
                    pid = min(ngh[0], cur[0])
                    v_in_perimiter[pid] = v_in_perimiter[pid] + [pval] if pid in v_in_perimiter else [pval]
                elif ngh[0] > cur[0]:
                    pval = ngh[1]
                    pid = min(ngh[0], cur[0])
                    v_out_perimiter[pid] = v_out_perimiter[pid] + [pval] if pid in v_out_perimiter else [pval]
                elif ngh[1] < cur[1]:
                    pval = ngh[0]
                    pid = min(ngh[1], cur[1])
                    
                    h_in_perimiter[pid] = h_in_perimiter[pid] + [pval] if pid in h_in_perimiter else [pval]
                elif ngh[1] > cur[1]:
                    pval = ngh[0]
                    pid = min(ngh[1], cur[1])
                    
                    h_out_perimiter[pid] = h_out_perimiter[pid] + [pval] if pid in h_out_perimiter else [pval]
                else:
                    raise Exception("Shit!")
            else:
                if ngh not in visited:
                    queue.append(ngh)
    
    sides = count_perimiters(v_in_perimiter)\
        + count_perimiters(h_in_perimiter)\
        + count_perimiters(h_out_perimiter)\
        + count_perimiters(v_out_perimiter)
    
    return area, perimiter, sides

def star01(data):
    result = 0
    visited = set()
    for y in range(len(data)):
        for x in range(len(data[0])):
            if (x,y) not in visited:
                area, perimiter, _ = measure_area(data, (x,y), visited)
                result += area * perimiter

    return result

def star02(data):
    result = 0
    visited = set()
    for y in range(len(data)):
        for x in range(len(data[0])):
            if (x,y) not in visited:
                area, _, sides = measure_area(data, (x,y), visited)
                result += area * sides

    return result

answer_a = star01(data)
answer_b = star02(data)
print(answer_a, answer_b)