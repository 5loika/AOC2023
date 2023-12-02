#!/bin/python3

import sys
from aocd import data
from aocd import submit

testdata = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

test1 = 8
test2 = 2286

def part1(rawdata):
    cubes = {'red': 12, 'green': 13, 'blue': 14}
    result = 0
    lines = rawdata.splitlines()
    for line in lines:
        valid = True
        game, draws = line.split(':')
        _, game = game.strip().split()
        game = int(game)        
        draws = draws.split(';')
        for d in draws:
            turns = d.split(',')
            for t in turns:
                count,color=t.strip().split()
                count = int(count)
                if count > cubes[color]:
                        valid = False
        if valid:
            result += game
    return result

def part2(rawdata):

    result = 0
    lines = rawdata.splitlines()
    for line in lines:
        cubes = {'red': 0, 'green': 0, 'blue': 0}
        _, draws = line.split(':')
        draws = draws.split(';')
        for d in draws:
            turns = d.split(',')
            for t in turns:
                count,color=t.strip().split()
                count = int(count)
                cubes[color] = max(cubes[color],count)
        power = 1
        for v in cubes.values():
            power *= v
        result += power
    return result


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