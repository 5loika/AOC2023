#!/bin/python3
""" Advent of Code 2023 -- Day 01"""

import sys
import re
import aocd

TESTDATA1 = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""
TESTDATA2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""
TEST1 = 142
TEST2 = 281


def part1(rawdata):
    """Code to solve part 1 of the puzzle"""
    tot = 0
    lines = rawdata.splitlines()
    for line in lines:
        # use re.findall
        x = re.findall("\\d", line)
        tot += 10 * int(x[0]) + int(x[-1])
    return tot


def part2(rawdata):
    """Code to solve part 2 of the puzzle"""
    lines = rawdata.splitlines()
    tot = 0
    for line in lines:
        # use replace to account for written digits
        # Messy approach, but it works!
        line = line.replace("one", "o1e")
        line = line.replace("two", "t2o")
        line = line.replace("three", "t3e")
        line = line.replace("four", "f4r")
        line = line.replace("five", "f5e")
        line = line.replace("six", "s6x")
        line = line.replace("seven", "s7n")
        line = line.replace("eight", "e8t")
        line = line.replace("nine", "n9e")
        # Still use re.findall
        x = re.findall("\\d", line)
        tot += 10 * int(x[0]) + int(x[-1])
    return tot


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
