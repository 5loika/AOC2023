#!/bin/python3
""" Advent of Code 2023 -- Day 18"""

import sys
import aocd
from collections import defaultdict

TESTDATA1 = TESTDATA2 = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
"""

TEST1 = 62
TEST2 = 952408144115

def part1(rawdata):
    """Code to solve part 1 of the puzzle"""
    outline = defaultdict(lambda: '.')
    board = defaultdict(lambda: '.')
    maxrow = minrow = 0
    maxcol = mincol = 0
    loc = [0,0]
    outline[(loc[0],loc[1])] = '#'
    for l in rawdata.splitlines():
        dir, dist, _ = l.split(' ')
        if dir == 'U':
            delta = [-1,0]
        elif dir == 'D':
            delta = [1,0]
        elif dir == 'L':
            delta = [0,-1]
        elif dir == 'R':
            delta = [0,1]
        for n in range(int(dist)):
            loc[0] += delta[0]
            loc[1] += delta[1]
            maxrow = max(maxrow,loc[0])
            minrow = min(minrow,loc[0])
            maxcol = max(maxcol, loc[1])
            mincol = min(mincol,loc[1])
            outline[(loc[0],loc[1])] = '#'
    rowoffset = 0 - minrow
    coloffset = 0 - mincol
    for row in range(0,maxrow+rowoffset+1):
        for col in range(0,maxcol+coloffset+1):
            if outline[(row-rowoffset,col-coloffset)] == '.':
                board[(row,col)] = 'O'
            else:
                if outline[(row-rowoffset,col-coloffset)] == '#':
                    board[(row,col)] = '#'
                    break
    for row in range(0,maxrow+rowoffset+1):
        for col in range(maxcol+coloffset,-1,-1):
            if outline[(row-rowoffset,col-coloffset)] == '.':
                board[(row,col)] = 'O'
            else:
                if outline[(row-rowoffset,col-coloffset)] == '#':
                    board[(row,col)] = '#'
                    break
    for col in range(0,maxcol+coloffset+1):
        for row in range(0,maxrow+rowoffset+1):
            if outline[(row-rowoffset,col-coloffset)] == '.':
                board[(row,col)] = 'O'
            else:
                if outline[(row-rowoffset,col-coloffset)] == '#':
                    board[(row,col)] = '#'
                    break
    for col in range(0,maxcol+coloffset+1):
        for row in range(maxrow+rowoffset,-1,-1):
            if outline[(row-rowoffset,col-coloffset)] == '.':
                board[(row,col)] = 'O'
            else:
                if outline[(row-rowoffset,col-coloffset)] == '#':
                    board[(row,col)] = '#'
                    break           
    for row in range(0,maxrow+rowoffset+1):
        for col in range(0,maxcol+coloffset+1):
            if outline[(row-rowoffset,col-coloffset)] == '#':
                board[(row,col)] = '#'
    changed = True
    while(changed):
        changed = False
        for row in range(0,maxrow+rowoffset+1):
            for col in range(0,maxcol+coloffset+1):
                if board[(row,col)] == '.':
                    up = (row-1,col)
                    down = (row+1,col)
                    left = (row,col-1)
                    right = (row,col+1)
                    if up in board.keys() and board[up] == 'O':
                        changed = True
                        board[(row,col)] = 'O'
                    if down in board.keys() and board[down] == 'O':
                        changed = True
                        board[(row,col)] = 'O'
                    if left in board.keys() and board[left] == 'O':
                        changed = True
                        board[(row,col)] = 'O'
                    if right in board.keys() and board[right] == 'O':
                        changed = True
                        board[(row,col)] = 'O'


    for j in range(0,maxrow+rowoffset+1):
        for k in range(0,maxcol+coloffset+1):
            if board[(j,k)] == '.':
                board[(j,k)] = '+'

    count = 0
    for j in range(0,maxrow+rowoffset+1):
        for k in range(0,maxcol+coloffset+1):
            if board[(j,k)] == '#' or board[(j,k)] == '+':
                count += 1
            print(board[(j,k)],end='')
        print()

    return count


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
