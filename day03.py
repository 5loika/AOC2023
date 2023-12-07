#!/bin/python3.12
""" Advent of Code 2023 -- Day 03"""

import sys
import re
import aocd

TESTDATA1 = TESTDATA2 = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

TEST1 = 4361
TEST2 = 467835


def part1(rawdata):
    """Code to solve part 1 of the puzzle"""
    lines = rawdata.splitlines()
    rows = len(lines)
    cols = len(lines[0])
    result = 0
    for r in range(rows):
        # find numbers in row
        nums = re.findall('\\d+',lines[r])
        pos = 0
        for n in nums:
            # find col for each number
            c = lines[r].find(n,pos)
            pos = c + len(n)
            partnum = False
            for j in range(max(r-1,0),min(r+2,rows)):
                for k in range(max(c-1,0),min(c+len(n)+1,cols)):
                    if not lines[j][k].isalnum() and not lines[j][k] == '.':
                        partnum = True
                        break
                if partnum:
                    break
            if partnum:
                result += int(n)
    return result


def part2(rawdata):
    """Code to solve part 2 of the puzzle"""
    lines = rawdata.splitlines()
    rows = len(lines)
    cols = len(lines[0])
    gears = [[None] * cols for i in range(rows)]
    ratio = 0
    for r in range(rows):
        # find numbers in row
        nums = re.findall('\\d+',lines[r])
        pos = 0
        for n in nums:
            # find col for each number
            c = lines[r].find(n,pos)
            pos = c + len(n)
            for j in range(max(r-1,0),min(r+2,rows)):
                for k in range(max(c-1,0),min(c+len(n)+1,cols)):
                    if lines[j][k] == '*':
                        if gears[j][k] is None:
                            gears[j][k] = [int(n)]
                        else:
                            gears[j][k].append(int(n))
    for r in range(rows):
        for c in range(cols):
            if gears[r][c] is not None:
                if len(gears[r][c]) == 2:
                    ratio += gears[r][c][0] * gears[r][c][1]
    return ratio

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
