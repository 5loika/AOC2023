#!/bin/python3
""" Advent of Code 2023 -- Day 06"""

import sys
import re
import math
import aocd

TESTDATA1 = TESTDATA2 = """Time:      7  15   30
Distance:  9  40  200
"""

TEST1 = 288
TEST2 = 71503


def part1(rawdata):
    """Code to solve part 1 of the puzzle"""
    wins = []
    lines = rawdata.splitlines()
    times = [int(i) for i in re.findall("\\d+", lines[0])]
    distances = [int(i) for i in re.findall("\\d+", lines[1])]
    for race, time in enumerate(times):
        c = 0
        for p in range(time):
            dist = (p) * (time - p)
            if dist > distances[race]:
                c += 1
        wins.append(c)
    return math.prod(wins)


def part2(rawdata):
    """Code to solve part 2 of the puzzle"""
    lines = rawdata.splitlines()
    times = [int(i) for i in re.findall("\\d+", lines[0].replace(" ", ""))]
    distances = [int(i) for i in re.findall("\\d+", lines[1].replace(" ", ""))]
    time = times[0]
    dist = distances[0]
    loss = 0
    for p in range(time):
        # Count first group of losses
        d = (p) * (time - p)
        if d <= dist:
            loss += 1
        else:
            break
        # subtract double the losses to calculate wins
    return time + 1 - (2 * loss)


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
