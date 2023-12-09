#!/bin/python3
"""TEST"""

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
    if len(sys.argv) > 1:
        if sys.argv[1] == "test":
            if sys.argv[2] == "a":
                result1 = part1(TESTDATA1)
                if TEST1 == result1:
                    print("Test 1 - Pass:", result1)
                else:
                    print("Test 1 - Fail:", result1)
            elif sys.argv[2] == "b":
                result2 = part2(TESTDATA2)
                if TEST2 == result2:
                    print("Test 2 - Pass:", result2)
                else:
                    print("Test 2 - Fail:", result2)
        elif sys.argv[1] == "submit":
            if sys.argv[2] == "a":
                aocd.submit(part1(aocd.data), part="a")
            elif sys.argv[2] == "b":
                aocd.submit(part2(aocd.data), part="b")
        elif sys.argv[1] == "run":
            if sys.argv[2] == "a":
                print("Part 1: ", part1(aocd.data))
            elif sys.argv[2] == "b":
                print("Part 2: ", part2(aocd.data))
    else:
        print("Part 1: ", part1(aocd.data))
        print("Part 2: ", part2(aocd.data))
