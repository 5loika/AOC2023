#!/bin/python3
""" Advent of Code 2023 -- Day 05"""

import sys
import re
import aocd

TESTDATA1 = TESTDATA2 = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""

TEST1 = 35
TEST2 = 46


def checkmap(m, v):
    """return mapped value"""
    for l in m:
        if v in range(l[1], l[1] + l[2]):
            return v + l[0] - l[1]
    return v


def part1(rawdata):
    """Code to solve part 1 of the puzzle"""
    seeds = []
    locations = []
    seedstosoil = []
    soiltofertilizer = []
    fertilizertowater = []
    watertolight = []
    lighttotemperature = []
    temperaturetohumidity = []
    humiditytolocation = []
    groups = rawdata.split("\n\n")
    for n in re.findall("\\d+", groups[0]):
        seeds.append(int(n))
    for l in groups[1].splitlines():
        # seeds-to-soil
        if not l == "seed-to-soil map:":
            j, k, r = [int(x) for x in l.strip().split()]
            seedstosoil.append([j, k, r])
    for l in groups[2].splitlines():
        # soil-to-fertilizer
        if not l == "soil-to-fertilizer map:":
            j, k, r = [int(x) for x in l.strip().split()]
            soiltofertilizer.append([j, k, r])
    for l in groups[3].splitlines():
        # fertilizer-to-water
        if not l == "fertilizer-to-water map:":
            j, k, r = [int(x) for x in l.strip().split()]
            fertilizertowater.append([j, k, r])
    for l in groups[4].splitlines():
        # water-to-light
        if not l == "water-to-light map:":
            j, k, r = [int(x) for x in l.strip().split()]
            watertolight.append([j, k, r])
    for l in groups[5].splitlines():
        if not l == "light-to-temperature map:":
            # light-to-temperature
            j, k, r = [int(x) for x in l.strip().split()]
            lighttotemperature.append([j, k, r])
    for l in groups[6].splitlines():
        # temperature-to-humidity
        if not l == "temperature-to-humidity map:":
            j, k, r = [int(x) for x in l.strip().split()]
            temperaturetohumidity.append([j, k, r])
    for l in groups[7].splitlines():
        # humidity-to-location
        if not l == "humidity-to-location map:":
            j, k, r = [int(x) for x in l.strip().split()]
            humiditytolocation.append([j, k, r])
    for n in seeds:
        print("Seed", n, end="")
        l = checkmap(seedstosoil, n)
        print(" soil", l, end="")
        l = checkmap(soiltofertilizer, l)
        print(" fertilizer", l, end="")
        l = checkmap(fertilizertowater, l)
        print(" water", l, end="")
        l = checkmap(watertolight, l)
        print(" light", l, end="")
        l = checkmap(lighttotemperature, l)
        print(" temperature", l, end="")
        l = checkmap(temperaturetohumidity, l)
        print(" humidity", l, end="")
        l = checkmap(humiditytolocation, l)
        print(" location", l)
        locations.append(l)
    return min(locations)


def part2(rawdata):
    """Code to solve part 2 of the puzzle"""
    result = None
    seedstosoil = []
    soiltofertilizer = []
    fertilizertowater = []
    watertolight = []
    lighttotemperature = []
    temperaturetohumidity = []
    humiditytolocation = []
    groups = rawdata.split("\n\n")
    seeds = re.findall("\\d+", groups[0])
    for l in groups[1].splitlines():
        # seeds-to-soil
        if not l == "seed-to-soil map:":
            j, k, r = [int(x) for x in l.strip().split()]
            seedstosoil.append([j, k, r])
    for l in groups[2].splitlines():
        # soil-to-fertilizer
        if not l == "soil-to-fertilizer map:":
            j, k, r = [int(x) for x in l.strip().split()]
            soiltofertilizer.append([j, k, r])
    for l in groups[3].splitlines():
        # fertilizer-to-water
        if not l == "fertilizer-to-water map:":
            j, k, r = [int(x) for x in l.strip().split()]
            fertilizertowater.append([j, k, r])
    for l in groups[4].splitlines():
        # water-to-light
        if not l == "water-to-light map:":
            j, k, r = [int(x) for x in l.strip().split()]
            watertolight.append([j, k, r])
    for l in groups[5].splitlines():
        if not l == "light-to-temperature map:":
            # light-to-temperature
            j, k, r = [int(x) for x in l.strip().split()]
            lighttotemperature.append([j, k, r])
    for l in groups[6].splitlines():
        # temperature-to-humidity
        if not l == "temperature-to-humidity map:":
            j, k, r = [int(x) for x in l.strip().split()]
            temperaturetohumidity.append([j, k, r])
    for l in groups[7].splitlines():
        # humidity-to-location
        if not l == "humidity-to-location map:":
            j, k, r = [int(x) for x in l.strip().split()]
            humiditytolocation.append([j, k, r])

    # Brute force approach takes too long to run
    # Attempt to approximate answer by looping through by 1000
    # then step down to 100, 10, and finally 1 to find solution
    # This happens to work for my input, but could miss the best
    # solution with other inputs

    bestk = 0
    narrow = None
    bestn = None
    stop = len(seeds)
    step = 1000
    while True:
        k = bestk
        while k < stop:
            print(
                "Checking locations:",
                int(seeds[k]),
                "to",
                int(seeds[k]) + int(seeds[k + 1]) - 1,
                "Step",
                step,
            )
            for n in range(int(seeds[k]), int(seeds[k]) + int(seeds[k + 1]), step):
                if narrow is None or n in narrow:
                    l = checkmap(seedstosoil, n)
                    l = checkmap(soiltofertilizer, l)
                    l = checkmap(fertilizertowater, l)
                    l = checkmap(watertolight, l)
                    l = checkmap(lighttotemperature, l)
                    l = checkmap(temperaturetohumidity, l)
                    l = checkmap(humiditytolocation, l)
                    if result is None:
                        result = l
                        bestn = n
                        print("Seed:", n, "Location:", l)
                    else:
                        q = min(result, l)
                        if q != result:
                            result = q
                            bestn = n
                            bestk = k
                            print("Seed:", n, "Location:", l)
            k += 2
        if step == 1:
            return result
        narrow = range(bestn - step, bestn + step)
        step = step // 10
        stop = bestk + 1
    return None


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
