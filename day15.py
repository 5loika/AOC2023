#!/bin/python3
""" Advent of Code 2023 -- Day 12"""

import sys
import aocd
import re

TESTDATA1 = TESTDATA2 = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""

TEST1 = 1320
TEST2 = 145


def lenshash(lens):
    h = 0
    for c in lens:
        h += ord(c)
        h *= 17
        h = h % 256
    return h

def part1(rawdata):
    """Code to solve part 1 of the puzzle"""
    total = 0
    for w in rawdata.split(','):
        total += lenshash(w)
    return total


def part2(rawdata):
    """Code to solve part 2 of the puzzle"""
    boxes  = {new_list: [] for new_list in range(257)}
    for w in rawdata.split(','):
        if '=' in w:
            lbl, foc = w.split('=')
            box = lenshash(lbl)
            if len(boxes[box]) == 0:
                boxes[box].append([lbl,int(foc)])
            else: 
                found = False
                for i in range(len(boxes[box])):
                    if boxes[box][i][0] == lbl:
                        found = True
                        boxes[box][i][1] = int(foc)
                if not found:
                    boxes[box].append([lbl,int(foc)])
        else:
            lbl,_ = w.split('-')
            box = lenshash(lbl)
            if len(boxes[box]) > 0:
                for i in range(len(boxes[box])):
                    if boxes[box][i][0] == lbl:
                        boxes[box].remove([boxes[box][i][0],boxes[box][i][1]])
                        break
    total = 0
    for n in range(len(boxes)):
        val = 0
        if len(boxes[n]) > 0:
            for j in range(len(boxes[n])):
                val += (n+1) * (j+1) * boxes[n][j][1]
        total += val
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
