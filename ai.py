# -*- coding: utf-8 -*-
import unirest
import random
from time import sleep
import enum


API_URL = "http://localhost:8080/"
SESSION_ID = ""
SLEEP_TIME = 0.1


class Direction(enum.Enum):
    up, right, down, left = range(4)


def start_request():
    return unirest.get(API_URL + "hi/start/json")


def move_request(direction):
    return unirest.get(API_URL + "hi/state/" + SESSION_ID + "/move/%d/json" % (direction.value,))


def simulate_move(grid, direction):
    new_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    
    if direction == Direction.up:
        for i in xrange(0, 4):
            column = map(lambda row: row[i], grid)
            merged = merge_list(column)
            for j in xrange(0, 4):
                new_grid[j][i] = merged[j]
    elif direction == Direction.down:
        for i in xrange(0, 4):
            column = map(lambda row: row[i], grid)
            merged = list(reversed(merge_list(reversed(column))))
            for j in xrange(0, 4):
                new_grid[j][i] = merged[j]
    elif direction == Direction.left:
        for i in xrange(0, 4):
            row = grid[i]
            merged = merge_list(row)
            for j in xrange(0, 4):
                new_grid[i][j] = merged[j]
    elif direction == Direction.right:
        for i in xrange(0, 4):
            row = grid[i]
            merged = list(reversed(merge_list(reversed(row))))
            for j in xrange(0, 4):
                new_grid[i][j] = merged[j]

    return new_grid


def merge_list(ls):
    ls = filter(lambda x: x != 0, ls)
    for i in xrange(0, len(ls) - 1):
        if ls[i] == 0:
            continue
        elif ls[i] == ls[i + 1]:
            ls[i] = ls[i] * 2
            ls[i + 1] = 0
    ls = filter(lambda x: x != 0, ls)
    return ls + ([0] * (4 - len(ls)))


def opt_direction(grid):
    # ランダムに方向を決定
    d = [Direction.up, Direction.right, Direction.down, Direction.left]
    return d[random.randint(0, 3)]


def grid_to_str(grid):
    result = "+-----+-----+-----+-----+\n"
    for row in xrange(0, 4):
        result += "|"
        for col in xrange(0, 4):
            result += "%5d" % (grid[row][col])
            result += "|"
        if row == 3:
            result += "\n+-----+-----+-----+-----+\n"
        else:
            result += "\n|-----+-----+-----+-----+\n"
    return result


if __name__ == "__main__":
    result = start_request().body;
    SESSION_ID = result["session_id"]
    while not result["over"]:
        direction = opt_direction(result["grid"])
        result = move_request(direction).body
        print "input: " + ["↑", "→", "↓", "←"][direction.value]
        print grid_to_str(result["grid"])
        if SLEEP_TIME != 0:
            sleep(SLEEP_TIME)
    if result["won"]:
        print "Won."
    else:
        print "Lost."
    print "score: %d" % (result["score"],)