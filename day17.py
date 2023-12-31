#!/bin/python3
""" Advent of Code 2023 -- Day 17"""
# 916 is too low (Curiously, it's the right answer for someone else)
# 989 is too high... Wait 5 minutes :(

import sys
import aocd
from collections import defaultdict
from queue import PriorityQueue


TESTDATA1 = TESTDATA2 = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
"""

TEST1 = 102
TEST2 = None

cost = defaultdict(lambda: 65535)
graph = {}

def neighbors(graph, node):
    # dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    dirs = [[0, 1], [-1, 0], [0, -1], [1, 0]]
    result = []
    for dir in dirs:
        neighbor = (node[0] + dir[0], node[1] + dir[1])
        if neighbor in graph.keys():
            result.append(neighbor)
    return result


# A* Heuristic -- Manhattan Distance
def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return (abs(x1 - x2) + abs(y1 - y2)) * 3.2


def part1(rawdata):
    """Code to solve part 1 of the puzzle"""
    cost.clear()
    graph.clear()
    maxcols = maxrows = None
    row = 0
    for l in rawdata.splitlines():
        if maxcols == None:
            maxcols = maxrows = len(l)
        r = [int(x) for x in l]
        col = 0
        for n in r:
            cost[(row, col)] = n
            graph[(row, col)] = []
            col += 1
        row += 1

    for row in range(maxrows):
        for col in range(maxcols):
            for neighbor in neighbors(graph,(row,col)):
                graph[(row, col)].append(neighbor)


    # AStar logic from redblobgames.com
    start = (0, 0)
    goal = (maxrows - 1, maxcols - 1)
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = dict()
    cost_so_far = dict()
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in neighbors(graph, current):
            skip = False
        # if next == came_from[current]:
        #     # print("Skip U turn",next, came_from[current])
        #     skip = True
        # else:
            thispath = []
            node = current
            while came_from[node] != None:
                thispath.append(node)
                node = came_from[node]
            if len(thispath) > 3:
                if next[0] == thispath[0][0] == thispath[1][0] == thispath[2][0] == thispath[3][0]:
                    # print("Skip", next, thispath[0:4])
                    skip = True
                if next[1] == thispath[0][1] == thispath[1][1] == thispath[2][1] == thispath[3][1]:
                    # print("Skip", next, thispath[0:4])
                    skip = True
            if not skip:
                new_cost = cost_so_far[current] + cost[next]
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost
                    #priority = new_cost + heuristic(goal, next)
                    frontier.put(next, priority)                    

                    came_from[next] = current
    bestpath = [
        (0, 1), (0, 2), (1, 2), (1, 3), (1, 4), (1, 5),
        (0, 5), (0, 6), (0, 7), (0, 8), (1, 8), (2, 8),
        (2, 9), (2, 10), (3, 10), (4, 10), (4, 11), (5, 11),
        (6, 11), (7, 11), (7, 12), (8, 12), (9, 12), (10, 12),
        (10, 11), (11, 11), (12, 11), (12, 12)]
    bestcost = 0
    j = 0
    for n in bestpath:
        print('\t',cost[n],n,end='')
        bestcost += cost[n]
        j += 1
        if j % 7 == 0:
            print()
    print()
    print(bestcost)

    path = []
    node = goal
    while node != start:
        path.append(node)
        node = came_from[node]
    path.reverse()
    totalcost = 0
    j = 0
    for n in path:
        print('\t',cost[n],n,end='')
        totalcost += cost[n]
        j += 1
        if j % 7 == 0:
            print()
    print()
    print(totalcost)

    return totalcost


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
