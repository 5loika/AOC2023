#!/bin/python3
""" Advent of Code 2023 -- Day 12"""

import sys
import aocd
from functools import cache
import re

TESTDATA1 = TESTDATA2 = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
"""

TEST1 = 21
TEST2 = 506250


# @cache
def aoc12(pattern, springs):
    springsneeded = sum(springs)
    if pattern.count("?") == 0:
        # all ? replaced -- does it match repair pattern?
        w = re.findall("#+", pattern)
        r = list(map(len, w))
        if r == springs:
            return 1
        else:
            return 0
    else:
        if pattern.count("#") == springsneeded:
            t = pattern
            n = t.index("?")
            t = t[:n] + "." + t[n + 1 :]
            return aoc12(t, springs)
        else:
            t = pattern
            u = pattern
            n = t.index("?")
            t = t[:n] + "." + t[n + 1 :]
            u = u[:n] + "#" + u[n + 1 :]
            return aoc12(t, springs) + aoc12(u, springs)


def part1(rawdata):
    """Code to solve part 1 of the puzzle"""
    pattern = []
    springs = []
    total = 0
    lines = rawdata.splitlines()
    for l in lines:
        a, b = l.split()
        pattern = a
        springs = [int(x) for x in b.split(",")]
        total += aoc12(pattern, springs)
    return total


def part2(rawdata):
    """Code to solve part 2 of the puzzle"""
    pattern = []
    springs = []
    total = 0
    lines = rawdata.splitlines()
    for l in lines:
        a, b = l.split()
        pattern = a + "?" + a + "?" + a + "?" + a + "?" + a
        b = b + "," + b + "," + b + "," + b + "," + b
        springs = [int(x) for x in b.split(",")]
        total += aoc12(pattern, springs)
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
