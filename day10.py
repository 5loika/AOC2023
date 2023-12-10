#!/bin/python3
""" Advent of Code 2023 -- Day 10"""

import sys
import aocd

TESTDATA1 = TESTDATA2 = """-L|F7
7S-7|
L|7||
-L-J|
L|-JF
"""


TEST1 = 4
TEST2 = None

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.


def north(loc):
    return (loc[0] - 1, loc[1])  # North


def south(loc):
    return (loc[0] + 1, loc[1])  # South


def east(loc):
    return (loc[0], loc[1] + 1)  # East


def west(loc):
    return (loc[0], loc[1] - 1)  # West


def part1(rawdata):
    """Code to solve part 1 of the puzzle"""
    map = []
    path = []
    start = None
    lines = rawdata.splitlines()
    for l in lines:
        map.append([x for x in l])
    rows = len(map)
    for r in range(rows):
        cols = len(map[r])
        for c in range(cols):
            if map[r][c] == "S":
                start = (r, c)
    path.append(start)
    print("Start at:", start)
    a = None
    b = None
    # check North:
    if start[0] > 1:
        if map[start[0] - 1][start[1]] in "|7F":
            print("Up is connected")
            if a == None:
                a = (start[0] - 1, start[1])
            elif b == None:
                b = (start[0] - 1, start[1])
            else:
                return None
    # check East:
    elif start[1] + 1 < cols:
        if map[start[0]][start[1] + 1] in "-J7":
            print("Right is connected")
            if a == None:
                a = (start[0], start[1] + 1)
            elif b == None:
                b = (start[0], start[1] + 1)
            else:
                return None
    # check South:
    elif start[0] + 1 < rows:
        if map[start[0] + 1][start[1]] in "|LJ":
            print("Down is connected")
            if a == None:
                a = (start[0] + 1, start[1])
            elif b == None:
                b = (start[0] + 1, start[1])
            else:
                return None
    # check West:
    elif start[1] - 1 > 1:
        if map[start[0]][start[1] - 1] in "-LF":
            print("Left is connected")
            if a == None:
                a = (start[0], start[1] - 1)
            elif b == None:
                b = (start[0], start[1] - 1)
            else:
                return None
    path.append(a)
    dest = b
    curr = a
    while True:
        if map[curr[0]][curr[1]] == "|":  # North/South
            a = north(curr)
            b = south(curr)
        elif map[curr[0]][curr[1]] == "-":  # East/West
            a = east(curr)
            b = west(curr)
        elif map[curr[0]][curr[1]] == "L":  # North/East
            a = north(curr)
            b = east(curr)
        elif map[curr[0]][curr[1]] == "J":  # North/West
            a = north(curr)
            b = west(curr)
        elif map[curr[0]][curr[1]] == "7":  # South/West
            a = south(curr)
            b = west(curr)
        elif map[curr[0]][curr[1]] == "F":  # South/East
            a = south(curr)
            b = east(curr)
        elif map[curr[0]][curr[1]] == ".":  # Ground
            print("Why is there a . on path?")
            return None
        elif map[curr[0]][curr[1]] == "S":  # Start
            print(curr)
            print("Why did I get back to S?")
            break
        else:
            print("Nothing matched, Input error?")  # Unknown
            return None
        if a not in path:
            print("Add:", a, "to path", len(path))
            path.append(a)
            curr = a
        elif b not in path:
            print("Add: ", b, "to path", len(path))
            path.append(b)
            curr = b
        else:
            print("Both a and b already on path")
            break
    print(len(path))
    return len(path) // 2 + len(path) % 2


def part2(rawdata):
    """Code to solve part 2 of the puzzle"""
    lines = rawdata.splitlines()
    total = 0

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
