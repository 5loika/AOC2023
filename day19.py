#!/bin/python3
""" Advent of Code 2023 -- Day 19"""

import sys
import aocd
import re

TESTDATA1 = TESTDATA2 = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
"""

TEST1 = 19114
TEST2 = 167409079868000

def processpart(rule,part):
    x,m,a,s = re.findall('\d+',part)
    x = int(x)
    m = int(m)
    a = int(a)
    s = int(s)
    for r in rule:
        if eval(r[0]):
            return r[1]
    return None


def part1(rawdata):
    """Code to solve part 1 of the puzzle"""
    program = dict()
    steps, parts = rawdata.split('\n\n')
    for s in steps.splitlines():
        id,rules = s.split('{')
        rules = rules[0:-1]
        q = [q for q in rules.split(',')]
        parsed = []
        for n in range(len(q)-1):
            rule,dest = q[n].split(':')
            parsed.append([rule,dest])
        parsed.append(['True == True',q[-1]])
        program[id] = parsed
        print(id,parsed)
    total = 0
    for p in parts.splitlines():
        print(p)
        next = 'in'
        while next != 'R' and next != 'A':
            print(next,program[next])
            next = processpart(program[next],p)
        if next == 'A':
            x, m, a, s = re.findall('\\d+',p)
            total += int(x) + int(m) + int(a) + int(s)
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
