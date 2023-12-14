#!/bin/python3
""" Advent of Code 2023 -- Day 12"""

import sys
import aocd
import re

TESTDATA1 = TESTDATA2 = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""

TEST1 = 136
TEST2 = 64

def part1(rawdata):
    """Code to solve part 1 of the puzzle"""
    row = []
    board = []
    for l in rawdata.splitlines():
        row = [c for c in l]
        board.append(row)
    while True:
        changed = 0
        for r in range(1,len(board)):
            for c in range(len(board[r])):
                if board[r][c] == 'O':
                    if board[r-1][c] == '.':
                        board[r-1][c] = 'O'
                        board[r][c] = '.'
                        changed += 1
        if changed == 0:
            break
    score = 0
    for r in range(len(board)):
        score += board[r].count('O') * (len(board) - r)
    return score


def part2(rawdata):
    """Code to solve part 2 of the puzzle"""
    states = {}
    scores = {}
    row = []
    board = []
    for l in rawdata.splitlines():
        row = [c for c in l]
        board.append(row)
    n = 0
    while n <  1000000000:
        north = west = south = east = True
        while north:
            changed = 0
            for r in range(1,len(board)):
                for c in range(len(board[r])):
                    if board[r][c] == 'O':
                        if board[r-1][c] == '.':
                            board[r-1][c] = 'O'
                            board[r][c] = '.'
                            changed += 1
            if changed == 0:
                north = False
        while west:
            changed = 0
            for r in range(len(board)):
                for c in range(1,len(board[r])):
                    if board[r][c] == 'O':
                        if board[r][c-1] == '.':
                            board[r][c-1] = 'O'
                            board[r][c] = '.'
                            changed += 1
            if changed == 0:
                west = False
        while south:
            changed = 0
            for r in range(len(board)-2,-1,-1):
                for c in range(len(board[r])):
                    if board[r][c] == 'O':
                        if board[r+1][c] == '.':
                            board[r+1][c] = 'O'
                            board[r][c] = '.'
                            changed += 1
            if changed == 0:
                south = False
        while east:
            changed = 0
            for r in range(len(board)):
                for c in range(len(board[r])-2,-1,-1):
                    if board[r][c] == 'O':
                        if board[r][c+1] == '.':
                            board[r][c+1] = 'O'
                            board[r][c] = '.'
                            changed += 1
            if changed == 0:
                east = False
        n += 1
        f = str(board)
        if f not in states.keys():
            states[f] = n
            score = 0
            for r in range(len(board)):
                score += board[r].count('O') * (len(board) - r)
            scores[n] = score    
        else:
            first = states[f]
            last = n -1
            print("Repeat of:",states[f],'at',n)
            break
    cycle = last - first + 1
    end = (1000000000 - first) % (cycle)
    print(first+end)
    return scores[first+end]


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
