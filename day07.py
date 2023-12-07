#!/bin/python3.12
""" Advent of Code 2023 -- Day 07"""

import sys
import functools
import aocd

TESTDATA1 = TESTDATA2 = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""

TEST1 = 6440
TEST2 = 5905

cards = {"A":14,"K":13,"Q":12,"J":11,"T":10,"9":9,"8":8,"7":7,"6":6,"5":5,"4":4,"3":3,"2":2}
# cards = {"A":14,"K":13,"Q":12,"J":1,"T":10,"9":9,"8":8,"7":7,"6":6,"5":5,"4":4,"3":3,"2":2}

def cmphands(a,b):
    if a[0] > b[0]:
        return(1)
    if a[0] < b[0]:
        return(-1)
    if a[0] == b[0]:
        for i in range(len(a[1])):
            if a[1][i] == b[1][i]:
                continue
            else:
                if cards[a[1][i]] > cards[b[1][i]]:
                    return(1)
                else:
                    return(-1)
    return(0)

def part1(rawdata):
    """Code to solve part 1 of the puzzle"""
    cards.update({"J":1})
    lines = rawdata.splitlines()
    camelcards = []
    for l in lines:
        hand, bid = l.split(" ")
        all_freq = {}
        for i in hand:
            if i in all_freq:
                all_freq[i] += 1
            else:
                all_freq[i] = 1
        most = max(all_freq.values())
        if most == 5:
            rank = 7
        elif most == 4:
            rank = 6
        elif most == 3:
            if 2 in all_freq.values():
                rank = 5
            else:
                rank = 4
        elif most == 2:
            rank = 1
            for i in all_freq.values():
                if i == 2:
                    rank += 1
        else:
            rank = 1
        
        camelcards.append([rank,hand,int(bid)])
    sortedcards = sorted(camelcards, key=functools.cmp_to_key(cmphands))
    total = 0
    for i in range(len(sortedcards)):
        total += (i+1)*sortedcards[i][2]
    return total

def part2(rawdata):
    """Code to solve part 2 of the puzzle"""
    cards.update({"J":1})
    lines = rawdata.splitlines()
    camelcards = []
    for l in lines:
        hand, bid = l.split(" ")
        jokers = hand.count("J")
        all_freq = {}
        for i in hand:
            if i in all_freq:
                all_freq[i] += 1
            else:
                all_freq[i] = 1
        most = max(all_freq.values())
        if most == 5:
            rank = 7
        elif most == 4:
            rank = 6
            if jokers == 4 or jokers == 1:
                rank = 7
        elif most == 3:
            if 2 in all_freq.values():
                rank = 5
                if jokers == 3 or jokers == 2:
                    rank = 7
            else:
                rank = 4
                if jokers == 1 or jokers == 3:
                    rank = 6
        elif most == 2:
            rank = 1
            for i in all_freq.values():
                if i == 2:
                    rank += 1
            if rank == 3:
                if jokers == 2:
                    rank = 6
                elif jokers == 1:
                    rank = 5
            elif rank == 2:
                if jokers == 2 or jokers == 1:
                    rank = 4
        else:
            rank = 1
            if jokers == 1:
                rank = 2
        
        camelcards.append([rank,hand,int(bid)])
    sortedcards = sorted(camelcards, key=functools.cmp_to_key(cmphands))
    total = 0
    for i in range(len(sortedcards)):
        print(sortedcards[i])
        total += (i+1)*sortedcards[i][2]
    return total


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