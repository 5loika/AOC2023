#!/bin/python3

import sys
from aocd import data
from aocd import submit
import re
testdata = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""
# testdata = """two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen
# """
test1 = 142
test2 = 281


def part1(rawdata):
    tot = 0
    lines = rawdata.splitlines()
    for line in lines:
        x = re.findall("\d", line)
        tot += 10*int(x[0])+int(x[-1])
    return tot


def part2(rawdata):
    lines = rawdata.splitlines()
    tot = 0
    for line in lines:
        line = line.replace("one", "o1e")
        line = line.replace("two", "t2o")
        line = line.replace("three", "t3e")
        line = line.replace("four", "f4r")
        line = line.replace("five", "f5e")
        line = line.replace("six", "s6x")
        line = line.replace("seven", "s7n")
        line = line.replace("eight", "e8t")
        line = line.replace("nine", "n9e")
        x = re.findall("\d", line)
        tot += 10*int(x[0])+int(x[-1])
    return tot


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "test":
            if sys.argv[2] == "a":
                result1 = part1(testdata)
                if test1 == result1:
                    print("Test 1 - Pass:", result1)
                else:
                    print("Test 1 - Fail:", result1)
            elif sys.argv[2] == "b":
                result2 = part2(testdata)
                if test2 == result2:
                    print("Test 2 - Pass:", result2)
                else:
                    print("Test 2 - Fail:", result2)
        elif sys.argv[1] == "submit":
            if sys.argv[2] == "a":
                submit(part1(data), part="a")
            elif sys.argv[2] == "b":
                submit(part2(data), part="b")
        elif sys.argv[1] == "run":
            if sys.argv[2] == "a":
                print("Part 1: ", part1(data))
            elif sys.argv[2] == "b":
                print("Part 2: ", part2(data))
    else:
        print("Part 1: ", part1(data))
        print("Part 2: ", part2(data))