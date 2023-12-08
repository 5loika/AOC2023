#!/bin/python3
"""TEST"""

import sys
import re
import numpy as np
import aocd

TESTDATA1 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""

TESTDATA2 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
"""

TEST1 = 6
TEST2 = None

def findpath(r, s, n):
    j = 0
    count = 1
    loc = r
    while True:
        if s[j] == 'L':
            loc = n[loc][0]
        else:
            loc = n[loc][1]
        if loc[2] == 'Z':
            return count
        count += 1
        j += 1
        if j == len(s):
            j = 0
    return None

def part1(rawdata):
    nodes = {}
    """Code to solve part 1 of the puzzle"""
    groups = rawdata.split('\n\n')
    steps = [i for i in groups[0].strip()]
    for line in groups[1].splitlines():
        node, left, right = re.findall('[A-Z][A-Z][A-Z]',line)
        nodes[node] = [left,right]
    j = 0
    count = 1
    loc = 'AAA'
    while True:
        if steps[j] == 'L':
            loc = nodes[loc][0]
        else:
            loc = nodes[loc][1]
        if loc == 'ZZZ':
            return count
        count += 1
        j += 1
        if j == len(steps):
            j = 0
    return None


def part2(rawdata):
    """Code to solve part 2 of the puzzle"""
    nodes = {}
    loc = []
    groups = rawdata.split('\n\n')
    steps = [i for i in groups[0].strip()]
    for line in groups[1].splitlines():
        node, left, right = re.findall('[0-9A-Z][0-9A-Z][A-Z]',line)
        nodes[node] = [left,right]
        if node[2] == 'A':
            loc.append(node)
    # BBA 21409 BLA 11653 AAA 19241 NFA 12737 DRA 14363 PSA 15989
    cycles = []
    for l in loc:
        c = findpath(l, steps, nodes)
        print(l,c)
        cycles.append(c)
    return np.lcm.reduce(cycles)


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
