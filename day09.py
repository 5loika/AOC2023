#!/bin/python3
""" Advent of Code 2023 -- Day 09"""

import sys
import aocd

TESTDATA1 = TESTDATA2 = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""


TEST1 = 114
TEST2 = 2


def extend(row):
    next = []
    t = 0
    for i in range(len(row) - 1):
        t += abs(row[i])
        next.append(row[i + 1] - row[i])
    t += row[-1]
    if t == 0:
        return t
    else:
        return row[-1] + extend(next)


def regress(row):
    next = []
    t = 0
    for i in range(len(row) - 1):
        t += abs(row[i])
        next.append(row[i + 1] - row[i])
    t += row[-1]
    if t == 0:
        return t
    else:
        return row[0] - regress(next)


def part1(rawdata):
    """Code to solve part 1 of the puzzle"""
    lines = rawdata.splitlines()
    total = 0
    for l in lines:
        row = [int(x) for x in l.split()]
        total += extend(row)
    return total


def part2(rawdata):
    """Code to solve part 2 of the puzzle"""
    lines = rawdata.splitlines()
    total = 0
    for l in lines:
        row = [int(x) for x in l.split()]
        total += regress(row)
    return total


if __name__ == "__main__":
    Test = Run = Submit = PartA = PartB = False
    if len(sys.argv) > 1:
        if 'test' in sys.argv: Test = True
        if 'run' in sys.argv: Run = True
        if 'submit' in sys.argv: Run = Submit = True
        if 'a' in sys.argv: PartA = True
        if 'b' in sys.argv: PartB = True
        if 'both' in sys.argv: PartA = PartB = True
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