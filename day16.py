#!/bin/python3
""" Advent of Code 2023 -- Day 16"""

import sys
import aocd
from collections import defaultdict

TESTDATA1 = TESTDATA2 = R""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....
"""

TEST1 = 46
TEST2 = 51


def part1(rawdata):
    """Code to solve part 1 of the puzzle"""
    visited = defaultdict(lambda: 0)
    puzz = []
    processed = []
    locations = [[(0,0),(0,1)]]
    for line in rawdata.splitlines():
        r = [c for c in line]
        puzz.append(r)
    ROWS = len(puzz)
    COLS = len(puzz[0])
    while len(locations) > 0:
        if locations[0] in processed:
            locations.pop(0)
        else:
            loc = locations[0][0]
            dir = locations[0][1]
            row = loc[0]
            col = loc[1]
            rd = dir[0]
            cd = dir[1]
            rn = row + rd
            cn = col + cd
            processed.append(locations.pop(0))
            if row in range(0,ROWS) and col in range(0,COLS):
                visited[(row,col)] += 1
                if puzz[row][col] == '.':
                    locations.append([(rn,cn),dir])
                elif puzz[row][col] == '-':
                    if rd == 0: # Moving horizontal -- continue
                        locations.append([(rn,cn),(dir)])
                    else: # Moving vertical, add right &  left
                        locations.append([(row,col+1),(0,1)])
                        locations.append([(row,col-1),(0,-1)])
                elif puzz[row][col] == '|':
                    if cd == 0: # Moving vertical -- continue
                        locations.append([(rn,cn),dir])
                    else: # Moving horizontal -- add up & down
                        locations.append([(row-1,col),(-1,0)])
                        locations.append([(row+1,col),(1,0)])
                elif puzz[row][col] == '/':
                    if cd == -1: # moving left add down
                        locations.append([(row+1,col),(1,0)])
                    elif cd == 1: # moving right, add up
                        locations.append([(row-1,col),(-1,0)])
                    elif rd == -1: # moving up, add right
                        locations.append([(row,col+1),(0,1)])
                    elif rd == 1: # moving down, add left
                        locations.append([(row,col-1),(0,-1)])
                elif puzz[row][col] == '\\':
                    if cd == -1: # moving left, add up
                        locations.append([(row-1,col),(-1,0)])
                    elif cd == 1: # moving right, add down
                        locations.append([(row+1,col),(1,0)])
                    elif rd == -1: # moving up, add left
                        locations.append([(row,col-1),(0,-1)])
                    elif rd == 1: # moving down, add right
                        locations.append([(row,col+1),(0,1)])
    total = len(visited.keys())
    return total


def part2(rawdata):
    """Code to solve part 2 of the puzzle"""
    puzz = []
    for line in rawdata.splitlines():
        r = [c for c in line]
        puzz.append(r)
    ROWS = len(puzz)
    COLS = len(puzz[0])
    starting = []
    for r in range(ROWS):
        starting.append([[(r,0),(0,1)]])
        starting.append([[(r,COLS-1),(0,-1)]])
    for c in range(COLS):
        starting.append([[(0,c),(1,0)]])
        starting.append([[(ROWS-1,c),(-1,0)]])
    visited = defaultdict(lambda: 0)
    processed = []
    locations = []
    total = 0
    while len(starting) > 0:
        processed.clear()
        visited.clear()
        locations.clear()
        locations = starting.pop(0)
        while len(locations) > 0:
            if locations[0] in processed:
                locations.pop(0)
            else:
                loc = locations[0][0]
                dir = locations[0][1]
                row = loc[0]
                col = loc[1]
                rd = dir[0]
                cd = dir[1]
                rn = row + rd
                cn = col + cd
                processed.append(locations.pop(0))
                if row in range(0,ROWS) and col in range(0,COLS):
                    visited[(row,col)] += 1
                    if puzz[row][col] == '.':
                        locations.append([(rn,cn),dir])
                    elif puzz[row][col] == '-':
                        if rd == 0: # Moving horizontal -- continue
                            locations.append([(rn,cn),(dir)])
                        else: # Moving vertical, add right &  left
                            locations.append([(row,col+1),(0,1)])
                            locations.append([(row,col-1),(0,-1)])
                    elif puzz[row][col] == '|':
                        if cd == 0: # Moving vertical -- continue
                            locations.append([(rn,cn),dir])
                        else: # Moving horizontal -- add up & down
                            locations.append([(row-1,col),(-1,0)])
                            locations.append([(row+1,col),(1,0)])
                    elif puzz[row][col] == '/':
                        if cd == -1: # moving left add down
                            locations.append([(row+1,col),(1,0)])
                        elif cd == 1: # moving right, add up
                            locations.append([(row-1,col),(-1,0)])
                        elif rd == -1: # moving up, add right
                            locations.append([(row,col+1),(0,1)])
                        elif rd == 1: # moving down, add left
                            locations.append([(row,col-1),(0,-1)])
                    elif puzz[row][col] == '\\':
                        if cd == -1: # moving left, add up
                            locations.append([(row-1,col),(-1,0)])
                        elif cd == 1: # moving right, add down
                            locations.append([(row+1,col),(1,0)])
                        elif rd == -1: # moving up, add left
                            locations.append([(row,col-1),(0,-1)])
                        elif rd == 1: # moving down, add right
                            locations.append([(row,col+1),(0,1)])
        total = max(total,len(visited.keys()))

    return total


if __name__ == "__main__":
    Test = Run = Submit = PartA = PartB = False
    if len(sys.argv) > 1:
        if "test" in sys.argv:
            Test = True
        if "run" in sys.argv:
            Run = True
        if "submit" in sys.argv:
            Run = Submit = True
        if "a" in sys.argv:
            PartA = True
        if "b" in sys.argv:
            PartB = True
        if "both" in sys.argv:
            PartA = PartB = True
    else:
        Test = Run = PartA = PartB = True
    if Test and PartA:
        test1 = part1(TESTDATA1)
        if test1 == TEST1:
            print("Test 1 - Pass:", test1)
        else:
            print("Test 1 - Fail:", test1)
    if Test and PartB:
        test2 = part2(TESTDATA2)
        if test2 == TEST2:
            print("Test 2 - Pass:", test2)
        else:
            print("Test 2 - Fail:", test2)
    if Run and PartA:
        result1 = part1(aocd.data)
        print("Part 1: ", result1)
    if Run and PartB:
        result2 = part2(aocd.data)
        print("Part 2: ", result2)
    if Submit and PartA:
        print("Submit - Part 1:", result1)
        aocd.submit(result1, part="a")
    if Submit and PartB:
        print("Submit - Part 2: ", result2)
        aocd.submit(result2, part="b")
