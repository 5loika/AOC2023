#!/bin/python3
""" Advent of Code 2023 -- Day 12"""

import sys
import aocd
from itertools import combinations
from itertools import permutations
import re

TESTDATA1 = TESTDATA2 = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
"""

TEST1 = 21
TEST2 = None


def part1(rawdata):
    """Code to solve part 1 of the puzzle"""
    springs = []
    repair = []
    lines = rawdata.splitlines()
    for l in lines:
        a, b = l.split()
        springs.append(a)
        repair.append([int(x) for x in b.split(',')])
    total = 0
    for d in range(len(springs)):
        j = springs[d].count('?') # how many unknown
        y = sum(repair[d]) # how many aprings do we need
        k = springs[d].count('#') # how many springs do we have
        p = ''.join(['#' for i in range(y-k)]) #springs 
        p = p + ''.join(['.' for i in range(j-(y-k))]) # empty
        o = set(permutations(p,j))
        print(j,y,k,len(o),p)
        for q in o:
            t = springs[d] #copy.copy(s)
            for c in q:
                n = t.index('?')
                t = t[:n]+c+t[n+1:]
            w = re.findall('#+',t)
            r = []
            for x in w:
                r.append(len(x))
            if r == repair[d]:
                print(springs[d],'\t',t,'\t',repair[d],'\t',r)
                total += 1
        print(d)
    print(total)
    return total


def part2(rawdata):
    """Code to solve part 2 of the puzzle"""

    return None


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
