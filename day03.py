#!/bin/python3

import sys
from aocd import data
from aocd import submit

testdata = """
"""

test1 = None
test2 = None

def part1(rawdata):
    lines = rawdata.splitlines()
    for line in lines:
        continue
    return None

def part2(rawdata):
    lines = rawdata.splitlines()
    for line in lines:
        continue
    return None


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