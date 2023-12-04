#!/bin/python3
""" Advent of Code 2023 -- Day 04"""

import sys
import re
import aocd

TESTDATA1 = TESTDATA2 = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""

TEST1 = 13
TEST2 = 30


def part1(rawdata):
    """Code to solve part 1 of the puzzle"""
    result = 0
    lines = rawdata.splitlines()
    for line in lines:
        wincount = 0
        _, nums = line.strip().split(':')
        l, r = nums.strip().split('|')
        win = re.findall('\\d+',l)
        draw = re.findall('\\d+',r)
        for n in draw:
            if n in win:
                wincount += 1
        if wincount > 0:
            result += 2**(wincount-1)
    return result


def part2(rawdata):
    """Code to solve part 2 of the puzzle"""
    result = 0
    lines = rawdata.splitlines()
    tickets = [1 for _ in range(len(lines))]
    for line in lines:
        card, nums = line.strip().split(':')
        card = int(re.findall('\\d+',card)[0])
        l, r = nums.strip().split('|')
        win = re.findall('\\d+',l)
        draw = re.findall('\\d+',r)
        wincount = 0
        j = 1
        for n in draw:
            if n in win:
                copies = tickets[card-1]
                tickets[card-1+j] += copies
                wincount += 1
                j += 1
    for n in tickets:
        result += n
    return result


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
