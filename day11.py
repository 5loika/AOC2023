#!/bin/python3
""" Advent of Code 2023 -- Day 11"""

import sys
from itertools import combinations
import aocd

TESTDATA1 = TESTDATA2 = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
"""

TEST1 = 374
TEST2 = 1030


def part1(rawdata):
    """Code to solve part 1 of the puzzle"""
    map = []
    gal = []
    lines = rawdata.splitlines()
    for l in lines:
        map.append([c for c in l])
    for r in range(len(map)):
        for c in range(len(map[0])):
            if map[r][c] == "#":
                gal.append((r, c))
    galrows = [int(r) for r, c in gal]
    galcols = [int(c) for r, c in gal]
    for n in range(len(map[0]) - 1, -1, -1):
        if n not in galcols:
            for r in range(len(map)):
                map[r].insert(n, ".")
    newrow = ["." for n in range(len(map[0]))]
    for n in range(len(map), -1, -1):
        if n not in galrows:
            map.insert(n, newrow)
    galaxy = set()
    for r in range(len(map)):
        for c in range(len(map[0])):
            if map[r][c] == "#":
                galaxy.add((r, c))
    combs = combinations(galaxy, 2)
    total = 0
    for p in combs:
        d = abs(p[1][0] - p[0][0]) + abs(p[1][1] - p[0][1])
        total += d
    return total


def part2(rawdata):
    """Code to solve part 2 of the puzzle"""
    map = []
    gal = []
    lines = rawdata.splitlines()
    for l in lines:
        map.append([c for c in l])
    for r in range(len(map)):
        for c in range(len(map[0])):
            if map[r][c] == "#":
                gal.append((r, c))
    galrows = [int(r) for r, c in gal]
    galcols = [int(c) for r, c in gal]
    emptyrows = []
    emptycols = []
    for n in range(len(map)):
        if n not in galrows:
            emptyrows.append(n)
    for n in range(len(map[0])):
        if n not in galcols:
            emptycols.append(n)
    galaxy = set()
    for r in range(len(map)):
        for c in range(len(map[0])):
            if map[r][c] == "#":
                galaxy.add((r, c))
    combs = combinations(galaxy, 2)
    total = 0
    expandfactor = 999999
    for p in combs:
        rexpand0 = rexpand1 = 0
        cexpand0 = cexpand1 = 0
        for r in emptyrows:
            if p[0][0] > r:
                rexpand0 += 1
            if p[1][0] > r:
                rexpand1 += 1
        for c in emptycols:
            if p[0][1] > c:
                cexpand0 += 1
            if p[1][1] > c:
                cexpand1 += 1
        rexpand0 *= expandfactor
        rexpand1 *= expandfactor
        cexpand0 *= expandfactor
        cexpand1 *= expandfactor
        d = abs((p[1][0] + rexpand1) - (p[0][0] + rexpand0)) + abs(
            (p[1][1] + cexpand1) - (p[0][1] + cexpand0)
        )
        total += d
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
